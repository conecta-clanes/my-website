import { DialogSystem } from '../systems/DialogSystem.js';
import { StateMachine } from '../systems/StateMachine.js';
import { InputManager } from '../systems/InputManager.js';
import { saveSystem } from '../systems/SaveSystem.js';
import { T, FONT } from '../config/styles.js';

export class TopicScene extends Phaser.Scene {
  constructor() { super('TopicScene'); }

  init(data) {
    this.topic = data.topic;
    this.npcTalked = false;
  }

  create() {
    const { width: W, height: H } = this.scale;

    this._buildWorld(W, H);
    this._buildPlayer(W, H);
    this._buildNPC(W, H);
    this._setupColliders();
    this._buildUI(W, H);

    this.dialog = new DialogSystem(this).create();
    this.inputMgr = new InputManager(this);

    this.cameras.main.fadeIn(400);
    this.time.delayedCall(500, () => this._showIntroDialog());
  }

  _buildWorld(W, H) {
    // Dark background — no Phaser.Display.Color so no risk of crash
    this.add.rectangle(0, 0, W, H, 0x0d1b2a).setOrigin(0);

    // Accent strip at top using topic color directly
    const accentColor = this.topic.color ?? 0x1e3a5f;
    this.add.rectangle(0, 0, W, 6, accentColor).setOrigin(0);

    // Stars
    for (let i = 0; i < 35; i++) {
      const x = Phaser.Math.Between(0, W);
      const y = Phaser.Math.Between(60, Math.floor(H * 0.55));
      const r = Phaser.Math.FloatBetween(0.5, 2);
      const star = this.add.circle(x, y, r, 0xffffff, Phaser.Math.FloatBetween(0.2, 0.8));
      this.tweens.add({
        targets: star, alpha: 0.1,
        duration: Phaser.Math.Between(1000, 3000),
        yoyo: true, repeat: -1,
        delay: Phaser.Math.Between(0, 2000),
      });
    }

    // Barra de título — fondo opaco para texto siempre legible
    this.add.rectangle(0, 0, W, 52, 0x050d18, 1).setOrigin(0);
    this.add.rectangle(0, 51, W, 2, 0xf5c842, 0.3).setOrigin(0);
    this.add.text(W / 2, 26, `Tema ${this.topic.num}: ${this.topic.title}`, T.title(15)).setOrigin(0.5);

    // Ground visual
    this.add.rectangle(0, H - 60, W, 60, 0x1a4731).setOrigin(0);
    // Grass strip
    this.add.rectangle(0, H - 60, W, 6, 0x2ecc71).setOrigin(0);

    // Decorative trees
    this._addTree(60, H - 60);
    this._addTree(W - 60, H - 60);
    this._addTree(W / 2 - 200, H - 60);

    // Floating platforms (visual only — physics bodies added in _setupColliders)
    this.platVisuals = [
      this.add.rectangle(160, H - 155, 120, 14, 0x2d6a4f),
      this.add.rectangle(W - 160, H - 155, 120, 14, 0x2d6a4f),
      this.add.rectangle(W / 2, H - 220, 150, 14, 0x2d6a4f),
    ];
    this.platVisuals.forEach(p => {
      this.add.rectangle(p.x, p.y - 1, p.width, 3, 0x3a8f69).setOrigin(0.5);
    });

    // Ground physics body (static)
    this.groundBody = this.add.rectangle(W / 2, H - 30, W, 60, 0x000000, 0);
    this.physics.add.existing(this.groundBody, true);

    // Platform physics bodies
    this.platBodies = this.platVisuals.map(pv => {
      const body = this.add.rectangle(pv.x, pv.y, pv.width, pv.height, 0x000000, 0);
      this.physics.add.existing(body, true);
      return body;
    });

    this.add.rectangle(0, H - 60, W, 22, 0x000000, 0.6).setOrigin(0);
    this.add.text(W / 2, H - 49, `Objetivo: ${this.topic.objective}`, {
      fontFamily: FONT, fontSize: '13px', fill: '#ffffff',
      wordWrap: { width: W - 180 }, align: 'center',
      shadow: { offsetX: 1, offsetY: 1, color: '#000', blur: 0, fill: true },
    }).setOrigin(0.5);
  }

  _addTree(x, groundY) {
    const trunk = this.add.rectangle(x, groundY - 18, 10, 36, 0x5c3d11).setOrigin(0.5, 1);
    const leaves = this.add.triangle(
      x, groundY - 54,
      x - 22, groundY - 18,
      x + 22, groundY - 18,
      0, groundY - 60,
      0x2d6a4f
    );
  }

  _buildPlayer(W, H) {
    this.player = this.physics.add.sprite(120, H - 130, 'player').setScale(1.3);
    this.player.setCollideWorldBounds(true);
    this.player.setMaxVelocity(300, 800);

    // Player state machine
    this.playerFsm = new StateMachine(this, 'player');
    const scene = this;

    this.playerFsm
      .addState('idle', {
        onEnter() {
          scene.player.setVelocityX(0);
        },
      })
      .addState('walk', {})
      .addState('jump', {
        onEnter() {
          scene.player.setVelocityY(-400);
        },
        onUpdate() {
          if (scene.player.body?.onFloor()) scene.playerFsm.setState('idle');
        },
      })
      .addState('talk', {
        onEnter() { scene.player.setVelocityX(0); },
      })
      .setState('idle');
  }

