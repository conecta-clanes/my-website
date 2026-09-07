"""
Extrae el texto manuscrito de la parte inferior de la imagen escaneada.
No usa OCR — localiza el texto buscando píxeles de color en la zona baja,
donde el niño siempre escribe su nombre debajo del dibujo.
"""
import os
import re
import numpy as np

_WHITE_THRESHOLD = 215   # píxeles más claros que esto se consideran fondo


def _name_from_filename(image_path: str) -> str:
    base = os.path.splitext(os.path.basename(image_path))[0]
    base = re.sub(r'[_-]p\d+$', '', base, flags=re.IGNORECASE)
    return base.capitalize()


def detect_text_crop(image_path: str) -> tuple[str | None, np.ndarray | None]:
    """
    Localiza el nombre manuscrito en la parte inferior del dibujo
    encontrando el bounding box de píxeles no-blancos en el tercio inferior.

    Devuelve (name_str, rgba_crop):
    - name_str  : nombre del archivo capitalizado (usado como identificador).
    - rgba_crop : array numpy RGBA del recorte del texto con fondo transparente,
                  o None si no se encuentra contenido de color en esa zona.
    """
    try:
        from PIL import Image

        img = Image.open(image_path).convert('RGBA')
        iw, ih = img.size
        arr = np.array(img, dtype=np.uint8)

        name = _name_from_filename(image_path)

        # Buscar en el tercio inferior (75 %–100 % de altura)
        # donde el niño escribe su nombre
        y_start = int(ih * 0.75)
        strip = arr[y_start:, :, :3]          # solo canales RGB

        is_colored = (
            (strip[:, :, 0] < _WHITE_THRESHOLD) |
            (strip[:, :, 1] < _WHITE_THRESHOLD) |
            (strip[:, :, 2] < _WHITE_THRESHOLD)
        )

        if not is_colored.any():
            print(f"[TEXT] {os.path.basename(image_path)}: sin texto en zona inferior")
            return name, None

        rows_idx = np.where(is_colored.any(axis=1))[0]
        cols_idx = np.where(is_colored.any(axis=0))[0]

        pad = 18
        y0 = max(0,  int(rows_idx[0])  - pad) + y_start
        y1 = min(ih, int(rows_idx[-1]) + pad + 1 + y_start)
        x0 = max(0,  int(cols_idx[0])  - pad)
        x1 = min(iw, int(cols_idx[-1]) + pad + 1)

        if x1 <= x0 or y1 <= y0:
            return name, None

        crop = arr[y0:y1, x0:x1].copy()

        # Fondo blanco → transparente
        r, g, b = crop[:, :, 0], crop[:, :, 1], crop[:, :, 2]
        is_white = (r >= _WHITE_THRESHOLD) & (g >= _WHITE_THRESHOLD) & (b >= _WHITE_THRESHOLD)
        crop[:, :, 3] = np.where(is_white, 0, crop[:, :, 3])

        print(f"[TEXT] {os.path.basename(image_path)}: recorte {x1-x0}x{y1-y0} px en y={y0}-{y1}")
        return name, crop

    except Exception as exc:
        print(f"[TEXT] Error en {os.path.basename(image_path)}: {exc}")
        return _name_from_filename(image_path), None
