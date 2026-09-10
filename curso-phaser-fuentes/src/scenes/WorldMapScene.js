import { TOPICS } from '../data/scoutData.js';
import { saveSystem } from '../systems/SaveSystem.js';
import { T, FONT } from '../config/styles.js';

const COLS = 5;
const CW = 132, CH = 116, GX = 18, GY = 16;

export class WorldMapScene extends Phaser.Scene {
  constructor() { super('WorldMap'); }

  create() {
    const { width: W, height: H } = this.scale;
    this._bg(W, H);
    this._header(W);
    this._grid(W, H);
    this._footer(W, H);
    this._animCards();
  }

  _bg(W, H) {
    this.add.rectangle(0, 0, W, H, 0x0d1b2a).setOrigin(0);
    for (let i = 0; i < 40; i++) {
      this.add.circle(
        Phaser.Math.Between(0, W), Phaser.Math.Between(0, H),
        Phaser.Math.FloatBetween(0.5, 1.5), 0xffffff, Phaser.Math.FloatBetween(0.3, 0.8)
      );
    }
  }

  _header(W) {
    this.add.rectangle(0, 0, W, 60, 0x071018).setOrigin(0);
    this.add.rectangle(0, 59, W, 2, 0xf5c842, 0.3).setOrigin(0);
    this.add.text(W / 2, 20, '⚜  Mapa del Curso de Inducción', T.title(20)).setOrigin(0.5);
    this.add.text(W / 2, 46, 'Selecciona un tema para comenzar', T.muted(13)).setOrigin(0.5);
  }

  _grid(W, H) {
    const totalW = COLS * (CW + GX) - GX;
    const x0 = (W - totalW) / 2 + CW / 2;
    // Header ends at y=61; give 12px breathing room then offset by half card height
    const y0 = 61 + 12 + CH / 2;
    this.cards = TOPICS.map((topic, i) => {
      const col = i % COLS, row = Math.floor(i / COLS);
      return this._card(x0 + col * (CW + GX), y0 + row * (CH + GY), topic);
    });
  }

  _card(x, y, topic) {
    const done = saveSystem.isTopicComplete(topic.id);
    const card = this.add.container(x, y).setAlpha(0);
    const gr   = this.add.graphics();

    const draw = (hover) => {
      gr.clear();
      gr.fillStyle(done ? 0x0e2840 : 0x111e2e, done ? 1 : 0.9);
      gr.fillRoundedRect(-CW/2, -CH/2, CW, CH, 9);
      gr.lineStyle(done ? 2 : 1, done ? 0xf5c842 : hover ? 0x4a88ff : 0x223344, 1);
      gr.strokeRoundedRect(-CW/2, -CH/2, CW, CH, 9);
    };
    draw(false);

    const icon   = this.add.text(0, -CH/2 + 26, topic.icon, { fontFamily: FONT, fontSize: '26px' }).setOrigin(0.5);
    const num    = this.add.text(-CW/2 + 8, -CH/2 + 7, `#${topic.num}`, T.hint(11));
    const title  = this.add.text(0, 8, topic.title, {
      ...T.body(done ? 13 : 12),
      fill: done ? '#f5c842' : '#ffffff',
      fontStyle: done ? 'bold' : 'normal',
      wordWrap: { width: CW - 14 }, align: 'center',
    }).setOrigin(0.5);

    const sc     = saveSystem.data.quizScores[topic.id];
    const status = this.add.text(0, CH/2 - 14,
      done ? `✓ ${sc ?? 0} pts` : `${topic.duration} min`,
      done ? T.success(11) : T.hint(11)
    ).setOrigin(0.5);

    const hit = this.add.rectangle(0, 0, CW, CH, 0, 0).setInteractive({ useHandCursor: true });
    hit.on('pointerover', () => { draw(true);  this.tweens.add({ targets: card, scaleX: 1.06, scaleY: 1.06, duration: 110 }); });
    hit.on('pointerout',  () => { draw(false); this.tweens.add({ targets: card, scaleX: 1,    scaleY: 1,    duration: 110 }); });
    hit.on('pointerdown', () => { this.game.registry.get('sfx')?.click(); this._open(topic); });

    card.add([gr, icon, num, title, status, hit]);
    return card;
  }

  _footer(W, H) {
    const save = saveSystem.data;
    const done = save.completedTopics.length;
    const pct  = Math.round((done / TOPICS.length) * 100);

    this.add.rectangle(0, H - 36, W, 36, 0x071018).setOrigin(0);
    this.add.rectangle(0, H - 36, W, 1, 0x223344).setOrigin(0);

    this.add.text(14, H - 18,
      `Progreso: ${done}/${TOPICS.length}  ·  ${save.totalScore} pts  ·  ${save.badges.length} insignias`,
      T.muted(13)
    ).setOrigin(0, 0.5);

    const bw = 160;
    this.add.rectangle(W/2 - bw/2, H - 22, bw, 8, 0x0a1520).setOrigin(0);
    const fill = this.add.rectangle(W/2 - bw/2, H - 22, 0, 8, 0x3a6fff).setOrigin(0);
    this.tweens.add({ targets: fill, width: bw * (pct / 100), duration: 1200, ease: 'Power2', delay: 400 });

    const back = this.add.text(W - 14, H - 18, '← Menú', T.muted(13)).setOrigin(1, 0.5).setInteractive({ useHandCursor: true });
    back.on('pointerover', () => back.setStyle({ fill: '#ffffff' }));
    back.on('pointerout',  () => back.setStyle(T.muted(13)));
    back.on('pointerdown', () => {
      this.game.registry.get('sfx')?.click();
      this.cameras.main.fadeOut(280, 0, 0, 0);
      this.cameras.main.once('camerafadeoutcomplete', () => this.scene.start('Menu'));
    });
  }

  _animCards() {
    this.cards.forEach((c, i) => this.tweens.add({ targets: c, alpha: 1, duration: 280, delay: i * 55, ease: 'Power1' }));
  }

  _open(topic) {
    this.cameras.main.fadeOut(280, 0, 0, 0);
    this.cameras.main.once('camerafadeoutcomplete', () => this.scene.start('TopicScene', { topic }));
  }
}
