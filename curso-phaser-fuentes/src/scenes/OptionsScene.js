import { saveSystem } from '../systems/SaveSystem.js';
import { T, FONT } from '../config/styles.js';

export class OptionsScene extends Phaser.Scene {
  constructor() { super('Options'); }

  create() {
    const { width: W, height: H } = this.scale;
    const settings = saveSystem.data.settings;

    this.add.rectangle(0, 0, W, H, 0x000000, 0.82).setOrigin(0).setDepth(200);

    const box = this.add.graphics().setDepth(201);
    box.fillStyle(0x071828, 1);
    box.fillRoundedRect(W/2-215, H/2-192, 430, 384, 16);
    box.lineStyle(3, 0xf5c842, 1);
    box.strokeRoundedRect(W/2-215, H/2-192, 430, 384, 16);

    this.add.text(W/2, H/2-162, '⚙  Opciones', T.title(21)).setOrigin(0.5).setDepth(202);

    // Separador
    const sep = this.add.graphics().setDepth(202);
    sep.lineStyle(1, 0x223344, 1);
    sep.lineBetween(W/2-180, H/2-132, W/2+180, H/2-132);

    const sliders = [
      { label: 'Volumen de Música',    key: 'musicVolume', y: -90 },
      { label: 'Efectos de Sonido',    key: 'sfxVolume',   y: -30 },
    ];

    sliders.forEach(({ label, key, y }) => {
      this.add.text(W/2-180, H/2+y, label, T.body(15)).setOrigin(0, 0.5).setDepth(202);

      const trackBg   = this.add.rectangle(W/2+55, H/2+y, 150, 8, 0x0a1520).setOrigin(0.5).setDepth(202);
      const trackFill = this.add.rectangle(W/2-20, H/2+y, 150*settings[key], 8, 0x3a6fff).setOrigin(0, 0.5).setDepth(202);
      const handle    = this.add.circle(W/2-20+150*settings[key], H/2+y, 13, 0xf5c842).setDepth(203).setInteractive({ useHandCursor:true, draggable:true });
      const val       = this.add.text(W/2+138, H/2+y, `${Math.round(settings[key]*100)}%`, T.muted(13)).setOrigin(0,0.5).setDepth(203);

      this.input.setDraggable(handle);
      handle.on('drag', (ptr) => {
        const minX = W/2-20, maxX = W/2+130;
        handle.x = Phaser.Math.Clamp(ptr.x, minX, maxX);
        const v = Math.round(((handle.x - minX)/150)*10)/10;
        trackFill.width = 150*v;
        settings[key]   = v;
        val.setText(`${Math.round(v*100)}%`);
        saveSystem.data.settings = settings;
        saveSystem.save();
        if (key === 'musicVolume') {
          const music = this.game.registry.get('music');
          if (music) music.setVolume(v * 0.13);
        }
        if (key === 'sfxVolume') {
          const sfx = this.game.registry.get('sfx');
          if (sfx) { sfx.setVolume(v); sfx.click(); }
        }
      });
    });

    // Separador
    const sep2 = this.add.graphics().setDepth(202);
    sep2.lineStyle(1, 0x223344, 1);
    sep2.lineBetween(W/2-180, H/2+32, W/2+180, H/2+32);

    // Estadísticas
    const save = saveSystem.data;
    [
      `Temas completados: ${save.completedTopics.length} / 10`,
      `Puntaje total: ${save.totalScore} puntos`,
      `Insignias ganadas: ${save.badges.length} / 5`,
    ].forEach((line, i) => {
      this.add.text(W/2, H/2 + 58 + i*26, line, T.muted(14)).setOrigin(0.5).setDepth(202);
    });

    const btn = this.add.text(W/2, H/2+168, '✓  Guardar y cerrar', {
      ...T.header(16), backgroundColor: '#1e5c3a', padding: { x: 22, y: 12 },
    }).setOrigin(0.5).setDepth(205).setInteractive({ useHandCursor: true });
    btn.on('pointerover', () => btn.setBackgroundColor('#2d8a55'));
    btn.on('pointerout',  () => btn.setBackgroundColor('#1e5c3a'));
    btn.on('pointerdown', () => { this.scene.stop(); this.scene.resume('Menu'); });
  }
}
