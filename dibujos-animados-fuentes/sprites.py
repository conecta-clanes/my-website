import pygame
import random
import math
import numpy as np
from PIL import Image
import config

FADE_DURATION = 0.4         # segundos de fade alpha al entrar / salir
ENTRY_DURATION = 0.9  # segundos del pop elástico de entrada

# Tipos de animación contnua

ANIM_FLOAT = 'float'        # sube y baja suavemente
ANIM_SWAY = 'sway'          # balanceo lateral (rotación)
ANIM_PULSE = 'pulse'        # respira (escala oscilante)
ANIM_ORBIT = 'orbit'        # pequeña orbita elptica
ANIM_BOUNCE = 'bounce'      # rebote vertical
ANIM_WIGGLE = 'wiggle'      # meneo: rotación + escala combinados

ALL_ANIMS = [ANIM_FLOAT, ANIM_SWAY, ANIM_PULSE, 
             ANIM_ORBIT, ANIM_BOUNCE, ANIM_WIGGLE ] 

# ------------------------------------
# Trayectorias — devuelven (dx, dy) en px dado t_norm ∈ [0, 1]
# Todas avanzan de izquierda a derecha (dx creciente).
# dy positivo = hacia abajo en pantalla; negativo = hacia arriba.
# ------------------------------------

def _traj_sine(t: float) -> tuple[float, float]:
    """Seno: 1 ciclo completo con amplitud ±210 px — ola claramente visible."""
    return t * 1280.0, math.sin(t * 2 * math.pi) * 210.0

def _traj_cosine(t: float) -> tuple[float, float]:
    """Coseno: arranca en cresta (+210), baja a valle (−210) y regresa."""
    return t * 1280.0, (math.cos(t * 2 * math.pi) - 1.0) * 105.0  # [0, −210]

def _traj_cotangent(t: float) -> tuple[float, float]:
    """Cotangente: S-curve de +200 a −200 px (descenso acelerado al centro)."""
    angle = math.pi / 4 + t * (math.pi / 2)
    dy = (math.cos(angle) / math.sin(angle)) * 200.0
    return t * 1280.0, dy

def _traj_parabola(t: float) -> tuple[float, float]:
    """Parábola invertida: sube 300 px en el centro y regresa al nivel base."""
    dy = -(4.0 * t * (1.0 - t)) * 300.0
    return t * 1280.0, dy

def _traj_hyperbola(t: float) -> tuple[float, float]:
    """Hipérbola: arranca plano y se dispara hacia abajo ~280 px al final."""
    x = t * 4.0
    dy = 70.0 * (math.sqrt(1.0 + x ** 2) - 1.0)
    return t * 1280.0, dy

def _traj_ascend(t: float) -> tuple[float, float]:
    """Ascendente: sube 280 px en línea recta diagonal."""
    return t * 1280.0, -t * 280.0

def _traj_zigzag(t: float) -> tuple[float, float]:
    """Zigzag: 4 dientes de sierra de ±150 px cruzando la pantalla."""
    phase = (t * 4.0) % 1.0
    dy = (1.0 - 4.0 * abs(phase - 0.5)) * 150.0
    return t * 1280.0, dy

TRAJECTORIES = [
    _traj_sine,       # 0 — seno
    _traj_cosine,     # 1 — coseno
    _traj_cotangent,  # 2 — cotangente
    _traj_parabola,   # 3 — parábola
    _traj_hyperbola,  # 4 — hipérbola
    _traj_ascend,     # 5 — ascendente
    _traj_zigzag,     # 6 — zigzag
]

# Rango real de dy para cada trayectoria, muestreado con 400 puntos.
# Usado para calcular base_y válido que garantice que el sprite no salga de pantalla.
def _traj_dy_range(fn) -> tuple[float, float]:
    ys = [fn(i / 400)[1] for i in range(401)]
    return min(ys), max(ys)

TRAJ_DY_RANGES: list[tuple[float, float]] = [_traj_dy_range(fn) for fn in TRAJECTORIES]


