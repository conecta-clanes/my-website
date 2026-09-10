import { BADGES } from '../data/scoutData.js';
import { saveSystem } from '../systems/SaveSystem.js';
import { T, FONT } from '../config/styles.js';

export class BadgesScene extends Phaser.Scene {
  constructor() { super('Badges'); }

  create() {
    const { width: W, height: H } = this.scale;
    const earned = saveSystem.data.badges;

    this.add.rectangle(0, 0, W, H, 0x000000, 0.82).setOrigin(0).setDepth(200);

    const box = this.add.graphics().setDepth(201);
    box.fillStyle(0x071828, 1);
    box.fillRoundedRect(46, 32, W - 92, H - 64, 16);
    box.lineStyle(3, 0xf5c842, 1);
    box.strokeRoundedRect(46, 32, W - 92, H - 64, 16);

    this.add.text(W / 2, 62, '🏅  Mis Insignias', T.title(22)).setOrigin(0.5).setDepth(202);
    this.add.text(W / 2, 90, `${earned.length} de ${BADGES.length} obtenidas`, T.muted(13)).setOrigin(0.5).setDepth(202);

    const perRow = 3;
    const colW   = (W - 130) / perRow;
    const rowH   = 138;
    const x0     = 65 + colW / 2;
    const y0     = 134;

    BADGES.forEach((badge, i) => {
      const col = i % perRow, row = Math.floor(i / perRow);
      const x   = x0 + col * colW;
      const y   = y0 + row * rowH;
      const ok  = earned.includes(badge.id);

      const cardBg = this.add.graphics().setDepth(202);
      cardBg.fillStyle(ok ? 0x0e2840 : 0x0a1420, 1);
      cardBg.fillRoundedRect(x - colW/2 + 8, y - 54, colW - 16, 108, 10);
      cardBg.lineStyle(2, ok ? 0xf5c842 : 0x223344, 1);
      cardBg.strokeRoundedRect(x - colW/2 + 8, y - 54, colW - 16, 108, 10);

      this.add.text(x, y - 24, badge.icon, {
        fontFamily: FONT, fontSize: '30px', alpha: ok ? 1 : 0.2,
      }).setOrigin(0.5).setDepth(203);

      this.add.text(x, y + 12, badge.name, {
        ...T.gold(13), fill: ok ? '#f5c842' : '#334455',
      }).setOrigin(0.5).setDepth(203);

      this.add.text(x, y + 32, badge.desc, {
        ...T.muted(ok ? 12 : 11), fill: ok ? '#e8f4ff' : '#2a3a4a',
        wordWrap: { width: colW - 24 }, align: 'center',
      }).setOrigin(0.5).setDepth(203);

      if (!ok) {
        this.add.text(x, y - 24, '🔒', { fontFamily: FONT, fontSize: '26px' }).setOrigin(0.5).setDepth(204);
      }
    });

    const close = this.add.text(W - 58, 50, '✕ Cerrar', T.muted(14))
      .setOrigin(0.5).setDepth(205).setInteractive({ useHandCursor: true });
    close.on('pointerover', () => close.setStyle({ fill: '#ffffff' }));
    close.on('pointerout',  () => close.setStyle(T.muted(14)));
    close.on('pointerdown', () => { this.scene.stop(); this.scene.resume('Menu'); });
  }
}
