export class ProceduralSfx {
  constructor(ctx) {
    this.ctx = ctx;
    this._vol = 0.7;
  }

  setVolume(v) { this._vol = v; }

  click()      { this._run(() => this._sweep(700, 1100, 0.07, 0.18)); }
  confirm()    { this._run(() => { this._tone(523, 0, 0.09, 0.16); this._tone(784, 0.09, 0.14, 0.20); }); }
  correct()    { this._run(() => { [[523,0],[659,.08],[784,.16],[1047,.26]].forEach(([hz,t]) => this._tone(hz, t, 0.13, 0.18)); }); }
  wrong()      { this._run(() => this._sweep(280, 110, 0.30, 0.14, 'sawtooth')); }
  dialog()     { this._run(() => this._tone(900, 0, 0.022, 0.06)); }
  transition() { this._run(() => this._sweep(200, 650, 0.22, 0.09)); }

  _run(fn) {
    if (!this.ctx) return;
    if (this.ctx.state === 'suspended') {
      this.ctx.resume().then(fn).catch(() => {});
    } else {
      fn();
    }
  }

  _tone(hz, delaySec, dur, vol, type = 'sine') {
    try {
      const t = this.ctx.currentTime + delaySec + 0.01;
      const osc = this.ctx.createOscillator();
      const env = this.ctx.createGain();
      osc.type = type;
      osc.frequency.value = hz;
      env.gain.setValueAtTime(0, t);
      env.gain.linearRampToValueAtTime(vol * this._vol, t + 0.015);
      env.gain.linearRampToValueAtTime(0, t + dur);
      osc.connect(env);
      env.connect(this.ctx.destination);
      osc.start(t);
      osc.stop(t + dur + 0.02);
    } catch (_) {}
  }

  _sweep(fromHz, toHz, dur, vol, type = 'sine') {
    try {
      const t = this.ctx.currentTime + 0.01;
      const osc = this.ctx.createOscillator();
      const env = this.ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(fromHz, t);
      osc.frequency.linearRampToValueAtTime(toHz, t + dur);
      env.gain.setValueAtTime(vol * this._vol, t);
      env.gain.linearRampToValueAtTime(0, t + dur);
      osc.connect(env);
      env.connect(this.ctx.destination);
      osc.start(t);
      osc.stop(t + dur + 0.02);
    } catch (_) {}
  }
}
