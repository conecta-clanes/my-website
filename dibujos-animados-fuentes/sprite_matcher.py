"""
Compara una imagen escaneada contra los sprite sheets disponibles
y devuelve el que más se parece.
Estrategia: primero matching por nombre (difflib), luego visual como respaldo.
"""
import os
import re
import json
from difflib import SequenceMatcher

import cv2
import numpy as np

_BASE_DIR    = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "base")
_SPRITES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "sprite-sheets")
_SHEET_EXTS = {'.png', '.jpg', '.jpeg', '.bmp', '.webp'}
_MIN_VISUAL_SCORE = 0.3   # threshold para matching visual contra sprite sheets
_MIN_NCC_SCORE    = 0.10  # threshold HOG-cosine (scores 0.10-0.33 para matches reales)
_MIN_NCC_MARGIN   = 0.005 # el mejor debe superar al 2do por al menos este valor
_MIN_NAME_SCORE   = 0.5   # similitud mínima de nombre — nombres de personas dan ≤0.40, animales ≥0.97


# ---------------------------------------------------------------------------
# Listado
# ---------------------------------------------------------------------------

def list_sheets() -> list[str]:
    if not os.path.isdir(_SPRITES_DIR):
        return []
    return [
        os.path.join(_SPRITES_DIR, f)
        for f in sorted(os.listdir(_SPRITES_DIR))
        if os.path.splitext(f)[1].lower() in _SHEET_EXTS
    ]


def _list_base_images() -> list[str]:
    if not os.path.isdir(_BASE_DIR):
        return []
    return [
        os.path.join(_BASE_DIR, f)
        for f in sorted(os.listdir(_BASE_DIR))
        if os.path.splitext(f)[1].lower() in _SHEET_EXTS
    ]


# ---------------------------------------------------------------------------
# Metadatos de cuadrícula
# ---------------------------------------------------------------------------

def load_sheet_metadata(sheet_path: str, img_bgr: np.ndarray | None = None) -> tuple[int, int]:
    """Devuelve (filas, columnas) desde sidecar JSON, auto-detección, o (5, 5)."""
    base = os.path.splitext(sheet_path)[0]
    json_path = base + '.json'
    if os.path.isfile(json_path):
        try:
            with open(json_path, encoding='utf-8') as f:
                data = json.load(f)
            rows, cols = int(data.get('rows', 5)), int(data.get('cols', 5))
            print(f"[GRID] {os.path.basename(sheet_path)}: {rows}x{cols} (JSON)")
            return rows, cols
        except Exception as exc:
            print(f"[GRID] Error leyendo JSON {json_path}: {exc}")

    if img_bgr is None:
        img_bgr = cv2.imread(sheet_path)
    if img_bgr is None:
        return 5, 5

    rows, cols = _detect_grid(img_bgr)
    print(f"[GRID] {os.path.basename(sheet_path)}: {rows}x{cols} (auto-detectado)")
    return rows, cols


