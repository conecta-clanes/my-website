import numpy as np
import pygame
from PIL import Image
import config

def load_drawing(path: str) -> pygame.Surface:
    """Carga un dibujo escaneado, elimina el fondo blanco y retorna un surface RGBA."""
    img = Image.open(path).convert("RGBA")
    data = np.array(img, dtype=np.uint8)

    r, g, b, a = data [:, :, 0], data [:, :, 1], data [:, :, 2], data [:, :, 3]
    threshold = config.WHITE_THRESHOLD
    white_mask = (r > threshold) & (g > threshold) & (b > threshold)
    data[:, :, 3] = np.where(white_mask, 0, a)

    #recortar al bounding box del cotenido visible
    visible = np.where(data[:, :, 3] > 10)
    if visible[0].size > 0:
        top, bottom = visible[0].min(), visible[0].max()
        left, right = visible[1].min(), visible[1].max()
        data = data[top: bottom + 1, left: right + 1]

    #escalar si es más ancho que el máximo configurado
    h, w = data.shape[:2]
    max_w = config.MAX_DRAWING_WIDTH
    if w > max_w:
        scale = max_w / w
        new_w, new_h = max_w, max(1, int(h * scale))
        pil_cropped = Image.fromarray(data, "RGBA")
        pil_cropped = pil_cropped.resize((new_w, new_h), Image.LANCZOS)
        data = np.array(pil_cropped, dtype=np.uint8)
        h, w = new_h, new_w

    # convertir a pygame Surface
    surface = pygame.image.frombuffer(data.tobytes(), (w,h), "RGBA").convert_alpha()
    return surface