def _ease_back_out(t: float) -> float:
    """Scale de 0 -> 1 con ligero overshot, para el pop entrada"""
    t = max(0.0, min(1.0, t))
    c1 = 1.70158
    c3 = c1 + 1
    return 1.0 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2 


class DrawingSprite:
    def __init__(self, surface: pygame.Surface, start_sec: float,
                 duration_sec: float, position: tuple,
                 anim_type: str | None = None, phase: float | None = None,
                 trajectory: int | None = None):
        self.surface = surface
        self.start = start_sec
        self.end = start_sec + duration_sec
        self.base_x , self.base_y = float(position[0]), float(position[1])
        self.anim_type = anim_type or random.choice(ALL_ANIMS)
        self.phase = phase if phase is not None else random.uniform(0, math.pi * 2)
        self.trajectory = trajectory
        self._w, self._h = surface.get_size()
        # rotozoom cache — avoids recomputing identical transforms every frame
        self._cached_surf: pygame.Surface = surface
        self._ca: float = 0.0
        self._cs: float = 1.0

    # ---------------------------
    # visibilidad y alpha
    # ---------------------------

    def is_visible(self, current_sec: float) -> bool:
        return self.start <= current_sec <= self.end
    
    def get_alpha(self, current_sec: float) -> int:
        elapsed = current_sec - self.start
        remaining = self.end - current_sec

        if elapsed < FADE_DURATION:
            a = elapsed / FADE_DURATION
        elif remaining < FADE_DURATION:
            a = remaining / FADE_DURATION
        else:
            a = 1.0
        
        return int(max(0, min(255, a * 255)))
    
    #----------------------------------
    # Animación: devulve (angle,_deg, scale, dx, dy)
    #----------------------------------
    def _get_transform(self, t: float) -> tuple[float, float, float, float]:
        # fase de entrada:pop elástico - escala crece de 0 a 1 con overshoot
        if t < ENTRY_DURATION:
            entry_scale = _ease_back_out(t /ENTRY_DURATION)
            return 0.0, entry_scale, 0.0, 0.0
        
        t2 = t - ENTRY_DURATION         # tiempo tras la entrada

        if self.anim_type == ANIM_FLOAT:
            dy = math.sin(t2 * 1.3 + self.phase) * 10
            return 0.0, 1.0, 0.0, dy
        
        elif self.anim_type == ANIM_SWAY:
            angle = math.sin(t2 * 0.9 + self.phase) * 8
            return angle, 1.0, 0.0, 0.0

        elif self.anim_type == ANIM_PULSE:
            scale = 1.0 + math.sin(t2 *1.6 +self.phase) * 0.08
            dy = math.sin(t2 * 0.8 + self.phase) * 5
            return 0.0, scale, 0.0, dy
         
        elif self.anim_type == ANIM_ORBIT:
            r = 16
            dx = math.cos(t2 * 0.8 + self.phase) * r
            dy = math.sin(t2 * 0.8 + self.phase ) * r * 0.5
            return 0.0, 1.0, dx , dy
        
        elif self.anim_type == ANIM_BOUNCE:
            bounce = abs(math.sin(t2 * 2.0 + self.phase))
            dy = -bounce *16
            scale = 0.96 + 0.04 * bounce        # ligera compresión al tocar fondo
            return 0.0, scale, 0.0, dy
        
        elif self.anim_type == ANIM_WIGGLE:
            angle = math.sin(t2 * 2.6 + self.phase) * 6
            scale = 1.0 + math.sin(t2 * 3.1 + self.phase + math.pi /3) * 0.05
            return angle, scale, 0.0, 0.0
        
        return 0.0, 1.0, 0.0, 0.0

    #----------------------------------
    # dibujo
    #---------------------------------

    def _get_cached_surf(self, angle: float, scale: float) -> pygame.Surface:
        """Devuelve surface transformada; reutiliza caché si angle/scale no cambiaron."""
        ra = round(angle)               # grado más cercano
        rs = round(scale * 100) / 100   # 0.01 más cercano
        if ra == self._ca and rs == self._cs:
            return self._cached_surf
        if ra != 0 or rs != 1.0:
            self._cached_surf = pygame.transform.rotozoom(self.surface, ra, rs)
        else:
            self._cached_surf = self.surface
        self._ca, self._cs = ra, rs
        return self._cached_surf

    def draw(self, screen: pygame.Surface, current_sec: float):
        if not self.is_visible(current_sec):
            return

        alpha = self.get_alpha(current_sec)
        t = current_sec - self.start
        duration = self.end - self.start
        t_norm = t / duration if duration > 0 else 0.0

        angle, scale, dx_anim, dy_anim = self._get_transform(t)

        if self.trajectory is not None:
            dx_traj, dy_traj = TRAJECTORIES[self.trajectory](t_norm)
        else:
            dx_traj, dy_traj = 0.0, 0.0

        surf = self._get_cached_surf(angle, scale)

        sw, sh = surf.get_size()
        x = int(self.base_x + dx_traj + dx_anim + (self._w - sw) / 2)
        y = int(self.base_y + dy_traj + dy_anim + (self._h - sh) / 2)
        y = max(0, min(config.HEIGHT - sh, y))

        surf.set_alpha(alpha)
        screen.blit(surf, (x, y))


