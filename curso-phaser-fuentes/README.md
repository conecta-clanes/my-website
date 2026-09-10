# ⚜ Siempre Listo: La Aventura Scout

Juego educativo interactivo basado en el **Manual de Inducción al Escultismo ASMAC 2019** (Asociación de Scouts de México). Diseñado para que nuevos Scouters y Dirigentes aprendan los fundamentos del Movimiento Scout de forma lúdica.

## Capturas de pantalla

> El juego se ejecuta en el navegador a 800×600 con escala automática.

## Características

- **10 temas educativos** organizados en 3 áreas temáticas
- **Diálogos con NPCs** que introducen cada tema antes del quiz
- **Quizzes de 3 preguntas** con retroalimentación inmediata
- **Sistema de insignias** desbloqueables por progreso
- **Música y efectos procedurales** generados con Web Audio API (sin archivos de audio externos)
- **Guardado automático** en `localStorage` con opción de nueva partida
- **Diseño responsive** que escala a cualquier tamaño de ventana

## Áreas temáticas

| Área | Temas |
|------|-------|
| La Organización | Panorama del Movimiento Scout · Tu Rol en la Estructura Scout |
| Proyecto Educativo | Proyecto Educativo · Método Scout · Manada de Lobatos · Tropa de Scouts · Comunidad de Caminantes · Clan de Rovers |
| Participación del Adulto | El Ciclo de Vida del Adulto · Competencias Scouts |

## Insignias

| Insignia | Requisito |
|----------|-----------|
| 🌱 Primer Paso | Completar 1 tema |
| 🧭 Explorador | Completar 3 temas |
| ⛺ Aventurero | Completar 5 temas |
| ⚜ Guardián Scout | Completar todos los temas |
| 🌟 Puntaje Perfecto | Obtener 30/30 en un quiz |

## Tecnologías

- **[Phaser 3.60](https://phaser.io/)** — motor de juego 2D (cargado desde CDN)
- **JavaScript ES Modules** — sin bundler, sin dependencias de build
- **Web Audio API** — música y SFX procedurales
- **localStorage** — sistema de guardado persistente

## Instalación y ejecución

**Requisito:** Node.js 16 o superior

```bash
# Clonar el repositorio
git clone <url-del-repo>
cd version-phaser

# Iniciar servidor de desarrollo
npx serve . --cors -l 8080
```

Luego abre `http://localhost:8080` en el navegador.

> No se requiere instalación de dependencias adicionales. Phaser se carga desde jsDelivr CDN.

### Script alternativo

```bash
npm start   # equivalente a npx serve . --cors -l 8080
```

## Estructura del proyecto

```
version-phaser/
├── index.html              # Punto de entrada HTML + pantalla de carga
├── package.json
└── src/
    ├── main.js             # Configuración de Phaser y arranque del juego
    ├── config/
    │   └── styles.js       # Estilos de texto y colores globales
    ├── data/
    │   └── scoutData.js    # Contenido educativo (temas, quizzes, insignias)
    ├── scenes/
    │   ├── BootScene.js    # Carga inicial y transición al menú
    │   ├── MenuScene.js    # Pantalla principal con estadísticas
    │   ├── WorldMapScene.js# Mapa de selección de temas
    │   ├── TopicScene.js   # Diálogo con NPC + introducción al tema
    │   ├── QuizScene.js    # Quiz de preguntas con puntuación
    │   ├── BadgesScene.js  # Galería de insignias
    │   └── OptionsScene.js # Configuración de audio y preferencias
    └── systems/
        ├── SaveSystem.js   # Guardado/carga en localStorage
        ├── AudioManager.js # Gestión centralizada de audio
        ├── InputManager.js # Abstracción de entrada (mouse/touch)
        ├── StateMachine.js # Máquina de estados genérica
        ├── DialogSystem.js # Sistema de diálogos con NPC
        ├── ProceduralMusic.js # Música generada proceduralmente
        └── ProceduralSfx.js   # Efectos de sonido procedurales
```

## Flujo del juego

```
BootScene → MenuScene → WorldMapScene → TopicScene → QuizScene → WorldMapScene
                ↕                                        ↕
           BadgesScene                            (desbloqueo de insignias)
           OptionsScene
```

## Datos de guardado

El progreso se guarda automáticamente en `localStorage` bajo la clave `siempre_listo_save`. Incluye:

- Temas completados y puntuaciones por tema
- Puntaje total acumulado
- Insignias desbloqueadas
- Tiempo de juego
- Configuración de audio

Desde el menú principal se puede reiniciar el progreso con "Nueva partida".

## Compatibilidad

Funciona en navegadores modernos con soporte para ES Modules y Web Audio API:

- Chrome / Edge 80+
- Firefox 75+
- Safari 13+

---

*Basado en el Manual de Inducción al Escultismo · Asociación de Scouts de México (ASMAC) 2019 · v1.0*