  _buildNPC(W, H) {
    this.npc = this.physics.add.sprite(W - 130, H - 120, 'npc').setScale(1.3);
    this.npc.setCollideWorldBounds(true);
    this.npc.setImmovable(true);

    // Nombre del NPC — fondo opaco, sin stroke
    this.add.text(W - 130, H - 175, this.topic.npcName, {
      ...T.gold(13), backgroundColor: '#050d18cc', padding: { x: 6, y: 3 },
    }).setOrigin(0.5);

    // Chat bubble
    this.chatBubble = this.add.text(W - 130, H - 196, '💬', { fontSize: '18px' }).setOrigin(0.5);
    this.tweens.add({
      targets: this.chatBubble, y: H - 204,
      duration: 700, yoyo: true, repeat: -1, ease: 'Sine.easeInOut',
    });

    // Topic icon near NPC
    this.add.text(W - 130, H - 220, this.topic.icon, { fontSize: '22px' }).setOrigin(0.5);

    // Interaction range indicator (invisible zone)
    this.npcZone = this.add.zone(W - 130, H - 120, 110, 100).setOrigin(0.5);
    this.physics.world.enable(this.npcZone);
    this.npcZone.body.setAllowGravity(false);
  }

  _setupColliders() {
    // Player ↔ ground
    this.physics.add.collider(this.player, this.groundBody);
    // Player ↔ platforms
    this.platBodies.forEach(pb => this.physics.add.collider(this.player, pb));
    // NPC ↔ ground
    this.physics.add.collider(this.npc, this.groundBody);
    // Player overlaps NPC zone → trigger dialog
    this.physics.add.overlap(this.player, this.npcZone, () => {
      if (!this.npcTalked && !this.dialog?.active) {
        this.npcTalked = true;
        this.playerFsm.setState('talk');
        this.dialog.show(this.topic.npcDialog, () => {
          this.playerFsm.setState('idle');
          this.time.delayedCall(400, () => this._startQuiz());
        });
      }
    });
  }

  _buildUI(W, H) {
    // Barra inferior con fondo sólido — garantiza legibilidad siempre
    this.add.rectangle(0, H - 58, W, 58, 0x050d18, 1).setOrigin(0).setDepth(19);
    this.add.rectangle(0, H - 58, W, 1, 0x223344).setOrigin(0).setDepth(19);

    // Objetivo del tema
    this.add.text(W / 2, H - 42, `Objetivo: ${this.topic.objective}`, {
      ...T.muted(13), wordWrap: { width: W - 200 }, align: 'center',
    }).setOrigin(0.5).setDepth(20);

    // Controles
    this.add.text(W / 2, H - 14, '← → Moverse  ·  ↑/W Saltar  ·  Acércate al NPC para hablar', T.hint(12)).setOrigin(0.5).setDepth(20);

    // Botón volver
    const back = this.add.text(10, H - 28, '← Mapa', T.muted(13)).setOrigin(0, 0.5).setDepth(20).setInteractive({ useHandCursor: true });
    back.on('pointerover', () => back.setStyle({ fill: '#ffffff' }));
    back.on('pointerout',  () => back.setStyle(T.muted(13)));
    back.on('pointerdown', () => {
      this.game.registry.get('sfx')?.click();
      this.cameras.main.fadeOut(300, 0, 0, 0);
      this.cameras.main.once('camerafadeoutcomplete', () => this.scene.start('WorldMap'));
    });

    // Badge de completado
    if (saveSystem.isTopicComplete(this.topic.id)) {
      this.add.text(W - 10, H - 28,
        `✓ ${saveSystem.data.quizScores[this.topic.id] ?? 0} pts`,
        T.success(13)
      ).setOrigin(1, 0.5).setDepth(20);
    }
  }

  _showIntroDialog() {
    if (this.dialog?.active) return;
    this.dialog.show([
      { name: 'Sistema', text: `¡Bienvenido al tema: "${this.topic.title}"!` },
      { name: 'Sistema', text: `Muévete hacia ${this.topic.npcName} con las teclas ← → y habla con él/ella para aprender. Luego responderás un quiz.` },
    ], () => {});
  }

  _startQuiz() {
    this.cameras.main.fadeOut(300, 0, 0, 0);
    this.cameras.main.once('camerafadeoutcomplete', () => {
      this.scene.start('QuizScene', { topic: this.topic });
    });
  }

  update() {
    if (!this.player || !this.inputMgr) return;

    const onFloor = this.player.body?.onFloor() ?? false;
    const inDialog = this.dialog?.active ?? false;

    if (!inDialog && !this.playerFsm.is('talk')) {
      const axis = this.inputMgr.getAxis();
      const vx = axis.x * 180;

      this.player.setVelocityX(vx);

      if (Math.abs(vx) > 10) {
        this.player.setFlipX(vx < 0);
        if (onFloor) this.playerFsm.setState('walk');
      } else {
        if (onFloor) this.playerFsm.setState('idle');
      }

      const jumpPressed = this.inputMgr.justDown('up')
        || this.inputMgr.justDown('w')
        || this.inputMgr.justDown('space');

      if (jumpPressed && onFloor) {
        this.playerFsm.setState('jump');
      }
    } else if (inDialog || this.playerFsm.is('talk')) {
      this.player.setVelocityX(0);
    }

    // NPC looks toward player
    if (this.npc) {
      const dx = this.player.x - this.npc.x;
      this.npc.setFlipX(dx < 0);
    }

    // Update jump state
    this.playerFsm.update(0);
  }
}
