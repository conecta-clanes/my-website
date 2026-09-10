import { saveSystem } from '../systems/SaveSystem.js';
import { TOPICS } from '../data/scoutData.js';
import { T, FONT } from '../config/styles.js';
import { ProceduralMusic } from '../systems/ProceduralMusic.js';
import { ProceduralSfx } from '../systems/ProceduralSfx.js';

export class MenuScene extends Phaser.Scene {
  constructor() { super('Menu'); }

  create() {
    const { width: w, height: h } = this.scale;
    this._bg(w, h);
    this._title(w, h);
    this._stats(w, h);
    this._buttons(w, h);
    this.add.text(w - 10, h - 10, 'v1.0 · Manual ASMAC 2019', T.hint(12)).setOrigin(1, 1);
    this._animIn();
    this._initMusic();
  }

  _bg(w, h) {
    this.add.rectangle(0, 0, w, h, 0x0d1b2a).setOrigin(0);
    for (let i = 0; i < 60; i++) {
      const s = this.add.circle(
        Phaser.Math.Between(0, w), Phaser.Math.Between(0, h * 0.75),
        Phaser.Math.FloatBetween(0.5, 2), 0xffffff, Phaser.Math.FloatBetween(0.4, 1)
      );
      this.tweens.add({ targets: s, alpha: 0.1, duration: Phaser.Math.Between(900, 2600), yoyo: true, repeat: -1, delay: Phaser.Math.Between(0, 2000) });
    }
    this.add.rectangle(0, h - 60, w, 60, 0x1a4731).setOrigin(0);
    this.add.ellipse(160, h - 60, 290, 120, 0x1e5c3a);
    this.add.ellipse(w - 190, h - 60, 330, 100, 0x1e5c3a);

    const fire = this.add.container(w / 2, h - 30);
    fire.add([
      this.add.rectangle(-12, 0, 30, 8, 0x5c3d11).setAngle(-30),
      this.add.rectangle(12, 0, 30, 8, 0x5c3d11).setAngle(30),
    ]);
    [0xff4500, 0xff8c00, 0xffff00].forEach((c, i) => {
      const f = this.add.triangle(0, -8 - i * 6, -6 + i * 2, 0, 6 - i * 2, 0, 0, -(16 + i * 8), c, 0.9);
      fire.add(f);
      this.tweens.add({ targets: f, scaleX: { from: 0.8, to: 1.2 }, x: { from: -2, to: 2 }, duration: 300 + i * 100, yoyo: true, repeat: -1, delay: i * 80 });
    });
  }

  _title(w, h) {
    this.cTitle = this.add.container(w / 2, h * 0.22).setAlpha(0);

    // Opaque panel — blocks star field so text is always sharp
    const bg = this.add.graphics();
    bg.fillStyle(0x071828, 0.92);
    bg.fillRoundedRect(-250, -80, 500, 182, 14);
    bg.lineStyle(1, 0x2a4a6a, 0.8);
    bg.strokeRoundedRect(-250, -80, 500, 182, 14);

    const fleur = this.add.text(0, -52, '⚜', { fontFamily: FONT, fontSize: '50px', fill: '#f5c842' }).setOrigin(0.5);
    const title = this.add.text(0, 12, 'SIEMPRE LISTO', { fontFamily: FONT, fontSize: '40px', fill: '#f5c842', fontStyle: '800', shadow: { offsetX: 2, offsetY: 2, color: '#000', blur: 0, fill: true } }).setOrigin(0.5);
    const sub   = this.add.text(0, 56, 'La Aventura Scout', { ...T.body(19), fill: '#ffffff' }).setOrigin(0.5);
    const org   = this.add.text(0, 86, 'Asociación de Scouts de México — ASMAC', {
      fontFamily: FONT, fontSize: '17px', fill: '#ffffff', fontStyle: 'bold',
      shadow: { offsetX: 1, offsetY: 1, color: '#000', blur: 0, fill: true },
    }).setOrigin(0.5);

    this.cTitle.add([bg, fleur, title, sub, org]);
    this.tweens.add({ targets: fleur, angle: { from: -5, to: 5 }, duration: 2000, yoyo: true, repeat: -1, ease: 'Sine.easeInOut' });
  }

  _stats(w, h) {
    this.cStats = this.add.container(w / 2, h * 0.47).setAlpha(0);
    const save = saveSystem.data;
    const pct  = Math.round((save.completedTopics.length / TOPICS.length) * 100);

    const bg = this.add.graphics();
    bg.fillStyle(0x102030, 0.95); bg.fillRoundedRect(-195, -34, 390, 68, 10);
    bg.lineStyle(1, 0x3a6fff, 0.6); bg.strokeRoundedRect(-195, -34, 390, 68, 10);

    const info = this.add.text(0, -12,
      `Temas: ${save.completedTopics.length}/${TOPICS.length}  ·  Puntaje: ${save.totalScore}  ·  Insignias: ${save.badges.length}`,
      T.body(14)
    ).setOrigin(0.5);

    const barBg   = this.add.rectangle(0, 18, 330, 10, 0x0a1520).setOrigin(0.5);
    const barFill = this.add.rectangle(-165, 13, 1, 10, 0x3a6fff).setOrigin(0, 0.5);
    this.tweens.add({ targets: barFill, width: 330 * (pct / 100), duration: 1000, ease: 'Power2', delay: 600 });

    this.cStats.add([bg, info, barBg, barFill]);
  }

