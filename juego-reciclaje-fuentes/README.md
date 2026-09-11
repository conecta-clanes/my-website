# Guardianes del Reciclaje

Videojuego educativo de concienciación sobre el manejo de desechos orgánicos e inorgánicos con detección de rostro en tiempo real.

## Descripción

El jugador controla al **Guardián del Reciclaje** con su rostro a través de la cámara web. El guardián sopla (dispara aire) automáticamente hacia arriba para reciclar los desechos que caen desde la parte superior de la pantalla.

- **Desechos orgánicos** (verde, +10 pts): corazón de manzana, cáscara de banana, cáscara de huevo.
- **Desechos inorgánicos** (azul, +15 pts): lata de aluminio, frasco de vidrio, botella plástica.

Si un desecho llega al suelo sin ser reciclado, el jugador pierde una vida. Con 3 vidas agotadas, la partida termina.

## Requisitos

- Python 3.10+
- Cámara web

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
# Modo normal
python main.py

# Modo con grabación de sesión
python main.py --grabar
```

La grabación se guarda en `recordings/sesion_YYYYMMDD_HHMMSS.mp4`.  
La leyenda **REC** parpadea en rojo en la esquina superior derecha durante la grabación.

## Controles

| Acción | Control |
|---|---|
| Mover al guardián | Mueve tu rostro frente a la cámara |
| Soplar / reciclar | Automático (el guardián sopla hacia arriba) |
| Salir / volver al menú | `C` o `ESC` |
| Iniciar partida | `ENTER` o `ESPACIO` |
| Reiniciar (game over) | `ENTER` o `ESPACIO` |

## Estructura del proyecto

```
juego-reciclaje/
├── main.py               # Punto de entrada (--grabar para grabar)
├── settings.py           # Constantes del juego
├── utils.py              # Carga de sprites con transparencia
├── requirements.txt
├── assets/               # Sprites del guardián y desechos
├── entities/
│   ├── player.py         # Guardián (sigue el rostro, sopla automáticamente)
│   ├── air_blast.py      # Proyectil de aire/agua
│   └── waste_item.py     # Desechos reciclables
├── systems/
│   ├── spawner.py        # Generación progresiva de desechos
│   ├── collision.py      # Detección de colisiones aire-desecho
│   ├── hud.py            # Score (arriba izquierda) y vidas (arriba derecha)
│   ├── particles.py      # Efectos visuales de reciclaje y textos flotantes
│   └── recorder.py       # Grabación de sesión en MP4
└── scenes/
    ├── menu_scene.py     # Pantalla de inicio con instrucciones
    └── game_scene.py     # Escena principal del juego
```

## Captura de pantalla

La cámara web se muestra como fondo en tiempo real. El guardián aparece sobre el rostro del jugador y sopla burbujas de aire/agua que al tocar un desecho lo reciclan con un efecto de partículas de color.
