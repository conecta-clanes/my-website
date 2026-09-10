import { BootScene } from './scenes/BootScene.js';
import { MenuScene } from './scenes/MenuScene.js';
import { WorldMapScene } from './scenes/WorldMapScene.js';
import { TopicScene } from './scenes/TopicScene.js';
import { QuizScene } from './scenes/QuizScene.js';
import { BadgesScene } from './scenes/BadgesScene.js';
import { OptionsScene } from './scenes/OptionsScene.js';

const config = {
  type: Phaser.AUTO,
  width: 800,
  height: 600,
  parent: 'game-container',
  backgroundColor: '#0d1b2a',
  // Renderiza al doble de píxeles en pantallas retina → texto nítido
  resolution: window.devicePixelRatio || 1,
  physics: {
    default: 'arcade',
    arcade: {
      gravity: { y: 600 },
      debug: false,
    },
  },
  scene: [
    BootScene,
    MenuScene,
    WorldMapScene,
    TopicScene,
    QuizScene,
    BadgesScene,
    OptionsScene,
  ],
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH,
    // El juego tiene resolución interna 800×600; Phaser escala el canvas
    // para llenar la ventana manteniendo la relación de aspecto.
    width: 800,
    height: 600,
  },
  render: {
    antialias: true,
    pixelArt: false,
    roundPixels: false,
  },
  audio: {
    disableWebAudio: false,
  },
};

window.addEventListener('load', () => {
  const game = new Phaser.Game(config);

  let lastTime = performance.now();
  game.events.on('step', () => {
    const now = performance.now();
    const dt = (now - lastTime) / 1000;
    lastTime = now;
    const saveData = window.__saveSystem;
    if (saveData) saveData.addPlayTime(dt);
  });

  if (import.meta.env?.DEV) {
    window.__game = game;
  }
});
