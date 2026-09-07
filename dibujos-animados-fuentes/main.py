import argparse
import os
import queue
import random
import shutil
import subprocess
import sys
import threading
import wave
import pygame
import cv2
import numpy as np

import config
import scene
import music
from drawing_processor import load_drawing
from sprites import DrawingSprite, AnimatedSprite, TextSprite, TRAJECTORIES, TRAJ_DY_RANGES
from sprite_matcher import find_best_sheet
from text_detector import detect_text_crop, _name_from_filename

# Separación mínima en Y (px) — debe ser >= altura real del sprite para evitar encimamiento
_MIN_SEP = 260

# Cola thread-safe: el hilo de detección deposita todo lo necesario para
# crear el sprite + texto juntos en el hilo principal.
_ready_queue: queue.Queue = queue.Queue()

# Mazo barajado: todas las trayectorias se usan antes de repetir,
# y nunca dos imágenes consecutivas comparten la misma.
_traj_deck: list[int] = []
_last_traj: int | None = None

# Desfase horizontal cíclico: cada sprite entra en un momento distinto del recorrido
# para que nunca coincidan varios en x≈0 al mismo tiempo.
# Valores negativos = el sprite comienza fuera de pantalla por la izquierda.
_X_OFFSETS = [0, -300, -600, -900]
_x_offset_idx: int = 0

def _pick_trajectory() -> int:
    global _traj_deck, _last_traj
    if not _traj_deck:
        deck = list(range(len(TRAJECTORIES)))
        random.shuffle(deck)
        if _last_traj is not None and deck[0] == _last_traj:
            deck.append(deck.pop(0))
        _traj_deck = deck
    chosen = _traj_deck.pop(0)
    _last_traj = chosen
    return chosen


def _pick_base_x() -> int:
    """Desfase horizontal cíclico: distribuye los sprites a lo ancho del recorrido."""
    global _x_offset_idx
    x = _X_OFFSETS[_x_offset_idx % len(_X_OFFSETS)]
    _x_offset_idx += 1
    return x


def _visual_y(sprite) -> int:
    """Posición Y visual del sprite al inicio de su trayectoria (t=0)."""
    dy0 = 0
    if hasattr(sprite, 'trajectory') and sprite.trajectory is not None:
        _, dy0 = TRAJECTORIES[sprite.trajectory](0.0)
    return int(getattr(sprite, 'base_y', 0) + dy0)


def _pick_spawn_y(active_sprites: list, now: float, traj_idx: int) -> int:
    """
    Devuelve un base_y tal que el sprite nunca sale del escenario (arriba ni abajo)
    durante toda la trayectoria. Usa el rango real (dy_min, dy_max) de la trayectoria.
    """
    dy_min, dy_max = TRAJ_DY_RANGES[traj_idx]
    anim_margin = 12          # margen extra por dy_anim = sin(...) * 10
    frame_h = config.MAX_DRAWING_WIDTH

    # base_y debe satisfacer:
    #   base_y + dy_min - anim_margin >= 0        (no salir por arriba)
    #   base_y + dy_max + frame_h + anim_margin <= HEIGHT  (no salir por abajo)
    base_min = max(0, int(-dy_min + anim_margin))
    base_max = int(config.HEIGHT - frame_h - dy_max - anim_margin)
    if base_max < base_min:
        # Trayectoria con amplitud mayor que la pantalla: usar el centro factible
        base_max = base_min

    occupied = [
        _visual_y(s) for s in active_sprites
        if hasattr(s, 'base_y') and s.is_visible(now)
        and not isinstance(s, TextSprite)
    ]

    def _free(y: int) -> bool:
        return all(abs(y - oy) >= _MIN_SEP for oy in occupied)

    candidates = [y for y in range(base_min, base_max + 1, 6) if _free(y)]
    if candidates:
        return random.choice(candidates)
    if occupied:
        return max(range(base_min, base_max + 1, 6) or [base_min],
                   key=lambda y: min(abs(y - oy) for oy in occupied))
    return (base_min + base_max) // 2


