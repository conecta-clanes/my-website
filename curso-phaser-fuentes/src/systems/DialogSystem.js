import { T, FONT } from '../config/styles.js';

export class DialogSystem {
  constructor(scene) {
    this.scene      = scene;
    this.container  = null;
    this.nameText   = null;
    this.bodyText   = null;
    this.hint       = null;
    this.queue      = [];
    this.active     = false;
    this.onComplete = null;
    this._fullText  = '';
    this._chars     = 0;
    this._timer     = null;
    this._delay     = 28;
  }

  create() {
    const { width: W, height: H } = this.scene.scale;
    const px = 18, py = H - 148, pw = W - 36, ph = 136;

    this.container = this.scene.add.container(0, 0).setDepth(100);

    const bg = this.scene.add.graphics();
    // Fondo muy opaco para garantizar contraste máximo sobre cualquier escena
    bg.fillStyle(0x050d18, 0.97);
    bg.fillRoundedRect(px, py, pw, ph, 12);
    bg.lineStyle(2, 0xf5c842, 0.9);
    bg.strokeRoundedRect(px, py, pw, ph, 12);

    // Nombre del NPC — tamaño 15px con sombra dura, sin stroke
    this.nameText = this.scene.add.text(px + 16, py + 14, '', {
      fontFamily: FONT, fontSize: '15px', fill: '#f5c842', fontStyle: 'bold',
      shadow: { offsetX: 1, offsetY: 1, color: '#000', blur: 0, fill: true },
    });

    // Cuerpo del texto — 15px, color muy claro
    this.bodyText = this.scene.add.text(px + 16, py + 40, '', {
      fontFamily: FONT, fontSize: '15px', fill: '#eaf0ff',
      shadow: { offsetX: 1, offsetY: 1, color: '#000', blur: 0, fill: true },
      wordWrap: { width: pw - 32 }, lineSpacing: 6,
    });

    this.hint = this.scene.add.text(px + pw - 14, py + ph - 12, '▶ ENTER', {
      fontFamily: FONT, fontSize: '12px', fill: '#f5c842',
      shadow: { offsetX: 1, offsetY: 1, color: '#000', blur: 0, fill: true },
    }).setOrigin(1, 1);

    this.scene.tweens.add({ targets: this.hint, alpha: 0.2, duration: 550, yoyo: true, repeat: -1 });

    this.container.add([bg, this.nameText, this.bodyText, this.hint]);
    this.container.setVisible(false);

    this.scene.input.keyboard.on('keydown-SPACE', () => this._advance());
    this.scene.input.keyboard.on('keydown-ENTER', () => this._advance());
    this.scene.input.on('pointerdown', () => this._advance());

    return this;
  }

  show(lines, onComplete) {
    this.queue      = Array.isArray(lines) ? [...lines] : [lines];
    this.onComplete = onComplete;
    this.active     = true;
    this.container.setVisible(true);
    this._next();
  }

  _next() {
    if (!this.queue.length) { this._close(); return; }
    const entry       = this.queue.shift();
    this._fullText    = entry.text ?? entry;
    this.nameText.setText(entry.name ?? '');
    this.bodyText.setText('');
    this._chars = 0;
    this._type();
  }

  _type() {
    if (this._chars >= this._fullText.length) return;
    this._chars++;
    this.bodyText.setText(this._fullText.slice(0, this._chars));
    this._timer = this.scene.time.delayedCall(this._delay, () => this._type());
  }

  _advance() {
    if (!this.active) return;
    const sfx = this.scene.game.registry.get('sfx');
    if (this._chars < this._fullText.length) {
      this._timer?.remove();
      this._chars = this._fullText.length;
      this.bodyText.setText(this._fullText);
    } else {
      sfx?.dialog();
      this._next();
    }
  }

  _close() {
    this.active = false;
    this.container.setVisible(false);
    this.onComplete?.();
  }

  destroy() { this.container?.destroy(); }
}
