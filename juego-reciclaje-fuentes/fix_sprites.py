"""Elimina el fondo de todos los sprites PNG de assets/ y los guarda con transparencia."""
import cv2
import numpy as np
from pathlib import Path

ASSETS = Path("assets")
FILES = [
    "waste-guardian-air-blower.png",
    "waste-guardian-character.png",
    "inorganic-aluminum-can.png",
    "inorganic-glass-jar.png",
    "inorganic-plastic-bottle.png",
    "organic-apple-core.png",
    "organic-banana-peel.png",
    "organic-eggshell.png",
]


def _sample_bg_color(bgra: np.ndarray) -> np.ndarray:
    """Promedia el color de las esquinas y bordes como color de fondo."""
    h, w = bgra.shape[:2]
    samples = []
    step = max(1, min(h, w) // 10)
    for r in range(0, h, step):
        samples.append(bgra[r, 0, :3])
        samples.append(bgra[r, w - 1, :3])
    for c in range(0, w, step):
        samples.append(bgra[0, c, :3])
        samples.append(bgra[h - 1, c, :3])
    return np.median(np.array(samples, dtype=np.float32), axis=0)


def remove_bg(bgra: np.ndarray, tolerance: int = 35) -> np.ndarray:
    h, w = bgra.shape[:2]
    bg = _sample_bg_color(bgra)

    pixels = bgra[:, :, :3].astype(np.float32)
    diff = np.abs(pixels - bg).max(axis=2)
    candidate_bg = (diff < tolerance).astype(np.uint8)

    # BFS flood-fill desde los 8 bordes para aislar solo el fondo EXTERIOR
    outer_bg = np.zeros((h, w), dtype=np.uint8)
    seeds = [
        (0,     0),     (0,     w - 1),
        (h - 1, 0),     (h - 1, w - 1),
        (0,     w // 2),(h - 1, w // 2),
        (h // 2, 0),    (h // 2, w - 1),
    ]
    for row, col in seeds:
        if candidate_bg[row, col] == 0 or outer_bg[row, col]:
            continue
        stack = [(row, col)]
        while stack:
            cr, cc = stack.pop()
            if cr < 0 or cr >= h or cc < 0 or cc >= w:
                continue
            if outer_bg[cr, cc] or candidate_bg[cr, cc] == 0:
                continue
            outer_bg[cr, cc] = 1
            stack.extend([(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)])

    # Suavizado del borde para anti-aliasing
    blurred = cv2.GaussianBlur(outer_bg.astype(np.float32), (7, 7), 1.5)
    alpha   = np.clip(1.0 - blurred, 0.0, 1.0)
    alpha_u8 = (alpha * 255).astype(np.uint8)

    return np.dstack([bgra[:, :, :3], alpha_u8])


for fname in FILES:
    path = ASSETS / fname
    img = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    if img is None:
        print(f"  SKIP (no encontrado): {path}")
        continue

    if img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    fixed     = remove_bg(img)
    cv2.imwrite(str(path), fixed)

    alpha   = fixed[:, :, 3]
    visible = int((alpha > 128).sum())
    total   = alpha.size
    print(f"  {fname}: {visible}/{total} px visibles ({100 * visible / total:.1f}%)")

print("Listo — fondos eliminados.")