_label_font: pygame.font.Font | None = None

def _get_label_font() -> pygame.font.Font:
    global _label_font
    if _label_font is None:
        _label_font = pygame.font.SysFont('segoeui', 18, bold=True)
    return _label_font


def _make_text_surface(name: str) -> pygame.Surface:
    """Renderiza el nombre con fuente pequeña cuando no hay crop de OCR."""
    font = _get_label_font()
    text_surf = font.render(name, True, (255, 255, 255))
    tw, th = text_surf.get_size()
    bg = pygame.Surface((tw + 10, th + 6), pygame.SRCALPHA)
    bg.fill((0, 0, 0, 140))
    bg.blit(text_surf, (5, 3))
    return bg


def _detect_and_prepare(image_path: str) -> None:
    """
    Corre en hilo separado: busca el sprite sheet y detecta texto.
    Deposita el resultado en _ready_queue para que el hilo principal
    cree el sprite y el texto juntos en el mismo frame.
    """
    fname = os.path.basename(image_path)
    sheet_path, rows, cols = find_best_sheet(image_path)
    text, rgba_crop = detect_text_crop(image_path)
    if rgba_crop is not None:
        print(f"[OCR] {fname}: '{text}' — recorte {rgba_crop.shape[1]}×{rgba_crop.shape[0]} px")
    else:
        print(f"[OCR] {fname}: sin texto detectado")
    _ready_queue.put((image_path, sheet_path, rows, cols, rgba_crop))

AUTO_DURATION = 60          # segundos que permanece visible cada sprite auto-detectado
LOAD_DELAY = 0.8            # segundos de espera antes de cargar (archivos puede seguir escribiendose)
TOAST_DURATION = 3.5        # segundos que dura el aviso en pantalla

_IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}

PDF_WATCH_DIR = r"C:\Users\user21\Documents"
PDF_LOAD_DELAY = 2.0    # espera extra antes de leer el PDF (puede seguir escribiéndose)

#------------------------------
# PDF extractor — convierte IMG_*.pdf a .jpg en assets/scanned
#------------------------------

_CROP_RIGHT_PT = 2.5 / 2.54 * 72   # 2.5 cm en puntos PDF (72 pt/pulgada)

def _extract_pdf_to_jpg(pdf_path: str, out_dir: str) -> list[str]:
    """Extrae cada página de un PDF como JPG en out_dir. Omite páginas ya extraídas."""
    try:
        import fitz
    except ImportError:
        print("[PDF] PyMuPDF no instalado — ejecuta:  pip install pymupdf")
        return []
    if not os.path.isfile(pdf_path):
        print(f"[PDF] Archivo no encontrado: {pdf_path}")
        return []
    base = os.path.splitext(os.path.basename(pdf_path))[0]
    saved = []
    try:
        doc = fitz.open(pdf_path)
        mat = fitz.Matrix(2.0, 2.0)     # 2× zoom → ~144 dpi
        for i, page in enumerate(doc):
            suffix = "" if len(doc) == 1 else f"_p{i + 1}"
            out_path = os.path.join(out_dir, f"{base}{suffix}.jpg")
            if os.path.exists(out_path):
                print(f"[PDF] Ya existe, se omite: {os.path.basename(out_path)}")
                continue
            clip = fitz.Rect(0, 0, page.rect.width - _CROP_RIGHT_PT, page.rect.height)
            pix = page.get_pixmap(matrix=mat, clip=clip)
            pix.save(out_path)
            saved.append(out_path)
            print(f"[PDF] Extraído (recorte derecho 2.5 cm): {os.path.basename(out_path)}")
        doc.close()
    except Exception as exc:
        print(f"[PDF] Error procesando {os.path.basename(pdf_path)}: {exc}")
    return saved