# ---------------------------------------------------------------------------
# AnimatedSprite — reproduce frames de un sprite sheet
# ---------------------------------------------------------------------------

ANIM_SHEET_FPS = 10     # cuadros de animación por segundo


class AnimatedSprite:
    """Sprite animado que cicla los frames de un sprite sheet detectado."""

    _label_font: pygame.font.Font | None = None

    @classmethod
    def _get_label_font(cls) -> pygame.font.Font:
        if cls._label_font is None:
            cls._label_font = pygame.font.SysFont("segoeui", 17, bold=True)
        return cls._label_font

    def __init__(self, sheet_path: str, rows: int, cols: int,
                 start_sec: float, duration_sec: float,
                 position: tuple,
                 trajectory: int | None = None,
                 phase: float | None = None,
                 color_source: str | None = None,
                 label: str | None = None):
        from colorizer import extract_color_stats
        lab_stats = extract_color_stats(color_source) if color_source else None
        self.frames = self._load_frames(sheet_path, rows, cols, lab_stats)
        self.start = start_sec
        self.end = start_sec + duration_sec
        self.base_x, self.base_y = float(position[0]), float(position[1])
        self.trajectory = trajectory if trajectory is not None else random.randint(0, len(TRAJECTORIES) - 1)
        self.phase = phase if phase is not None else random.uniform(0, math.pi * 2)
        self._fw, self._fh = self.frames[0].get_size() if self.frames else (0, 0)
        self.label = label

    # ------------------------------------------------------------------
    def _load_frames(self, sheet_path: str, rows: int, cols: int,
                     lab_stats: tuple | None) -> list[pygame.Surface]:
        from colorizer import apply_color_to_frame
        try:
            pil_sheet = Image.open(sheet_path).convert("RGBA")
        except Exception as exc:
            print(f"[SPRITE] Error cargando sheet {sheet_path}: {exc}")
            return []

        sw, sh = pil_sheet.size
        fw, fh = sw // cols, sh // rows
        data_sheet = np.array(pil_sheet, dtype=np.uint8)
        threshold = config.WHITE_THRESHOLD

        # Escala uniforme para todos los frames
        target_w = config.MAX_DRAWING_WIDTH
        if fw > target_w:
            scale = target_w / fw
            new_fw = target_w
            new_fh = max(1, int(fh * scale))
        else:
            new_fw, new_fh = fw, fh

        frames: list[pygame.Surface] = []
        for r in range(rows):
            for c in range(cols):
                y0, y1 = r * fh, (r + 1) * fh
                x0, x1 = c * fw, (c + 1) * fw
                data = data_sheet[y0:y1, x0:x1].copy()

                # Eliminar fondo blanco
                rc, gc, bc = data[:, :, 0], data[:, :, 1], data[:, :, 2]
                white = (rc > threshold) & (gc > threshold) & (bc > threshold)
                data[:, :, 3] = np.where(white, 0, data[:, :, 3])

                if data[:, :, 3].max() == 0:
                    continue  # frame vacío

                if (new_fw, new_fh) != (fw, fh):
                    pil_frame = Image.fromarray(data, "RGBA").resize((new_fw, new_fh), Image.LANCZOS)
                    data = np.array(pil_frame, dtype=np.uint8)

                # Aplicar color de la imagen escaneada (si la tiene)
                if lab_stats is not None:
                    data = apply_color_to_frame(data, lab_stats)

                h, w = data.shape[:2]
                surf = pygame.image.frombuffer(data.tobytes(), (w, h), "RGBA").convert_alpha()
                frames.append(surf)

        color_tag = "con recoloración" if lab_stats else "colores originales"
        print(f"[SPRITE] {len(frames)} frames cargados ({new_fw}×{new_fh} px, {color_tag})")
        return frames

    # ------------------------------------------------------------------
    def is_visible(self, current_sec: float) -> bool:
        return bool(self.frames) and self.start <= current_sec <= self.end

    def get_alpha(self, current_sec: float) -> int:
        elapsed = current_sec - self.start
        remaining = self.end - current_sec
        if elapsed < FADE_DURATION:
            a = elapsed / FADE_DURATION
        elif remaining < FADE_DURATION:
            a = remaining / FADE_DURATION
        else:
            a = 1.0
        return int(max(0, min(255, a * 255)))

    def draw(self, screen: pygame.Surface, current_sec: float):
        if not self.is_visible(current_sec):
            return

        t = current_sec - self.start
        frame_idx = int(t * ANIM_SHEET_FPS) % len(self.frames)
        frame = self.frames[frame_idx]

        alpha = self.get_alpha(current_sec)
        duration = self.end - self.start
        t_norm = t / duration if duration > 0 else 0.0

        dx_traj, dy_traj = TRAJECTORIES[self.trajectory](t_norm)
        dy_anim = math.sin(t * 1.3 + self.phase) * 10

        x = int(self.base_x + dx_traj)
        y = int(self.base_y + dy_traj + dy_anim)
        y = max(0, min(config.HEIGHT - frame.get_height(), y))

        frame.set_alpha(alpha)
        screen.blit(frame, (x, y))


