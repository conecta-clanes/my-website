"""
Extrae estadísticas de color de una imagen escaneada y las aplica a frames de sprites
usando transferencia de color LAB (algoritmo de Reinhard).
Preserva la luminancia del sprite (shading intacto) y solo cambia tono/color.
"""
import cv2
import numpy as np

_SAT_MIN = 25   # saturación mínima (0-255) para considerar que la imagen tiene color


def extract_color_stats(image_path: str) -> tuple[float, float, float, float] | None:
    """
    Extrae estadísticas de color LAB de los píxeles de primer plano.
    Devuelve (mean_a, std_a, mean_b, std_b) o None si la imagen es B&N.
    """
    img_bgr = cv2.imread(image_path)
    if img_bgr is None:
        return None

    # Máscara de primer plano: descarta píxeles casi blancos
    img_f = img_bgr.astype(np.float32) / 255.0
    is_fg = ~np.all(img_f > 0.85, axis=2)
    if not is_fg.any():
        return None

    # Verificar que haya color real (no solo grises/negro)
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    avg_sat = float(hsv[:, :, 1][is_fg].mean())
    if avg_sat < _SAT_MIN:
        print(f"[COLOR] Imagen B&N (sat={avg_sat:.0f}) → sprite sin recoloración")
        return None

    lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB).astype(np.float32)
    a_vals = lab[:, :, 1][is_fg]
    b_vals = lab[:, :, 2][is_fg]

    stats = (
        float(a_vals.mean()), float(max(a_vals.std(), 1.0)),
        float(b_vals.mean()), float(max(b_vals.std(), 1.0)),
    )
    print(f"[COLOR] Stats LAB extraídas: a={stats[0]:.1f}±{stats[1]:.1f}  "
          f"b={stats[2]:.1f}±{stats[3]:.1f}")
    return stats


def apply_color_to_frame(frame_rgba: np.ndarray,
                         lab_stats: tuple[float, float, float, float]) -> np.ndarray:
    """
    Aplica las estadísticas de color LAB a un frame RGBA (numpy uint8).
    Solo modifica los canales de crominancia (a, b); la luminancia L queda intacta.
    """
    src_mean_a, src_std_a, src_mean_b, src_std_b = lab_stats

    alpha = frame_rgba[:, :, 3]
    visible = alpha > 10
    if not visible.any():
        return frame_rgba

    # RGBA → BGR para OpenCV
    bgr = frame_rgba[:, :, [2, 1, 0]].copy()
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB).astype(np.float32)

    # Estadísticas del sprite (solo píxeles visibles)
    a_vis = lab[:, :, 1][visible]
    b_vis = lab[:, :, 2][visible]
    tgt_mean_a = float(a_vis.mean())
    tgt_std_a  = float(max(a_vis.std(), 1.0))
    tgt_mean_b = float(b_vis.mean())
    tgt_std_b  = float(max(b_vis.std(), 1.0))

    # Transferencia Reinhard en canales a y b
    new_lab = lab.copy()
    new_lab[:, :, 1] = np.where(
        visible,
        (lab[:, :, 1] - tgt_mean_a) * (src_std_a / tgt_std_a) + src_mean_a,
        lab[:, :, 1],
    )
    new_lab[:, :, 2] = np.where(
        visible,
        (lab[:, :, 2] - tgt_mean_b) * (src_std_b / tgt_std_b) + src_mean_b,
        lab[:, :, 2],
    )
    new_lab = np.clip(new_lab, 0, 255).astype(np.uint8)
    new_bgr = cv2.cvtColor(new_lab, cv2.COLOR_LAB2BGR)

    result = frame_rgba.copy()
    result[:, :, 0] = new_bgr[:, :, 2]   # R
    result[:, :, 1] = new_bgr[:, :, 1]   # G
    result[:, :, 2] = new_bgr[:, :, 0]   # B
    return result