class PDFWatcher:
    """Vigila PDF_WATCH_DIR para archivos IMG_*.pdf y los convierte a JPG en assets/scanned."""
    CHECK_INTERVAL = 2.0

    def __init__(self, out_dir: str):
        self.out_dir = out_dir
        # _known vacío → detecta también los PDFs que ya existen al arrancar
        self._known: set[str] = set()
        # _timer inicia en CHECK_INTERVAL → primer escaneo ocurre en el primer frame
        self._timer = self.CHECK_INTERVAL
        self._elapsed = 0.0
        self._pending: list[tuple[str, float]] = []     # (path_pdf, tiempo_detección)

    def _scan(self) -> set[str]:
        if not os.path.isdir(PDF_WATCH_DIR):
            print(f"[PDF] Directorio no encontrado: {PDF_WATCH_DIR}")
            return set()
        return {
            f for f in os.listdir(PDF_WATCH_DIR)
            if f.upper().startswith("IMG_") and f.lower().endswith(".pdf")
        }

    def update(self, dt: float) -> None:
        """Llama en cada frame. Extrae PDFs listos a out_dir (HotWatcher los animará)."""
        self._elapsed += dt
        self._timer += dt

        if self._timer >= self.CHECK_INTERVAL:
            self._timer = 0.0
            current = self._scan()
            nuevos = current - self._known
            for fname in nuevos:
                path = os.path.join(PDF_WATCH_DIR, fname)
                self._pending.append((path, self._elapsed))
                print(f"[PDF] PDF detectado: {fname}")
            self._known = current

        ready = [(p, t) for p, t in self._pending if self._elapsed - t >= PDF_LOAD_DELAY]
        self._pending = [(p, t) for p, t in self._pending if self._elapsed - t < PDF_LOAD_DELAY]
        for path, _ in ready:
            _extract_pdf_to_jpg(path, self.out_dir)


#------------------------------
# Hotwatcher - detecta archivos nuevos en el directorio de assets
#------------------------------

class HotWatcher:
    CHECK_INTERVAL = 1.0

    def __init__(self, folder: str, preloaded: set[str] | None = None):
        self.folder = folder
        # Archivos ya cargados en la carga inicial — no se detectan como nuevos
        self._known: set[str] = set(preloaded) if preloaded else set()
        self._timer = 0.0
        self._elapsed = 0.0
        self._pending: list [tuple[str, float]] = []        # (path, tiempo_detección)

    def _scan(self) -> set[str]:
        if not os.path.isdir(self.folder):
            return set()
        return {
            f for f in os.listdir(self.folder)
            if os.path.splitext(f)[1].lower() in _IMAGE_EXTS
        }
    def update(self, dt: float) -> list[str]:
        """llama en cada frame. Devuelve paths de archivos listos para cargar """
        self._elapsed += dt
        self._timer += dt

        if self._timer >= self.CHECK_INTERVAL:
            self._timer = 0.0
            current = self._scan()
            for fname in current - self._known:
                path = os.path.join(self.folder, fname)
                self._pending.append((path, self._elapsed))
                print(f"[HOT] Nuevo archivo detectado: {fname} ")
            self._known = current
        
        ready = []
        still_pending = []
        for path, detected_at in self._pending:
            if self._elapsed - detected_at >= LOAD_DELAY:
                ready.append(path)
            else:
                still_pending.append((path, detected_at))
        self._pending = still_pending
        return ready
    
#------------------------
# Toast - aviso cuando aparece una imagen nueva
#------------------------

class Toast:
    def __init__(self, text: str, born: float, font: pygame.font.Font):
        self.text = text
        self.born = born
        self.font = font

    def alive(self, now: float) -> bool:
        return now -self.born < TOAST_DURATION
    
    def draw(self, surface: pygame.Surface, now: float, row: int):
        age = now - self.born
        fade = min(1.0, (TOAST_DURATION - age) / 0.7)
        alpha = int(fade * 230)
        label = self.font.render(f"✦ {self.text}", True, (180, 255, 140))
        bg = pygame.Surface((label.get_width() + 20, label.get_height() + 10),
                            pygame.SRCALPHA)
        bg.fill((10, 10, 30, int(fade * 160)))
        bg.blit(label, (10, 5))
        bg.set_alpha(alpha)
        surface.blit(bg, (18, 18 + row * (label.get_height() + 14)))

