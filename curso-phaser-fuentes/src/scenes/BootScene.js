import { saveSystem } from '../systems/SaveSystem.js';

export class BootScene extends Phaser.Scene {
  constructor() { super('Boot'); }

  preload() {
    const bar = document.getElementById('loading-bar');
    const txt = document.getElementById('loading-text');

    this.load.on('progress', (v) => {
      if (bar) bar.style.width = `${Math.round(v * 100)}%`;
      if (txt) txt.textContent = `Cargando... ${Math.round(v * 100)}%`;
    });

    this.load.on('complete', () => {
      const screen = document.getElementById('loading-screen');
      if (screen) screen.style.display = 'none';
    });

    this._generateAssets();
  }

  _generateAssets() {
    const g = this.make.graphics({ x: 0, y: 0, add: false });

    const textures = [
      { key: 'player', color: 0x4a90d9, size: 32, shape: 'circle' },
      { key: 'npc', color: 0xf5c842, size: 32, shape: 'circle' },
      { key: 'ground', color: 0x4a7c59, size: 32, shape: 'rect' },
      { key: 'sky_day', color: 0x87ceeb, size: 1, shape: 'rect' },
      { key: 'sky_night', color: 0x0d1b2a, size: 1, shape: 'rect' },
      { key: 'tree', color: 0x2d6a4f, size: 40, shape: 'triangle' },
      { key: 'badge_locked', color: 0x555555, size: 48, shape: 'hex' },
      { key: 'badge_unlocked', color: 0xf5c842, size: 48, shape: 'hex' },
      { key: 'btn_normal', color: 0x2d6a4f, size: 1, shape: 'rect' },
      { key: 'btn_hover', color: 0x3a8f69, size: 1, shape: 'rect' },
      { key: 'topic_card', color: 0x1e3a5f, size: 1, shape: 'rect' },
    ];

    textures.forEach(({ key, color, size, shape }) => {
      g.clear();
      g.fillStyle(color, 1);
      if (shape === 'circle') {
        g.fillCircle(size / 2, size / 2, size / 2);
        g.generateTexture(key, size, size);
      } else if (shape === 'triangle') {
        g.fillTriangle(size / 2, 0, 0, size, size, size);
        g.generateTexture(key, size, size);
      } else if (shape === 'hex') {
        const cx = size / 2, cy = size / 2, r = size / 2 - 2;
        const pts = Array.from({ length: 6 }, (_, i) => {
          const a = (Math.PI / 3) * i - Math.PI / 6;
          return { x: cx + r * Math.cos(a), y: cy + r * Math.sin(a) };
        });
        g.fillPoints(pts, true);
        g.generateTexture(key, size, size);
      } else {
        g.fillRect(0, 0, size || 200, size || 50);
        g.generateTexture(key, size || 200, size || 50);
      }
    });

    g.destroy();

    this._generatePlayerFrames();
    this._generateParticles();
  }

  _generatePlayerFrames() {
    const g = this.make.graphics({ x: 0, y: 0, add: false });
    const size = 32;

    [0xf5c842, 0xffffff, 0x4a90d9].forEach((color, i) => {
      g.clear();
      g.fillStyle(0x4a90d9, 1);
      g.fillCircle(size / 2, size / 2, size / 2);
      g.fillStyle(color, 1);
      g.fillCircle(size / 2, size / 2, 6);
      g.generateTexture(`player_f${i}`, size, size);
    });

    g.destroy();
  }

  _generateParticles() {
    const g = this.make.graphics({ x: 0, y: 0, add: false });
    g.fillStyle(0xf5c842, 1);
    g.fillCircle(4, 4, 4);
    g.generateTexture('particle_star', 8, 8);
    g.fillStyle(0xffffff, 1);
    g.fillCircle(3, 3, 3);
    g.generateTexture('particle_dot', 6, 6);
    g.destroy();
  }

  create() {
    saveSystem.load();
    // Explicitly request Nunito before creating any text, with 2s safety fallback
    const go = () => this.scene.isActive('Boot') && this.scene.start('Menu');
    Promise.race([
      Promise.all([
        document.fonts.load('700 16px "Nunito"'),
        document.fonts.load('400 16px "Nunito"'),
      ]),
      new Promise(res => setTimeout(res, 2000)),
    ]).then(go).catch(go);
  }
}
