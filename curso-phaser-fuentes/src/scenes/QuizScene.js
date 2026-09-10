import { saveSystem } from '../systems/SaveSystem.js';
import { BADGES } from '../data/scoutData.js';
import { T, FONT } from '../config/styles.js';

export class QuizScene extends Phaser.Scene {
  constructor() { super('QuizScene'); }

  init(data) {
    this.topic    = data.topic;
    this.questions = [...this.topic.quiz];
    this.current  = 0;
    this.score    = 0;
    this.answered = false;
    this.maxScore = this.questions.reduce((s, q) => s + q.points, 0);
  }

  create() {
    const { width: W, height: H } = this.scale;
    this._bg(W, H);
    this._header(W, H);
    this.qBox = this.add.container(0, 0);
    this._question(W, H);
    this.cameras.main.fadeIn(280);
  }

  _bg(W, H) {
    this.add.rectangle(0, 0, W, H, 0x0d1b2a).setOrigin(0);
    this.add.rectangle(0, 0, W, 66, 0x071018).setOrigin(0);
    this.add.rectangle(0, 65, W, 2, 0x3a6fff, 0.5).setOrigin(0);
  }

  _header(W) {
    this.add.text(W / 2, 20, `⚜  Quiz: ${this.topic.title}`, T.title(17)).setOrigin(0.5);
    this.pText = this.add.text(W / 2, 47, '', T.muted(13)).setOrigin(0.5);
    this.sText = this.add.text(W - 14, 22, 'Puntaje: 0', T.score(15)).setOrigin(1, 0.5);
    this._updateHdr();
  }

  _updateHdr() {
    this.pText.setText(`Pregunta ${this.current + 1} de ${this.questions.length}`);
    this.sText.setText(`Puntaje: ${this.score}`);
  }

  _question(W, H) {
    this.qBox.removeAll(true);
    const q = this.questions[this.current];
    this.answered = false;

    // Fondo de la pregunta — más opaco para mayor contraste
    const bg = this.add.graphics();
    bg.fillStyle(0x0e2040, 1);
    bg.fillRoundedRect(28, 78, W - 56, 100, 10);
    bg.lineStyle(2, 0x3a6fff, 0.7);
    bg.strokeRoundedRect(28, 78, W - 56, 100, 10);

    const qText = this.add.text(W / 2, 128, q.q, {
      ...T.body(16),
      wordWrap: { width: W - 90 }, align: 'center',
    }).setOrigin(0.5);

    const opts = q.options.map((opt, i) => this._option(opt, i, q.answer, q.points, W, H));
    const hint = this.add.text(W / 2, H - 12, 'Toca o haz clic en la respuesta correcta', T.hint(12)).setOrigin(0.5);

    this.qBox.add([bg, qText, hint, ...opts]);
    this.tweens.add({ targets: this.qBox, alpha: { from: 0, to: 1 }, x: { from: 20, to: 0 }, duration: 280, ease: 'Power2' });
  }

  _option(text, idx, correctIdx, points, W, H) {
    const colW = (W - 68) / 2;
    const rowH = 72;
    const col  = idx % 2, row = Math.floor(idx / 2);
    const x    = 34 + col * (colW + 16);
    const y    = 200 + row * rowH;
    const btn  = this.add.container(x, y);

    // Fondos bien diferenciados por opción
    const baseFills = [0x0e2e5c, 0x0e3d24, 0x3d1e08, 0x2e0e3d];
    const gr = this.add.graphics();

    const draw = (state) => {
      gr.clear();
      const fill = state === 'correct' ? 0x0d5c30
        : state === 'wrong'   ? 0x5c0d0d
        : state === 'hover'   ? 0x1a4080
        : baseFills[idx];
      gr.fillStyle(fill, 1);
      gr.fillRoundedRect(0, 0, colW, rowH - 10, 9);
      const border = state === 'correct' ? 0x55ee99
        : state === 'wrong'  ? 0xff7777
        : state === 'hover'  ? 0x88bbff
        : 0x334466;
      gr.lineStyle(state === 'normal' ? 1 : 2, border, 1);
      gr.strokeRoundedRect(0, 0, colW, rowH - 10, 9);
    };
    draw('normal');

    const labels = ['A', 'B', 'C', 'D'];
    const lbl = this.add.text(13, (rowH - 10) / 2, labels[idx], T.gold(18)).setOrigin(0, 0.5);

    // Texto de opción: 14px con Nunito — sin stroke, fondo oscuro garantiza contraste
    const optTxt = this.add.text(40, (rowH - 10) / 2, text, {
      ...T.body(14),
      wordWrap: { width: colW - 52 },
    }).setOrigin(0, 0.5);

    const hit = this.add.rectangle(colW/2, (rowH-10)/2, colW, rowH-10, 0, 0).setInteractive({ useHandCursor: true });
    hit.on('pointerover', () => { if (!this.answered) draw('hover'); });
    hit.on('pointerout',  () => { if (!this.answered) draw('normal'); });
    hit.on('pointerdown', () => {
      if (this.answered) return;
      this.answered = true;
      const correct = idx === correctIdx;
      const sfx = this.game.registry.get('sfx');
      draw(correct ? 'correct' : 'wrong');
      if (correct) {
        this.score += points;
        this.sText.setText(`Puntaje: ${this.score}`);
        this._burst(x + colW / 2, y + (rowH - 10) / 2);
        sfx?.correct();
      } else {
        this.cameras.main.shake(180, 0.006);
        sfx?.wrong();
      }
      const [fbMsg, fbStyle] = correct
        ? ['¡Correcto! ✓', T.success(14)]
        : [`Incorrecto — era: "${this.questions[this.current].options[correctIdx]}"`, T.danger(13)];
      this.qBox.add(this.add.text(W / 2, H - 44, fbMsg, { ...fbStyle, wordWrap: { width: W - 60 }, align: 'center' }).setOrigin(0.5));
      this.time.delayedCall(1900, () => this._next(W, H));
    });

    btn.add([gr, lbl, optTxt, hit]);
    return btn;
  }

