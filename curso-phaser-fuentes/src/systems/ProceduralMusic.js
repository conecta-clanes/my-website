// G major scale semitones from G3 (196 Hz)
// G A B C D E F# G  →  0 2 4 5 7 9 11 12
const G3 = 196.00;
const BPM = 76;
const BEAT = 60 / BPM;
const LOOP = 8 * BEAT; // 2-bar loop

const hz = (st) => G3 * Math.pow(2, st / 12);

// Main melody (8 beats)
const MELODY = [
  { st: 0,  b: 0,   d: 0.85 }, // G3
  { st: 7,  b: 1,   d: 0.85 }, // D4
  { st: 12, b: 2,   d: 0.85 }, // G4
  { st: 11, b: 3,   d: 0.4  }, // F#4
  { st: 7,  b: 3.5, d: 0.4  }, // D4
  { st: 5,  b: 4,   d: 0.85 }, // C4
  { st: 4,  b: 5,   d: 0.85 }, // B3
  { st: 7,  b: 6,   d: 1.7  }, // D4 held
];

// High shimmer notes (beats 0.5, 2, 4, 6)
const SHIMMER = [
  { st: 12, b: 0.5 }, // G4
  { st: 14, b: 2   }, // A4
  { st: 16, b: 4   }, // B4
  { st: 12, b: 6   }, // G4
];

export class ProceduralMusic {
  constructor(ctx) {
    this.ctx = ctx;
    this.gain = null;
    this._until = 0;
    this._tid = null;
    this.running = false;
    this._vol = 0.09;
  }

  start(vol = 0.09) {
    if (this.running || !this.ctx) return;
    this._vol = vol;
    this.running = true;

    this.gain = this.ctx.createGain();
    this.gain.gain.setValueAtTime(0, this.ctx.currentTime);
    this.gain.gain.linearRampToValueAtTime(vol, this.ctx.currentTime + 3);
    this.gain.connect(this.ctx.destination);

    this._until = this.ctx.currentTime + 0.05;
    this._tick();
  }

  setVolume(v) {
    this._vol = v;
    if (this.gain && this.running) {
      this.gain.gain.cancelScheduledValues(this.ctx.currentTime);
      this.gain.gain.linearRampToValueAtTime(v, this.ctx.currentTime + 0.5);
    }
  }

  stop(fadeSec = 2) {
    if (!this.running) return;
    this.running = false;
    clearTimeout(this._tid);
    if (this.gain) {
      this.gain.gain.cancelScheduledValues(this.ctx.currentTime);
      this.gain.gain.linearRampToValueAtTime(0, this.ctx.currentTime + fadeSec);
    }
  }

  _tick() {
    if (!this.running) return;
    const now = this.ctx.currentTime;
    while (this._until < now + 1.8) {
      this._scheduleLoop(this._until);
      this._until += LOOP;
    }
    this._tid = setTimeout(() => this._tick(), 300);
  }

  _scheduleLoop(t) {
    // Bass: G2 + D3 sustained
    this._note(hz(-12), t, LOOP * 0.94, 0.13, 'sine');
    this._note(hz(-5),  t, LOOP * 0.94, 0.07, 'sine');

    // Melody
    MELODY.forEach(({ st, b, d }) => {
      this._note(hz(st), t + b * BEAT, d * BEAT, 0.18, 'triangle');
    });

    // Shimmer
    SHIMMER.forEach(({ st, b }) => {
      this._note(hz(st), t + b * BEAT, 0.35 * BEAT, 0.06, 'sine');
    });
  }

  _note(frequency, start, dur, vol, type) {
    try {
      const osc = this.ctx.createOscillator();
      const env = this.ctx.createGain();
      osc.type = type;
      osc.frequency.value = frequency;
      const att = Math.min(0.06, dur * 0.15);
      env.gain.setValueAtTime(0, start);
      env.gain.linearRampToValueAtTime(vol, start + att);
      env.gain.setValueAtTime(vol * 0.75, start + dur - 0.05);
      env.gain.linearRampToValueAtTime(0, start + dur);
      osc.connect(env);
      env.connect(this.gain);
      osc.start(start);
      osc.stop(start + dur + 0.02);
    } catch (_) { /* audio context may be suspended */ }
  }
}