# ---------------------------------------------------------------------------
# TextSprite — muestra el recorte del texto manuscrito original con trayectoria
# ---------------------------------------------------------------------------

class TextSprite:
    """
    Recorte real de texto manuscrito (RGBA) que se anima con su propia
    trayectoria. Acepta un pygame.Surface pre-construido desde la imagen escaneada.
    """

    def __init__(self, surface: pygame.Surface,
                 start_sec: float, duration_sec: float,
                 position: tuple,
                 trajectory: int | None = None,
                 phase: float | None = None):
        self.start = start_sec
        self.end = start_sec + duration_sec
        self.base_x, self.base_y = float(position[0]), float(position[1])
        self.trajectory = trajectory if trajectory is not None else random.randint(0, len(TRAJECTORIES) - 1)
        self.phase = phase if phase is not None else random.uniform(0, math.pi * 2)
        self._surf = surface

    def is_visible(self, current_sec: float) -> bool:
        return self.start <= current_sec <= self.end

    def get_alpha(self, current_sec: float) -> int:
        elapsed = current_sec - self.start
        remaining = self.end - current_sec
        if elapsed < FADE_DURATION:
            a = elapsed / FADE_DURATION
        elif remaining < FADE_DURATION:
            a = remaining / FADE_DURATION
        else:
            a = 1.0
        return int(max(0, min(255, a * 255)))

    def draw(self, screen: pygame.Surface, current_sec: float):
        if not self.is_visible(current_sec):
            return

        t = current_sec - self.start
        duration = self.end - self.start
        t_norm = t / duration if duration > 0 else 0.0

        dx_traj, dy_traj = TRAJECTORIES[self.trajectory](t_norm)
        dy_anim = math.sin(t * 1.3 + self.phase) * 10

        x = int(self.base_x + dx_traj)
        y = int(self.base_y + dy_traj + dy_anim)
        y = max(0, min(config.HEIGHT - self._surf.get_height(), y))

        self._surf.set_alpha(self.get_alpha(current_sec))
        screen.blit(self._surf, (x, y))