def _detect_grid(img: np.ndarray) -> tuple[int, int]:
    """Detecta la cuadrícula buscando líneas separadoras de fondo blanco."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, bg_mask = cv2.threshold(gray, 240, 1, cv2.THRESH_BINARY)

    row_bg = bg_mask.mean(axis=1)
    col_bg = bg_mask.mean(axis=0)

    def count_content_strips(arr, threshold=0.95) -> int:
        count = 0
        in_content = False
        for v in arr:
            is_content = bool(v < threshold)
            if is_content and not in_content:
                count += 1
            in_content = is_content
        return max(1, count)

    rows = count_content_strips(row_bg)
    cols = count_content_strips(col_bg)

    if 2 <= rows <= 20 and 2 <= cols <= 20:
        return rows, cols
    return 5, 5


# ---------------------------------------------------------------------------
# Matching por nombre
# ---------------------------------------------------------------------------

def _normalize_name(filename: str) -> str:
    """
    Quita extensión y sufijos de animación, extrae tokens CamelCase,
    los ordena y los une. Así 'aguilaLeon' y 'leonAguila' son idénticos.
    """
    name = os.path.splitext(filename)[0]
    name = re.sub(r'[-_](walk|run|idle|stand|v\d+).*$', '', name, flags=re.IGNORECASE)
    # separar por CamelCase y guiones/subrayados
    tokens = re.findall(r'[A-Za-z][a-z]*', name)
    tokens = [t.lower() for t in tokens if len(t) >= 3]
    return ''.join(sorted(tokens))


def _name_similarity(scanned_file: str, sheet_file: str) -> float:
    a = _normalize_name(scanned_file)
    b = _normalize_name(sheet_file)
    return SequenceMatcher(None, a, b).ratio()


def _find_best_by_name(scanned_path: str, sheets: list[str]) -> tuple[str | None, int, int]:
    """Busca el sheet con mayor similitud de nombre. Devuelve None si ninguno supera _MIN_NAME_SCORE."""
    scanned_file = os.path.basename(scanned_path)
    best_path: str | None = None
    best_score = 0.0
    best_rows, best_cols = 5, 5

    for sheet_path in sheets:
        sheet_file = os.path.basename(sheet_path)
        s = _name_similarity(scanned_file, sheet_file)
        print(f"[NAME]  {sheet_file}: similitud={s:.2f}")
        if s > best_score:
            best_score = s
            best_path = sheet_path

    if best_path and best_score >= _MIN_NAME_SCORE:
        best_rows, best_cols = load_sheet_metadata(best_path)
        print(f"[NAME] OK {os.path.basename(best_path)} (similitud={best_score:.2f})")
        return best_path, best_rows, best_cols

    print(f"[NAME] Sin match por nombre (mejor={best_score:.2f})")
    return None, 0, 0


# ---------------------------------------------------------------------------
# HOG cosine similarity — robusto a rellenos de color de crayón
# ---------------------------------------------------------------------------

def _hog_feature(img_bgr: np.ndarray, size: tuple[int, int] = (256, 256)) -> np.ndarray:
    """
    Histograma de Gradientes Orientados (HOG) simplificado.
    Captura la DIRECCIÓN de los bordes en celdas de 16×16 px con 9 bins de ángulo.
    Al depender de orientaciones y no de intensidades, es invariante al color
    y discrimina plantillas con formas distintas incluso cuando están coloreadas.
    """
    gray = cv2.resize(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY), size).astype(np.float32)
    gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
    mag = np.sqrt(gx ** 2 + gy ** 2)
    ang = (np.arctan2(gy, gx) * 180.0 / np.pi) % 180.0  # [0, 180) sin signo
    cell = 16
    feat: list[float] = []
    for r in range(size[1] // cell):
        for c in range(size[0] // cell):
            m = mag[r * cell:(r + 1) * cell, c * cell:(c + 1) * cell]
            a = ang[r * cell:(r + 1) * cell, c * cell:(c + 1) * cell]
            hist, _ = np.histogram(a.flatten(), bins=9, range=(0, 180),
                                   weights=m.flatten())
            feat.extend(hist.tolist())
    v = np.array(feat, dtype=np.float32)
    v -= v.mean()
    n = np.linalg.norm(v)
    return v / n if n > 1e-8 else v


def _ncc_score(a_bgr: np.ndarray, b_bgr: np.ndarray,
               size: tuple[int, int] = (256, 256)) -> float:
    """
    Similitud coseno entre descriptores HOG.
    Scores típicos: ~0.15-0.33 para el template correcto, ~0.07-0.19 para los otros.
    Robusto cuando el scan está coloreado con crayones y la referencia es B&N.
    """
    return float(np.dot(_hog_feature(a_bgr, size), _hog_feature(b_bgr, size)))


# ---------------------------------------------------------------------------
# Matching visual (respaldo)
# ---------------------------------------------------------------------------

def _to_edges(img_bgr: np.ndarray, size: tuple[int, int] = (128, 128)) -> np.ndarray:
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 30, 120)
    return cv2.resize(edges, size, interpolation=cv2.INTER_AREA)


def _histogram_correlation(a: np.ndarray, b: np.ndarray) -> float:
    ha = cv2.calcHist([a], [0], None, [64], [0, 256])
    hb = cv2.calcHist([b], [0], None, [64], [0, 256])
    cv2.normalize(ha, ha)
    cv2.normalize(hb, hb)
    return float(cv2.compareHist(ha, hb, cv2.HISTCMP_CORREL))


def _hu_similarity(a: np.ndarray, b: np.ndarray) -> float:
    gray_a = a if a.ndim == 2 else cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    gray_b = b if b.ndim == 2 else cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    ma = cv2.moments(gray_a)
    mb = cv2.moments(gray_b)
    hu_a = cv2.HuMoments(ma).flatten()
    hu_b = cv2.HuMoments(mb).flatten()
    eps = 1e-10
    hu_a = -np.sign(hu_a) * np.log10(np.abs(hu_a) + eps)
    hu_b = -np.sign(hu_b) * np.log10(np.abs(hu_b) + eps)
    dist = float(np.sqrt(np.sum((hu_a - hu_b) ** 2)))
    return 1.0 / (1.0 + dist)


def _visual_score(scanned_bgr: np.ndarray, frame_bgr: np.ndarray) -> float:
    sc_edges = _to_edges(scanned_bgr)
    fr_edges = _to_edges(frame_bgr)
    corr = _histogram_correlation(sc_edges, fr_edges)
    hu = _hu_similarity(sc_edges, fr_edges)
    return 0.6 * corr + 0.4 * hu


def _find_best_by_visual(scanned_path: str, sheets: list[str]) -> tuple[str | None, int, int]:
    scanned_bgr = cv2.imread(scanned_path)
    if scanned_bgr is None:
        print(f"[VISUAL] No se pudo leer: {scanned_path}")
        return None, 0, 0

    best_path: str | None = None
    best_rows, best_cols = 5, 5
    best_score = -999.0

    for sheet_path in sheets:
        img = cv2.imread(sheet_path)
        if img is None:
            continue
        rows, cols = load_sheet_metadata(sheet_path, img)
        h, w = img.shape[:2]
        fh, fw = h // rows, w // cols
        first_frame = img[0:fh, 0:fw]

        s = _visual_score(scanned_bgr, first_frame)
        print(f"[VISUAL] {os.path.basename(sheet_path)} [{rows}x{cols}]: score={s:.3f}")

        if s > best_score:
            best_score = s
            best_path = sheet_path
            best_rows, best_cols = rows, cols

    if best_path and best_score >= _MIN_VISUAL_SCORE:
        print(f"[VISUAL] OK {os.path.basename(best_path)} (score={best_score:.3f})")
        return best_path, best_rows, best_cols

    print(f"[VISUAL] Sin coincidencia suficiente (mejor={best_score:.3f})")
    return None, 0, 0


# ---------------------------------------------------------------------------
# Matching por imagen de referencia (assets/base/)
# ---------------------------------------------------------------------------

def _find_best_by_base_image(scanned_path: str, sheets: list[str]) -> tuple[str | None, int, int]:
    """
    Compara la imagen escaneada contra las imágenes de referencia en assets/base/ usando NCC.
    NCC es muy discriminativa para dibujos de línea: self=1.0, cross≈0.02-0.07.
    Si hay match (NCC > _MIN_NCC_SCORE), usa el nombre base para buscar el sprite sheet.
    """
    scanned_bgr = cv2.imread(scanned_path)
    if scanned_bgr is None:
        return None, 0, 0

    base_images = _list_base_images()
    if not base_images:
        return None, 0, 0

    best_base: str | None = None
    best_score = -1.0
    second_score = -1.0

    for base_path in base_images:
        ref = cv2.imread(base_path)
        if ref is None:
            continue
        s = _ncc_score(scanned_bgr, ref)
        print(f"[BASE]  {os.path.basename(base_path)}: ncc={s:.4f}")
        if s > best_score:
            second_score = best_score
            best_score = s
            best_base = base_path
        elif s > second_score:
            second_score = s

    margin = best_score - max(second_score, 0.0)
    if best_base is None or best_score < _MIN_NCC_SCORE or margin < _MIN_NCC_MARGIN:
        print(f"[BASE] Sin match claro (mejor={best_score:.4f}, margen={margin:.4f})")
        return None, 0, 0

    print(f"[BASE] OK {os.path.basename(best_base)} (ncc={best_score:.4f}, margen={margin:.4f})")

    # Usar el nombre de la imagen base para encontrar el sprite sheet del mismo personaje
    path, rows, cols = _find_best_by_name(best_base, sheets)
    if path:
        return path, rows, cols

    print(f"[BASE] No hay sprite sheet para '{os.path.basename(best_base)}'")
    return None, 0, 0


# ---------------------------------------------------------------------------
# API pública
# ---------------------------------------------------------------------------

def _find_by_sidecar(scanned_path: str, sheets: list[str]) -> tuple[str | None, int, int]:
    """
    Lee un JSON sidecar junto al archivo escaneado para forzar un sprite sheet concreto.
    Formato: {"sheet": "aguilaAramadillo-walk-v1.png"}
    El nombre puede incluir o no la extensión; la búsqueda es case-insensitive.
    """
    sidecar = os.path.splitext(scanned_path)[0] + '.json'
    if not os.path.isfile(sidecar):
        return None, 0, 0
    try:
        with open(sidecar, encoding='utf-8') as f:
            data = json.load(f)
        sheet_name = str(data.get('sheet', '')).strip()
        if not sheet_name:
            return None, 0, 0
        # Buscar el sheet que termine con el nombre indicado (con o sin extensión)
        if not os.path.splitext(sheet_name)[1]:
            sheet_name += '.png'
        for sheet_path in sheets:
            if os.path.basename(sheet_path).lower() == sheet_name.lower():
                rows, cols = load_sheet_metadata(sheet_path)
                print(f"[SIDECAR] {os.path.basename(scanned_path)} -> {os.path.basename(sheet_path)} ({rows}x{cols})")
                return sheet_path, rows, cols
        print(f"[SIDECAR] Sheet '{sheet_name}' no encontrado en sprite-sheets/")
    except Exception as exc:
        print(f"[SIDECAR] Error leyendo {sidecar}: {exc}")
    return None, 0, 0


def find_best_sheet(scanned_path: str) -> tuple[str | None, int, int]:
    """
    Pipeline de 4 pasos:
    0. Sidecar: JSON junto al scan que fuerza un sprite sheet concreto.
    1. Nombre: compara nombre del archivo escaneado contra sprite sheets.
    2. Base:   compara visualmente contra assets/base/ (dibujos de referencia del mismo estilo).
    3. Visual: último recurso — compara contra primer frame de cada sprite sheet.
    Devuelve (ruta_sheet, filas, columnas) o (None, 0, 0).
    """
    sheets = list_sheets()
    if not sheets:
        print("[MATCH] No hay sprite sheets en assets/sprite-sheets/")
        return None, 0, 0

    # 0. Sidecar JSON — override explícito del operador
    path, rows, cols = _find_by_sidecar(scanned_path, sheets)
    if path:
        return path, rows, cols

    # 1. Matching por nombre
    path, rows, cols = _find_best_by_name(scanned_path, sheets)
    if path:
        return path, rows, cols

    # 2. Matching visual contra imágenes de referencia en assets/base/
    path, rows, cols = _find_best_by_base_image(scanned_path, sheets)
    if path:
        return path, rows, cols

    # 3. Matching visual contra primer frame de sprite sheets (último recurso)
    return _find_best_by_visual(scanned_path, sheets)
