export class InputManager {
  constructor(scene) {
    this.scene = scene;
    this.keys = {};
    this.pointers = [];
    this.gamepad = null;
    this._callbacks = { up: [], down: [], left: [], right: [], action: [], cancel: [] };
    this._setup();
  }

  _setup() {
    const { keyboard } = this.scene.input;

    this.keys = keyboard.addKeys({
      up: Phaser.Input.Keyboard.KeyCodes.UP,
      down: Phaser.Input.Keyboard.KeyCodes.DOWN,
      left: Phaser.Input.Keyboard.KeyCodes.LEFT,
      right: Phaser.Input.Keyboard.KeyCodes.RIGHT,
      w: Phaser.Input.Keyboard.KeyCodes.W,
      s: Phaser.Input.Keyboard.KeyCodes.S,
      a: Phaser.Input.Keyboard.KeyCodes.A,
      d: Phaser.Input.Keyboard.KeyCodes.D,
      space: Phaser.Input.Keyboard.KeyCodes.SPACE,
      enter: Phaser.Input.Keyboard.KeyCodes.ENTER,
      esc: Phaser.Input.Keyboard.KeyCodes.ESC,
      shift: Phaser.Input.Keyboard.KeyCodes.SHIFT,
    });

    this.scene.input.on('pointerdown', (p) => this._onPointer(p));

    if (this.scene.input.gamepad) {
      this.scene.input.gamepad.on('connected', (pad) => { this.gamepad = pad; });
    }
  }

  _onPointer(pointer) {
    this._callbacks.action.forEach(cb => cb({ x: pointer.x, y: pointer.y, source: 'touch' }));
  }

  on(action, callback) {
    if (this._callbacks[action]) this._callbacks[action].push(callback);
  }

  getAxis() {
    const x = (this.isDown('right') || this.isDown('d') ? 1 : 0)
             - (this.isDown('left') || this.isDown('a') ? 1 : 0);
    const y = (this.isDown('down') || this.isDown('s') ? 1 : 0)
             - (this.isDown('up') || this.isDown('w') ? 1 : 0);

    if (this.gamepad) {
      return {
        x: x || this.gamepad.leftStick.x,
        y: y || this.gamepad.leftStick.y,
      };
    }
    return { x, y };
  }

  isDown(key) {
    return this.keys[key]?.isDown ?? false;
  }

  justDown(key) {
    return Phaser.Input.Keyboard.JustDown(this.keys[key] ?? {});
  }

  justUp(key) {
    return Phaser.Input.Keyboard.JustUp(this.keys[key] ?? {});
  }

  isActionDown() {
    return this.isDown('space') || this.isDown('enter')
      || this.gamepad?.A?.isDown;
  }

  isCancelDown() {
    return this.isDown('esc') || this.gamepad?.B?.isDown;
  }

  destroy() {
    this.scene.input.keyboard.removeAllKeys();
    this._callbacks = {};
  }
}
