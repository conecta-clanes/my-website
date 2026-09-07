# Requisitos del sistema — Bosque Mágico

Animación generativa en tiempo real que detecta dibujos escaneados iluminados por los niños o jóvenes de hojas tamaño carta iluminadas con crayones y escaneadas con un scanner, los compara contra sprite sheets y los muestra animados sobre un escenario de bosque nocturno.

---

## Requisitos de hardware

| Componente | Mínimo | Recomendado |
|---|---|---|
| CPU | Intel Core i5 / AMD Ryzen 5 (4 núcleos) | i7 / Ryzen 7 o superior |
| RAM | 4 GB | 8 GB |
| Pantalla | 1280 × 720 px | 1920 × 1080 px |
| Almacenamiento | 500 MB libres | 1 GB libres |
| GPU | Integrada (Intel HD / AMD Vega) | Dedicada (para grabación de video) |

> La resolución de pantalla debe ser al menos **1280 × 720** porque el escenario se dibuja exactamente a ese tamaño.

---

## Requisitos de software

### 1. Python 3.10 o superior

El código usa sintaxis de tipos moderna (`str | None`, `tuple[float, float]`) que requiere Python 3.10+.

**Verificar versión instalada:**
```
py --version
```

**Descargar Python:** https://www.python.org/downloads/

Durante la instalación en Windows, marcar **"Add Python to PATH"**.

---

### 2. Bibliotecas Python

Instalar todas de una vez con:

```
py -m pip install -r requirements.txt
```

O una por una:

```
py -m pip install pygame
py -m pip install Pillow
py -m pip install opencv-python
py -m pip install numpy
py -m pip install pymupdf
```

| Biblioteca | Versión mínima | Para qué se usa |
|---|---|---|
| `pygame` | 2.5.0 | Ventana, renderizado, mixer de audio |
| `Pillow` | 10.0.0 | Carga y redimensión de imágenes |
| `opencv-python` | 4.8.0 | Comparación de imágenes, detección de cuadrícula, grabación de video |
| `numpy` | 1.24.0 | Procesamiento de píxeles, síntesis de audio PCM |
| `pymupdf` | 1.23.0 | Conversión de PDFs escaneados a JPG (opcional) |

---

### 3. FFmpeg (solo para grabación de video)

FFmpeg es necesario **únicamente** al usar la opción `--grabar`. En modo previsualización no se requiere.

**Instalar con winget (recomendado):**
```
winget install ffmpeg
```

**Verificar instalación:**
```
ffmpeg -version
```

Después de instalarlo, cerrar y volver a abrir la terminal para que el PATH se actualice.

---

## Estructura de carpetas requerida

```
dibujos-animados/
├── assets/
│   ├── base/           # Imágenes de referencia originales
│   ├── scanned/        # Imágenes a detectar (el programa las carga al iniciar)
│   └── sprite-sheets/  # Sprite sheets PNG + JSON de cuadrícula
├── output/             # Videos generados (se crea automáticamente)
├── main.py
├── config.py
├── sprites.py
├── sprite_matcher.py
├── scene.py
├── colorizer.py
├── drawing_processor.py
├── music.py
└── requirements.txt
```

Los archivos en `assets/scanned/` se detectan automáticamente al iniciar el programa.
Cada sprite sheet `.png` debe tener un archivo `.json` del mismo nombre con la cuadrícula:
```json
{"rows": 5, "cols": 5}
```

---

## Ejecución

```bash
# Previsualización (sin grabar)
py main.py

# Con grabación de video
py main.py --grabar

# Ajustar transparencia del escenario (0 = invisible, 255 = opaco)
py main.py --bg-alpha 180

# Combinado
py main.py --grabar --bg-alpha 200

# Ayuda
py main.py --help
```

Presionar **ESC** o cerrar la ventana para terminar.

---

## Solución de problemas comunes

| Error | Causa | Solución |
|---|---|---|
| `ModuleNotFoundError: No module named 'pygame'` | Biblioteca no instalada | `py -m pip install pygame` |
| `ModuleNotFoundError: No module named 'cv2'` | OpenCV no instalado | `py -m pip install opencv-python` |
| `ModuleNotFoundError: No module named 'fitz'` | PyMuPDF no instalado | `py -m pip install pymupdf` |
| `--grabar requiere FFmpeg` | FFmpeg no en PATH | `winget install ffmpeg` y reiniciar terminal |
| Ventana negra / no abre | Python < 3.10 | Actualizar Python |
| `no se encontró Python` | Python no en PATH | Reinstalar Python marcando "Add to PATH" |
