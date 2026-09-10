"""One-shot script: rebuilds alpha channels for all 4 sprite PNGs."""
import cv2
import numpy as np
from pathlib import Path

ASSETS = Path("assets")
FILES = [
    "player-ship-sprite.png",
    "enemy-ship-large-sprite.png",
    "enemy-ship-medium-sprite.png",
    "enemy-ship-small-sprite.png",
]

# Background: near-white, near-neutral gray (original canvas)
BG_BRIGHTNESS_MIN = 215   # background is very light
BG_MAX_DIFF       = 22    # background channels are nearly equal (neutral gray)


def remove_bg(bgra: np.ndarray) -> np.ndarray:
    h, w = bgra.shape[:2]
    bgr = bgra[:, :, :3].astype(np.float32)
    b, g, r = bgr[:, :, 0], bgr[:, :, 1], bgr[:, :, 2]

    brightness = (b + g + r) / 3.0
    max_diff = np.maximum(np.abs(r - g), np.maximum(np.abs(r - b), np.abs(g - b)))

    # Candidate background pixels (neutral, bright — matches original canvas)
    candidate_bg = ((max_diff < BG_MAX_DIFF) & (brightness > BG_BRIGHTNESS_MIN)).astype(np.uint8)

    # Flood-fill from all 8 border seeds on the binary candidate mask.
    # This isolates OUTER background; interior holes or dark recesses in the ship stay as ship.
    outer_bg = np.zeros((h, w), dtype=np.uint8)
    seeds = [
        (0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1),
        (0, w // 2), (h - 1, w // 2), (h // 2, 0), (h // 2, w - 1),
    ]
    for row, col in seeds:
        if candidate_bg[row, col] == 0:
            continue                          # not background at this seed
        if outer_bg[row, col]:
            continue                          # already reached
        # BFS on candidate_bg to mark connected region
        stack = [(row, col)]
        while stack:
            cr, cc = stack.pop()
            if cr < 0 or cr >= h or cc < 0 or cc >= w:
                continue
            if outer_bg[cr, cc] or candidate_bg[cr, cc] == 0:
                continue
            outer_bg[cr, cc] = 1
            stack.extend([(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)])

    # Feather the edge for a smooth anti-aliased border
    bg_float = outer_bg.astype(np.float32)
    blurred  = cv2.GaussianBlur(bg_float, (7, 7), 1.5)
    alpha    = np.clip(1.0 - blurred, 0.0, 1.0)
    alpha_u8 = (alpha * 255).astype(np.uint8)

    bgr_u8 = bgra[:, :, :3]
    return np.dstack([bgr_u8, alpha_u8])


for fname in FILES:
    path = ASSETS / fname
    img = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    if img is None:
        print(f"SKIP (not found): {path}")
        continue
    if img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    fixed = remove_bg(img)
    cv2.imwrite(str(path), fixed)

    alpha = fixed[:, :, 3]
    ship_px = int((alpha > 128).sum())
    total   = alpha.size
    print(f"{fname}: {ship_px}/{total} ship pixels ({100*ship_px/total:.1f}%)")

print("Done.")
