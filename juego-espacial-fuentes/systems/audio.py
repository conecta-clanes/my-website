import os
import wave
import numpy as np
import pygame

_SR = 44100


# ──────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────

def _sine(freq, t, amp=1.0):
    return amp * np.sin(2 * np.pi * freq * t)


def _adsr(n, attack=0.02, decay=0.08, sustain=0.6, release=0.2):
    a = int(attack * _SR)
    d = int(decay  * _SR)
    r = int(release * _SR)
    s = max(0, n - a - d - r)
    return np.concatenate([
        np.linspace(0, 1, a),
        np.linspace(1, sustain, d),
        np.full(s, sustain),
        np.linspace(sustain, 0, r),
    ])[:n]


# ──────────────────────────────────────────────
# Music generation
# ──────────────────────────────────────────────

def _generate_space_track(duration=32):
    n = int(duration * _SR)
    t = np.arange(n) / _SR

    slow_mod = 0.8 + 0.2 * np.sin(2 * np.pi * 0.05 * t)
    drone = (_sine(55, t, 0.12) + _sine(110, t, 0.07) + _sine(165, t, 0.04)) * slow_mod

    pad = (
        _sine(220,    t, 0.06) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.13 * t)) +
        _sine(277.18, t, 0.04) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.09 * t)) +
        _sine(329.63, t, 0.035) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.07 * t))
    )

    penta    = [220, 261.63, 293.66, 329.63, 392.0]
    note_dur = 0.375
    arp      = np.zeros(n)
    for i in range(int(duration / note_dur) + 1):
        freq  = penta[i % len(penta)]
        start = int(i * note_dur * _SR)
        end   = min(int((i + 1) * note_dur * _SR), n)
        length = end - start
        if length <= 0:
            break
        env  = _adsr(length, 0.02, 0.05, 0.5, 0.18)
        ts   = t[start:end]
        arp[start:end] += 0.06 * env * np.sin(2 * np.pi * freq * ts)
        if i % 3 == 2:
            arp[start:end] += 0.03 * env * np.sin(2 * np.pi * freq * 2 * ts)

    noise = np.random.default_rng(42).standard_normal(n) * 0.015
    noise = np.convolve(noise, np.ones(64) / 64, mode='same')

    mix  = drone + pad + arp + noise
    mix  = mix / (np.max(np.abs(mix)) + 1e-8) * 0.80
    left  = mix * (0.9 + 0.1 * np.sin(2 * np.pi * 0.03 * t))
    right = mix * (0.9 + 0.1 * np.sin(2 * np.pi * 0.03 * t + np.pi))
    stereo = np.column_stack([left, right])
    return (stereo * 32767).astype(np.int16)


def ensure_music(path="assets/music.wav"):
    if not os.path.exists(path):
        data = _generate_space_track(duration=32)
        with wave.open(path, "w") as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(_SR)
            wf.writeframes(data.tobytes())
    return path


# ──────────────────────────────────────────────
# SFX samples (float32 stereo, exported for recorder)
# ──────────────────────────────────────────────

def shoot_samples() -> np.ndarray:
    """Returns float32 stereo array [-1,1] for shoot SFX."""
    n = int(0.08 * _SR)
    t = np.arange(n) / _SR
    freq = np.linspace(900, 200, n)
    wav  = np.sin(2 * np.pi * np.cumsum(freq) / _SR)
    env  = np.linspace(1.0, 0.0, n) ** 2
    mono = wav * env * 0.25
    return np.column_stack([mono, mono]).astype(np.float32)


def explosion_samples() -> np.ndarray:
    """Returns float32 stereo array [-1,1] for explosion SFX."""
    n = int(0.45 * _SR)
    rng   = np.random.default_rng(7)
    noise = rng.standard_normal(n)
    noise = np.convolve(noise, np.ones(18) / 18, mode='same')
    env   = np.linspace(1.0, 0.0, n) ** 1.4
    mono  = noise * env * 0.55
    return np.column_stack([mono, mono]).astype(np.float32)


def _to_sound(arr: np.ndarray):
    clipped = np.clip(arr, -1, 1)
    return pygame.sndarray.make_sound((clipped * 32767).astype(np.int16))


# ──────────────────────────────────────────────
# Manager
# ──────────────────────────────────────────────

class AudioManager:
    def __init__(self):
        pygame.mixer.init(frequency=_SR, size=-16, channels=2, buffer=512)
        pygame.mixer.music.load(ensure_music())
        pygame.mixer.music.set_volume(0.45)
        pygame.mixer.music.play(loops=-1)

        self._shoot_snd   = _to_sound(shoot_samples())
        self._explode_snd = _to_sound(explosion_samples())
        self._shoot_snd.set_volume(0.18)
        self._explode_snd.set_volume(0.50)

    def play_shoot(self):
        self._shoot_snd.play()

    def play_explosion(self):
        self._explode_snd.play()

    def stop(self):
        pygame.mixer.music.stop()
