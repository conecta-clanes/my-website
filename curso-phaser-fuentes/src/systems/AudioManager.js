export class AudioManager {
  constructor(scene) {
    this.scene = scene;
    this.music = null;
    this.sfxVolume = 0.7;
    this.musicVolume = 0.5;
    this.muted = false;
    this._tracks = {};
  }

  setVolumes(sfx, music) {
    this.sfxVolume = sfx;
    this.musicVolume = music;
    if (this.music) this.music.setVolume(this.muted ? 0 : music);
  }

  playMusic(key, { loop = true, fade = 1000 } = {}) {
    if (this.music?.isPlaying && this.music.key === key) return;
    if (this.music?.isPlaying) {
      this.scene.tweens.add({
        targets: this.music,
        volume: 0,
        duration: fade,
        onComplete: () => { this.music?.stop(); this._startMusic(key, loop, fade); },
      });
    } else {
      this._startMusic(key, loop, fade);
    }
  }

  _startMusic(key, loop, fade) {
    if (!this.scene.cache.audio.has(key)) return;
    this.music = this.scene.sound.add(key, { loop, volume: 0 });
    this.music.play();
    if (!this.muted) {
      this.scene.tweens.add({
        targets: this.music,
        volume: this.musicVolume,
        duration: fade,
      });
    }
  }

  playSfx(key, config = {}) {
    if (this.muted) return;
    if (!this.scene.cache.audio.has(key)) return;
    this.scene.sound.play(key, { volume: this.sfxVolume, ...config });
  }

  stopMusic(fade = 800) {
    if (!this.music?.isPlaying) return;
    this.scene.tweens.add({
      targets: this.music,
      volume: 0,
      duration: fade,
      onComplete: () => this.music?.stop(),
    });
  }

  toggleMute() {
    this.muted = !this.muted;
    if (this.music) this.music.setVolume(this.muted ? 0 : this.musicVolume);
    return this.muted;
  }
}
