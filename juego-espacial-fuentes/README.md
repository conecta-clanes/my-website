# 🚀 Juego Espacial

> Shooter espacial controlado por **reconocimiento facial** en tiempo real. Tu rostro es el joystick: muévelo y la nave te sigue. Los disparos son automáticos — solo esquiva y destruye.

---

## Capturas de pantalla

| Menú principal | En partida |
|---|---|
| *(pantalla de bienvenida)* | *(nave siguiendo el rostro del jugador)* |

---

## ¿Cómo funciona?

La webcam captura tu rostro en cada frame mediante **OpenCV Haar Cascades**. La posición normalizada del centro del rostro se mapea al espacio de pantalla (800 × 600 px) y la nave la sigue con **suavizado exponencial (α = 0.12)** — sin saltos bruscos. La nave dispara automáticamente hacia la derecha cada 300 ms; los enemigos viajan de derecha a izquierda con trayectoria sinusoidal.

```
Webcam → Haar Cascade → (x, y) del rostro → Player.set_target() → suavizado → posición en pantalla
```

---

## Características

| Característica | Detalle |
|---|---|
| **Control facial** | OpenCV detecta tu cara; la nave la sigue suavemente (filtro exponencial α = 0.12) |
| **Disparo automático** | Cadencia de 300 ms, sin pulsar nada |
| **3 tipos de enemigos** | Grande, mediano y pequeño — HP, velocidad y puntos distintos |
| **Movimiento sinusoidal** | Cada tipo de enemigo oscila con amplitud y frecuencia propias |
| **Oleadas progresivas** | Cada oleada suma más enemigos de cada tipo |
| **Sistema de vidas** | 3 vidas + 2 s de invulnerabilidad tras recibir daño (parpadeo visual) |
| **Partículas** | Explosiones al destruir enemigos o al perder una vida |
| **HUD** | Puntuación, vidas y número de oleada superpuestos en pantalla |
| **Audio** | Música de fondo WAV + efectos de sonido (disparo, explosión) |
| **Grabación** | Flag `--grabar` guarda el gameplay en MP4 con OpenCV VideoWriter |

---

## Enemigos

| Tipo | HP | Velocidad | Puntos | Radio colisión | Amplitud sinusoidal | Frecuencia |
|---|---|---|---|---|---|---|
| Grande | 3 | 1.0 | 100 | 76 px | 60 px | 0.5 |
| Mediano | 2 | 2.0 | 200 | 52 px | 40 px | 1.0 |
| Pequeño | 1 | 3.5 | 300 | 32 px | 20 px | 2.0 |

### Escalado de oleadas

```
Oleada N:
  grandes  = 2 + (N-1) × 1
  medianos = 3 + (N-1) × 1
  pequeños = 4 + (N-1) × 2
```

---

## Requisitos

- **Python 3.10+**
- **Webcam** funcional (resolución mínima recomendada: 640 × 480)
- **Sistema operativo**: Windows / macOS / Linux

### Dependencias

| Paquete | Versión mínima | Uso |
|---|---|---|
| `pygame` | 2.5.0 | Motor gráfico, audio, gestión de eventos |
| `opencv-contrib-python` | 5.0.0 | Captura de webcam, detección facial (Haar Cascades), grabación |
| `numpy` | 1.24.0 | Procesamiento de frames de la cámara |
| `mediapipe` | 1.0.0 | Disponible para extensiones futuras (landmarks faciales) |

---

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/juego-espacial.git
cd juego-espacial

# 2. (Opcional) Crear un entorno virtual
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## Uso

```bash
# Partida normal
python main.py

# Partida + grabación de video
python main.py --grabar
```

Las grabaciones se guardan automáticamente en:

```
recordings/sesion_YYYYMMDD_HHMMSS.mp4
```

---

## Controles

| Acción | Descripción |
|---|---|
| **Mover el rostro** | Desplaza la nave hacia arriba / abajo (y lateralmente) |
| `ENTER` o `SPACE` | Iniciar partida desde el menú / reiniciar tras Game Over |
| `C` o `ESC` | Abandonar la partida y volver al menú principal |

> La nave dispara sola — solo necesitas moverte para esquivar y apuntar.

---

## Arquitectura del proyecto

```
juego-espacial/
├── main.py               # Punto de entrada: argparse, bucle principal (pygame), gestión de escenas
├── settings.py           # Constantes globales (resolución, FPS, física, datos de enemigos)
├── utils.py              # Helpers: carga de imágenes con canal alfa
│
├── assets/               # Recursos estáticos
│   ├── player-ship-sprite.png
│   ├── enemy-ship-large-sprite.png
│   ├── enemy-ship-medium-sprite.png
│   ├── enemy-ship-small-sprite.png
│   └── music.wav
│
├── entities/             # Objetos del juego
│   ├── player.py         # Nave del jugador: suavizado facial, disparo automático, invulnerabilidad
│   ├── enemy.py          # Enemigos: movimiento sinusoidal de derecha a izquierda
│   └── bullet.py         # Proyectiles: velocidad y tiempo de vida configurables
│
├── scenes/               # Máquina de estados de escenas
│   ├── menu_scene.py     # Pantalla de bienvenida
│   └── game_scene.py     # Loop de juego principal: actualización, render, Game Over
│
├── systems/              # Sistemas desacoplados (inspirado en ECS)
│   ├── spawner.py        # Generación de oleadas de enemigos
│   ├── collision.py      # Detección de colisiones (radio circular)
│   ├── hud.py            # Renderizado del HUD (score, vidas, oleada)
│   ├── particles.py      # Sistema de partículas / explosiones
│   ├── audio.py          # Música de fondo y efectos de sonido
│   └── recorder.py       # Grabación de video con OpenCV VideoWriter
│
└── context/              # Documentación de diseño original
    ├── context.md
    └── theme.md
```

### Flujo de escenas

```
MenuScene ──(ENTER/SPACE)──► GameScene ──(Game Over / ESC / C)──► MenuScene
```

---

## Configuración

Todos los parámetros de juego se ajustan en `settings.py` sin modificar el código del juego:

```python
# Pantalla
WIDTH, HEIGHT = 800, 600
FPS = 60

# Jugador
PLAYER_MAX_SPEED  = 7
PLAYER_FRICTION   = 0.985
SHOOT_COOLDOWN    = 300     # ms entre disparos
PLAYER_LIVES      = 3
INVULNERABLE_TIME = 2000    # ms de invulnerabilidad tras daño
PLAYER_RADIUS     = 44      # radio de colisión

# Balas
BULLET_SPEED    = 14
BULLET_LIFETIME = 1000      # ms antes de desaparecer
BULLET_RADIUS   = 4

# Escalado de oleadas
BASE_WAVE_COUNTS = {'large': 2, 'medium': 3, 'small': 4}
WAVE_INCREMENT   = {'large': 1, 'medium': 1, 'small': 2}
```

---

## Posibles mejoras

- [ ] Integrar **MediaPipe Face Mesh** para control más preciso (landmarks)
- [ ] Añadir jefes (boss) cada 5 oleadas
- [ ] Tabla de puntuaciones persistente (SQLite / JSON)
- [ ] Modo multijugador local (segunda cámara)
- [ ] Power-ups: escudo, disparo triple, velocidad
- [ ] Exportar como ejecutable standalone (PyInstaller)

---

## Licencia

Este proyecto es de uso educativo y personal. Consulta el archivo `LICENSE` si existe.
