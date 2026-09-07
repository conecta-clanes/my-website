# Archivos de carga inicial — aparecen al arrancar la animación.
# El resto de imágenes en assets/scanned se cargan dinámicamente.

TIMELINE = [
    {"file": "yola.jpg", "start": 1,  "duration": 30, "position": ( 480, 285)},
    {"file": "moni.jpg", "start": 1,  "duration": 30, "position": ( 680, 285)},
]

# Conjunto de nombres usados en la carga inicial (para que HotWatcher los ignore)
INITIAL_FILES: set[str] = {entry["file"] for entry in TIMELINE}