def make_video_writer(path: str) -> cv2.VideoWriter:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    return cv2.VideoWriter(path, fourcc, config.FPS, (config.WIDTH, config.HEIGHT))

def _save_wav(path: str, pcm: np.ndarray, sr: int) -> None:
    with wave.open(path, "w") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)   # 16-bit
        wf.setframerate(sr)
        wf.writeframes(pcm.tobytes())

def _merge_av(video_path: str, audio_path: str, output_path: str) -> bool:
    """Combina video y audio con FFmpeg. Devuelve True si tuvo éxito."""
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        output_path,
    ]
    result = subprocess.run(cmd, capture_output=True)
    if result.returncode != 0:
        print("[AVISO] FFmpeg falló — el video se guardará sin audio.")
        print(result.stderr.decode(errors="replace"))
        return False
    return True

#-----------------------------
# main
#----------------------

def parse_args():
    parser = argparse.ArgumentParser(description="Bosque mágico - animación")
    parser.add_argument(
        "--bg-alpha", type=int, default=config.BG_ALPHA,
        metavar="0-255",
        help=f"Transparencia del escenario (0=invisible, 255=opaco). Por defecto: {config.BG_ALPHA}",
    )
    parser.add_argument(
        "--grabar", action="store_true",
        help="Graba la animación en video (desactivado por defecto)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    config.BG_ALPHA = max(0, min(255, args.bg_alpha))

    if args.grabar and not shutil.which("ffmpeg"):
        print("Error: --grabar requiere FFmpeg pero no se encontró en PATH.")
        print("Instálalo con:  winget install ffmpeg")
        sys.exit(1)

    music.pre_init()
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("Bosque mágico")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("segoeui", 22, bold=True)

    _music = music.generate_and_play()          # mantener referencia para evitar GC

    # Sin sprites al iniciar — solo aparecen cuando llega una imagen a scanned/
    sprites: list[DrawingSprite | AnimatedSprite] = []

    watcher = HotWatcher(config.ASSETS_DIR)
    pdf_watcher = PDFWatcher(config.ASSETS_DIR)
    toasts: list[Toast] = []

    _video_tmp = config.OUTPUT_PATH.replace(".mp4", "_tmp_video.mp4")
    writer = make_video_writer(_video_tmp) if args.grabar else None

    elapsed_sec = 0.0
    running = True

    if args.grabar:
        print(f"Grabando animación {config.TOTAL_SECONDS}s -> {config.OUTPUT_PATH}")
    else:
        print("Modo previsualización (sin grabación). Usa --grabar para guardar video.")
    print(f"Detectando imágenes nuevas en: {config.ASSETS_DIR} ")
    print("presione ESC o cierra la ventana para terinar antes de tiempo")

    while running and elapsed_sec <= config.TOTAL_SECONDS:
        dt = clock.tick(config.FPS) / 1000.0            # segundos transcurridos en este frame()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # convierte PDFs nuevos → JPG en assets/scanned (HotWatcher los recoge)
        pdf_watcher.update(dt)

        # Lanza hilo de detección para cada imagen nueva (no bloquea el loop)
        for path in watcher.update(dt):
            print(f"[HOT] Detectado: {os.path.basename(path)} — procesando en segundo plano...")
            threading.Thread(
                target=_detect_and_prepare,
                args=(path,),
                daemon=True,
            ).start()

        # Cuando la detección termina, crea sprite + texto juntos (pygame solo en hilo principal)
        while not _ready_queue.empty():
            try:
                image_path, sheet_path, rows, cols, rgba_crop = _ready_queue.get_nowait()
            except queue.Empty:
                break
            fname = os.path.basename(image_path)
            traj_idx = _pick_trajectory()
            base_y = _pick_spawn_y(sprites, elapsed_sec, traj_idx)
            base_x = _pick_base_x()
            pos = (base_x, base_y)
            try:
                if sheet_path:
                    sprite = AnimatedSprite(
                        sheet_path=sheet_path,
                        rows=rows, cols=cols,
                        start_sec=elapsed_sec,
                        duration_sec=AUTO_DURATION,
                        position=pos,
                        trajectory=traj_idx,
                        color_source=image_path,
                    )
                    sprites.append(sprite)

                    # Construir superficie del nombre (crop OCR o fuente de respaldo)
                    if rgba_crop is not None:
                        h, w = rgba_crop.shape[:2]
                        target_w = max(12, w // 10)
                        target_h = max(4, h // 10)
                        tsurf = pygame.image.frombuffer(rgba_crop.tobytes(), (w, h), "RGBA").convert_alpha()
                        tsurf = pygame.transform.smoothscale(tsurf, (target_w, target_h))
                    else:
                        # OCR no encontró texto: renderizar nombre del archivo
                        tsurf = _make_text_surface(_name_from_filename(image_path))

                    frame_w = sprite.frames[0].get_width()  if sprite.frames else config.MAX_DRAWING_WIDTH
                    frame_h = sprite.frames[0].get_height() if sprite.frames else config.MAX_DRAWING_WIDTH
                    tw = tsurf.get_width()
                    text_base_x = pos[0] + (frame_w - tw) / 2
                    text_base_y = base_y + frame_h - 40
                    sprites.append(TextSprite(
                        surface=tsurf,
                        start_sec=elapsed_sec,
                        duration_sec=AUTO_DURATION,
                        position=(text_base_x, text_base_y),
                        trajectory=traj_idx,
                        phase=sprite.phase,
                    ))

                    sheet_name = os.path.basename(sheet_path)
                    toasts.append(Toast(f"{fname} → {sheet_name}", elapsed_sec, font))
                    print(f"[HOT] {fname} → {sheet_name} base_y={base_y} traj={traj_idx}")
                else:
                    surface = load_drawing(image_path)
                    sprites.append(DrawingSprite(
                        surface=surface,
                        start_sec=elapsed_sec,
                        duration_sec=AUTO_DURATION,
                        position=pos,
                        trajectory=traj_idx,
                    ))
                    toasts.append(Toast(fname, elapsed_sec, font))
                    print(f"[HOT] {fname} → sin sheet base_y={base_y} traj={traj_idx}")
            except Exception as exc:
                print(f"[Error] No se puede crear sprite para {fname}: {exc}")

        # actualizar escena
        scene.update(dt)

        # dibujar fondo
        scene.draw(screen, elapsed_sec)

        # dibujar sprites detectados en scanned/
        for sprite in sprites:
            sprite.draw(screen, elapsed_sec)

        # dibujar toasts activos
        toasts = [t for t in toasts if t.alive(elapsed_sec)]
        for row, toast in enumerate(toasts):
            toast.draw(screen, elapsed_sec, row)

        # mostrar en pantalla
        pygame.display.flip()

        if writer is not None:
            frame = pygame.surfarray.array3d(screen).transpose(1, 0, 2)
            writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

        elapsed_sec += dt

    # Siempre exportar audio al salir
    print("[Audio] Exportando audio...")
    _wav_out = config.OUTPUT_PATH.replace(".mp4", ".wav")
    _save_wav(_wav_out, music.build_full_track(elapsed_sec), music.SR)
    print(f"[Audio] Guardado en: {_wav_out}")

    if writer is not None:
        writer.release()
        print("[Grabación] Combinando video y audio...")
        if _merge_av(_video_tmp, _wav_out, config.OUTPUT_PATH):
            print(f"[Grabación] Video con audio guardado en: {config.OUTPUT_PATH}")
        else:
            shutil.copy(_video_tmp, config.OUTPUT_PATH)
            print(f"[Grabación] Video (sin audio) guardado en: {config.OUTPUT_PATH}")
        os.remove(_video_tmp)
    pygame.quit()

if __name__ == "__main__":
    main()