  _burst(x, y) {
    for (let i = 0; i < 14; i++) {
      const p = this.add.circle(x, y, Phaser.Math.Between(3, 7), 0xf5c842);
      this.tweens.add({ targets: p, x: x + Phaser.Math.Between(-90, 90), y: y + Phaser.Math.Between(-90, 90), alpha: 0, scale: 0, duration: Phaser.Math.Between(350, 650), ease: 'Power2', onComplete: () => p.destroy() });
    }
  }

  _next(W, H) {
    this.current++;
    this._updateHdr();
    if (this.current < this.questions.length) {
      this.tweens.add({ targets: this.qBox, alpha: 0, x: -24, duration: 190, ease: 'Power1', onComplete: () => this._question(W, H) });
    } else {
      this._results(W, H);
    }
  }

  _results(W, H) {
    const pct = Math.round((this.score / this.maxScore) * 100);
    saveSystem.completeTopicId(this.topic.id, this.score);
    const newBadges = this._checkBadges();
    this.qBox.removeAll(true);

    const ov = this.add.graphics().setDepth(50);
    ov.fillStyle(0x000000, 0.75); ov.fillRect(0, 0, W, H);

    const box = this.add.graphics().setDepth(51);
    box.fillStyle(0x071828, 1);
    box.fillRoundedRect(W/2-230, H/2-215, 460, 430, 16);
    box.lineStyle(3, 0xf5c842, 1);
    box.strokeRoundedRect(W/2-230, H/2-215, 460, 430, 16);

    const emoji = pct >= 80 ? '🌟' : pct >= 50 ? '✅' : '📖';
    const msg   = pct >= 80 ? '¡Excelente trabajo!' : pct >= 50 ? '¡Buen intento!' : 'Sigue estudiando';

    const d = 52;
    this.add.text(W/2, H/2-183, emoji,                      { fontFamily: FONT, fontSize:'44px' }).setOrigin(0.5).setDepth(d);
    this.add.text(W/2, H/2-130, msg,                        T.title(24)).setOrigin(0.5).setDepth(d);
    this.add.text(W/2, H/2-94,  this.topic.title,           T.muted(14)).setOrigin(0.5).setDepth(d);
    this.add.text(W/2, H/2-52,  `${this.score}/${this.maxScore} puntos`, T.score(32)).setOrigin(0.5).setDepth(d);
    this.add.text(W/2, H/2-12,  `${pct}% de aciertos`,     T.body(18)).setOrigin(0.5).setDepth(d);

    if (newBadges.length > 0) {
      this.add.text(W/2, H/2+28, `🏅 ¡Nueva insignia: ${newBadges[0].name}!`, T.gold(15)).setOrigin(0.5).setDepth(d);
    }

    const cont = this.add.text(W/2, H/2+120, '→  Volver al Mapa', {
      ...T.header(17), backgroundColor: '#1e5c3a', padding: { x: 24, y: 12 },
    }).setOrigin(0.5).setDepth(d).setInteractive({ useHandCursor: true });
    cont.on('pointerover', () => cont.setBackgroundColor('#2d8a55'));
    cont.on('pointerout',  () => cont.setBackgroundColor('#1e5c3a'));
    cont.on('pointerdown', () => {
      this.cameras.main.fadeOut(280, 0, 0, 0);
      this.cameras.main.once('camerafadeoutcomplete', () => this.scene.start('WorldMap'));
    });

    const retry = this.add.text(W/2, H/2+168, '↩  Repetir quiz', T.muted(14)).setOrigin(0.5).setDepth(d).setInteractive({ useHandCursor: true });
    retry.on('pointerover', () => retry.setStyle({ fill: '#ffffff' }));
    retry.on('pointerout',  () => retry.setStyle(T.muted(14)));
    retry.on('pointerdown', () => this.scene.restart({ topic: this.topic }));
  }

  _checkBadges() {
    const done = saveSystem.data.completedTopics.length;
    const newBadges = [];
    BADGES.forEach(b => {
      if (b.requirement > 0 && done >= b.requirement && saveSystem.awardBadge(b.id)) newBadges.push(b);
      if (b.id === 'perfecto' && this.score >= this.maxScore && saveSystem.awardBadge(b.id)) newBadges.push(b);
    });
    return newBadges;
  }
}
