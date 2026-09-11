"""Audio sintético: música ambiental eco-temática y efectos de sonido."""
import os
import wave
import numpy as np
import pygame

_SR = 44100


# ── helpers ────────────────────────────────────────────────────────────────

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


# ── música ambiental eco ────────────────────────────────────────────────────

def _generate_eco_track(duration=32):
    n = int(duration * _SR)
    t = np.arange(n) / _SR
    rng = np.random.default_rng(42)

    # Viento suave (ruido filtrado)
    wind = rng.standard_normal(n) * 0.07
    wind = np.convolve(wind, np.ones(300) / 300, mode='same')
    wind *= 0.6 + 0.4 * np.sin(2 * np.pi * 0.04 * t)

    # Bajo/drone natural en Do mayor
    drone = (
        _sine(65.41,  t, 0.09) +   # C2
        _sine(130.81, t, 0.055) +  # C3
        _sine(196.00, t, 0.03)     # G3
    ) * (0.65 + 0.35 * np.sin(2 * np.pi * 0.055 * t))

    # Pad etéreo (coros armónicos)
    pad = (
        _sine(261.63, t, 0.055) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.11 * t)) +
        _sine(329.63, t, 0.04)  * (0.5 + 0.5 * np.sin(2 * np.pi * 0.07 * t)) +
        _sine(392.00, t, 0.035) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.09 * t))
    )

    # Arpegio pentatónico (gotas de agua / hojas)
    penta    = [523.25, 587.33, 659.25, 783.99, 880.00]  # C5 D5 E5 G5 A5
    note_dur = 0.28
    arp      = np.zeros(n)
    rng2     = np.random.default_rng(7)
    for i in range(int(duration / note_dur) + 1):
        freq  = penta[rng2.integers(0, len(penta))]
        start = int(i * note_dur * _SR)
        length = int(0.20 * _SR)
        end    = min(start + length, n)
        length = end - start
        if length <= 0:
            break
        ts  = np.arange(length) / _SR
        env = np.exp(-ts * 18)
        arp[start:end] += 0.045 * env * np.sin(2 * np.pi * freq * ts)

    # Trinos de pájaros (breves barridos de frecuencia)
    chirps = np.zeros(n)
    for i, cs in enumerate(range(0, n, int(2.8 * _SR))):
        for offset, f0, f1 in [(0, 2200, 1800), (int(0.09 * _SR), 2650, 2100)]:
            pos = cs + offset
            ln  = int(0.055 * _SR)
            if pos + ln > n:
                continue
            ts  = np.arange(ln) / _SR
            fsw = np.linspace(f0, f1, ln)
            env = np.exp(-ts * 45)
            chirps[pos:pos + ln] += 0.03 * env * np.sin(2 * np.pi * np.cumsum(fsw) / _SR)

    mix  = drone + pad + arp + wind + chirps
    mix  = mix / (np.max(np.abs(mix)) + 1e-8) * 0.78
    left  = mix * (0.9 + 0.1 * np.sin(2 * np.pi * 0.025 * t))
    right = mix * (0.9 + 0.1 * np.sin(2 * np.pi * 0.025 * t + np.pi))
    return (np.column_stack([left, right]) * 32767).astype(np.int16)


def ensure_music(path="assets/music_eco.wav"):
    if not os.path.exists(path):
        data = _generate_eco_track(duration=32)
        with wave.open(path, "w") as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(_SR)
            wf.writeframes(data.tobytes())
    return path


# ── efectos de sonido ───────────────────────────────────────────────────────

def blow_samples() -> np.ndarray:
    """Soplo de aire suave (whoosh corto)."""
    n   = int(0.09 * _SR)
    rng = np.random.default_rng(1)
    noise = rng.standard_normal(n)
    noise = np.convolve(noise, np.ones(12) / 12, mode='same')
    freq  = np.linspace(700, 150, n)
    tone  = np.sin(2 * np.pi * np.cumsum(freq) / _SR)
    env   = np.linspace(1.0, 0.0, n) ** 1.8
    mono  = (tone * 0.12 + noise * 0.08) * env
    return np.column_stack([mono, mono]).astype(np.float32)


def recycle_organic_samples() -> np.ndarray:
    """Ding cálido para reciclaje orgánico (acorde mayor suave)."""
    n = int(0.35 * _SR)
    t = np.arange(n) / _SR
    # Do mayor: C5 – E5 – G5
    wav = (
        _sine(523.25, t, 0.35) +
        _sine(659.25, t, 0.25) +
        _sine(783.99, t, 0.20)
    )
    env  = np.exp(-t * 7)
    mono = wav * env * 0.30
    return np.column_stack([mono, mono]).astype(np.float32)


def recycle_inorganic_samples() -> np.ndarray:
    """Ping metálico para reciclaje inorgánico (armónicos brillantes)."""
    n = int(0.30 * _SR)
    t = np.arange(n) / _SR
    # La mayor agudo con parciales metálicos
    wav = (
        _sine(880.00,  t, 0.35) +
        _sine(1046.50, t, 0.25) +
        _sine(1318.51, t, 0.18) +
        _sine(1760.00, t, 0.10)
    )
    env  = np.exp(-t * 11)
    mono = wav * env * 0.28
    return np.column_stack([mono, mono]).astype(np.float32)


def miss_samples() -> np.ndarray:
    """Golpe grave al perder una vida."""
    n   = int(0.40 * _SR)
    t   = np.arange(n) / _SR
    rng = np.random.default_rng(3)
    freq = np.linspace(180, 50, n)
    tone = np.sin(2 * np.pi * np.cumsum(freq) / _SR)
    noise = rng.standard_normal(n)
    noise = np.convolve(noise, np.ones(35) / 35, mode='same')
    env  = np.linspace(1.0, 0.0, n) ** 1.3
    mono = (tone * 0.30 + noise * 0.18) * env
    return np.column_stack([mono, mono]).astype(np.float32)


# ── conversión helper ───────────────────────────────────────────────────────

def _to_sound(arr: np.ndarray) -> pygame.mixer.Sound:
    clipped = np.clip(arr, -1.0, 1.0)
    return pygame.sndarray.make_sound((clipped * 32767).astype(np.int16))


# ── manager ─────────────────────────────────────────────────────────────────

class AudioManager:
    def __init__(self):
        pygame.mixer.init(frequency=_SR, size=-16, channels=2, buffer=512)
        pygame.mixer.music.load(ensure_music())
        pygame.mixer.music.set_volume(0.40)
        pygame.mixer.music.play(loops=-1)

        self._blow_snd      = _to_sound(blow_samples())
        self._rec_org_snd   = _to_sound(recycle_organic_samples())
        self._rec_inorg_snd = _to_sound(recycle_inorganic_samples())
        self._miss_snd      = _to_sound(miss_samples())

        self._blow_snd.set_volume(0.14)
        self._rec_org_snd.set_volume(0.55)
        self._rec_inorg_snd.set_volume(0.50)
        self._miss_snd.set_volume(0.60)

    def play_blow(self):
        self._blow_snd.play()

    def play_recycle(self, item_type: str):
        if item_type == "organic":
            self._rec_org_snd.play()
        else:
            self._rec_inorg_snd.play()

    def play_miss(self):
        self._miss_snd.play()

    def stop(self):
        pygame.mixer.music.stop()
        pygame.mixer.stop()