  _buttons(w, h) {
    this.cBtns = this.add.container(w / 2, h * 0.58).setAlpha(0);
    [
      { label: '🎮  Jugar',     key: 'play',    bg: 0x1e5c3a, hover: 0x2d8a55 },
      { label: '🏅  Insignias', key: 'badges',  bg: 0x1a3560, hover: 0x2a5299 },
      { label: '⚙  Opciones',  key: 'options', bg: 0x4a2800, hover: 0x7a4200 },
    ].forEach(({ label, key, bg, hover }, i) => {
      this.cBtns.add(this._btn(0, i * 60, label, bg, hover, () => this._go(key)));
    });

    if (save => save.completedTopics.length > 0, saveSystem.data.completedTopics.length > 0) {
      const r = this.add.text(w / 2, h - 26, '↩ Nueva partida', T.muted(13)).setOrigin(0.5).setInteractive({ useHandCursor: true });
      r.on('pointerover', () => r.setStyle({ fill: '#ffffff' }));
      r.on('pointerout',  () => r.setStyle(T.muted(13)));
      r.on('pointerdown', () => this._confirmReset(w, h));
    }
  }

  _btn(x, y, label, bgColor, hoverColor, cb) {
    const btn = this.add.container(x, y);
    const gr  = this.add.graphics();
    const draw = (c) => {
      gr.clear();
      gr.fillStyle(c, 1); gr.fillRoundedRect(-148, -25, 296, 50, 10);
      gr.lineStyle(1, 0xffffff, 0.18); gr.strokeRoundedRect(-148, -25, 296, 50, 10);
    };
    draw(bgColor);
    const txt = this.add.text(0, 0, label, T.header(18)).setOrigin(0.5);
    const hit = this.add.rectangle(0, 0, 296, 50, 0, 0).setInteractive({ useHandCursor: true });
    hit.on('pointerover', () => { draw(hoverColor); this.tweens.add({ targets: btn, scaleX: 1.04, scaleY: 1.04, duration: 100 }); });
    hit.on('pointerout',  () => { draw(bgColor);    this.tweens.add({ targets: btn, scaleX: 1,    scaleY: 1,    duration: 100 }); });
    hit.on('pointerdown', () => { this.game.registry.get('sfx')?.confirm(); cb(); });
    btn.add([gr, txt, hit]);
    return btn;
  }

  _animIn() {
    [this.cTitle, this.cStats, this.cBtns].forEach((c, i) => {
      const y0 = c.y; c.y = y0 + 24;
      this.tweens.add({ targets: c, alpha: 1, y: y0, duration: 480, delay: i * 180, ease: 'Power2' });
    });
  }

  _initMusic() {
    if (this.game.registry.get('music')) return;
    const ctx = this.sound.context;
    if (!ctx) return;

    const launch = () => {
      if (this.game.registry.get('music')) return;
      ctx.resume().then(() => {
        const settings = saveSystem.data.settings ?? {};

        const m = new ProceduralMusic(ctx);
        m.start((settings.musicVolume ?? 0.7) * 0.13);
        this.game.registry.set('music', m);

        const sfx = new ProceduralSfx(ctx);
        sfx.setVolume(settings.sfxVolume ?? 0.7);
        this.game.registry.set('sfx', sfx);
      }).catch(() => {});
    };

    if (ctx.state === 'running') {
      launch();
    } else {
      this.input.once('pointerdown', launch);
      this.input.keyboard.once('keydown', launch);
    }
  }

  _go(key) {
    if (key === 'play') {
      this.cameras.main.fadeOut(350, 0, 0, 0);
      this.cameras.main.once('camerafadeoutcomplete', () => this.scene.start('WorldMap'));
    } else if (key === 'badges') {
      this.scene.launch('Badges'); this.scene.pause();
    } else {
      this.scene.launch('Options'); this.scene.pause();
    }
  }

  _confirmReset(w, h) {
    const ov  = this.add.rectangle(w/2, h/2, w, h, 0x000000, 0.75).setDepth(200);
    const box = this.add.graphics().setDepth(201);
    box.fillStyle(0x0d1b2a,1); box.fillRoundedRect(w/2-195,h/2-95,390,190,14);
    box.lineStyle(2,0xf5c842,1); box.strokeRoundedRect(w/2-195,h/2-95,390,190,14);
    const msg = this.add.text(w/2, h/2-38, '¿Borrar progreso y empezar de nuevo?', { ...T.body(16), wordWrap:{width:350}, align:'center' }).setOrigin(0.5).setDepth(202);
    const yes = this.add.text(w/2-72, h/2+48, 'Sí, borrar', T.danger(16)).setOrigin(0.5).setDepth(202).setInteractive({ useHandCursor:true });
    const no  = this.add.text(w/2+72, h/2+48, 'Cancelar',  T.muted(16)).setOrigin(0.5).setDepth(202).setInteractive({ useHandCursor:true });
    yes.on('pointerover', ()=>yes.setStyle({fill:'#ff4444'}));
    yes.on('pointerout',  ()=>yes.setStyle(T.danger(16)));
    yes.on('pointerdown', ()=>{ saveSystem.reset(); this.scene.restart(); });
    no.on('pointerdown',  ()=>{ [ov,box,msg,yes,no].forEach(o=>o.destroy()); });
  }
}
