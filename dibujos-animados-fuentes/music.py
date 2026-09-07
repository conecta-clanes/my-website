"""
Música chiptune generada por síntesis de ondas (numpy + pygame).
Sin archivos externos, Escala C lidio, estilo RPG/aventura, loop de 4 compases
"""

import numpy as np
import pygame

SR = 44100              # sample rate(Hz)
BPM = 108
BEAT = 60.0 / BPM       # segundos por tiempo

# Frecuencia de notas (Hz) ----------------------------------------------

NOTE = {
'C3':  130.81, 'D3': 146.83, 'E3': 164.81,
'G3':  196.00, 'A3': 220.0,
'C4':  261.63, 'D4': 293.66, 'E4': 329.63,
'Fs4': 369.99, 'G4': 392.00, 'A4': 440.00, 'B4': 493.88,
'C5':  523.25, 'D5': 587.33, 'E5': 659.25,
'Fs5': 739.99, 'G5': 783.99, 'A5': 880.00, 'B5': 987.77,
'R':   0,
}

# sintesis ----------------------------------------------------------------
def _env (n: int, atk: float = 0.01, rel: float = 0.08) -> np.ndarray:
    e = np.ones(n, dtype=np.float32)
    a, r = int(n * atk), int(n * rel)
    if a: e[:a]  = np.linspace(0, 1, a)
    if r: e[-r:] = np.linspace(1, 0, r)
    return e


def _square(freq: float, dur: float, vol: float = 1.0, duty: float = 0.5) -> np.ndarray:
    n = max(1, int(SR * dur))
    if freq <= 0:
        return np.zeros(n, dtype=np.float32)
    t = np.arange(n, dtype=np.float32) /SR
    wave =  np.where((t * freq % 1.0) < duty, 1.0, -1.0).astype(np.float32)
    return wave * _env(n) * vol


def _triangle(freq: float, dur: float, vol: float = 1.0) -> np.ndarray:
    n = max(1, int(SR * dur))
    if freq <= 0:
        return np.zeros(n, dtype=np.float32)
    t = np.arange(n, dtype=np.float32) / SR
    phase = ( t * freq) % 1.0
    wave = (2 * np.abs(2*phase - 1) - 1).astype(np.float32)
    return wave * _env(n, 0.005, 0.05) * vol

def _noise(dur: float, vol: float = 1.0) -> np.ndarray:
    n = max(1, int(SR * dur))
    rng = np.random.default_rng(seed=7)
    wave = rng.uniform(-1, 1, n).astype(np.float32)
    return wave * _env(n, 0.002, 0.65) * vol

def _render_melody(seq, vol: float) -> np.ndarray:
    return np.concatenate([_square(NOTE[n], b * BEAT, vol) for n, b in seq])

def _render_harmony(seq, vol: float) -> np.ndarray:                         
    return np.concatenate([_square(NOTE[n], b * BEAT, vol, duty=0.25) for n, b in seq])

def _render_bass(seq, vol: float) -> np.ndarray:  
    return np.concatenate([_triangle(NOTE[n], b * BEAT, vol) for n, b in seq])

def _render_perc(seq, vol: float) -> np.ndarray: 
    parts = []
    for hit, beats in seq:
        dur = beats * BEAT
        parts.append(_noise(dur, vol) if hit else np.zeros(int(SR * dur), dtype=np.float32))
    return np.concatenate(parts)

def _mix(*tracks: np.ndarray) -> np.ndarray:
    maxlen =  max(len(t) for t in tracks)
    out = np.zeros(maxlen, dtype=np.float32)
    for t in tracks:
        out[:len(t)] += t
    return np.clip(out, -1.0, 1.0)

  
# composición 4 compases, 16 tiempos, C lidio ------------------------------------
#  C lidio: C D E F# G A B (el F# le da el toque mágico/etéreo)

MELODY = [
        #Compás 1
        ('C5',  1),   ('E5', 0.5) , ('G5', 0.5), ('A5', 1), ('G5', 0.5), ('E5', 0.5),
        #Compás 2
        ('Fs5', 0.5), ('E5', 0.5) , ('D5', 1), ('G5', 1.5), ('R', 0.5), 
        #Compás 3
        ('E5',  0.5), ('G5', 0.5) , ('A5', 1), ('B5', 0.5), ('A5', 0.5), ('G5', 0.1),
        #Compás 4
        ('Fs5', 0.5), ('G5', 0.5) , ('E5', 0.5), ('D5', 0.5), ('C5', 2),  
] #total : 16 tiempos

HARMONY = [
       ('G4', 2), ('E4', 2) , #compás 1
       ('Fs4', 2), ('G4', 2) , #compás 2
       ('C4', 2), ('G4', 2) , #compás 3
       ('D4', 2), ('C4', 2) , #compás 4
] #total : 16 tiempos

BASS = [      
      ('C3', 4),                # compás 1
      ('D3', 2), ('G3', 2),     # compás 2
      ('C3', 2), ('G3', 2),     # compás 3
      ('D3', 2), ('C3', 2),     # compás 4
] #total : 16 tiempos

# hi hat en corchetes: alterna silencia / golpe (32 x 0.5 = 16 tiempos)
PERC = [(i % 2==1, 0.5) for i in range(32)]

# API pública--------------------------------------------------------------------
def pre_init():
    """llame antes de pygame.init() para configurar el mixer"""
    pygame.mixer.pre_init(frequency=SR, size=-16, channels=2, buffer=2048)

def _build_loop(volume: float = 0.72) -> np.ndarray:
    return _mix(
        _render_melody(MELODY,   vol=0.30 * volume),
        _render_harmony(HARMONY, vol=0.16 * volume),
        _render_bass(BASS,       vol=0.22 * volume),
        _render_perc(PERC,       vol=0.09 * volume),
    )

def generate_and_play(volume: float = 0.72) -> pygame.mixer.Sound:
    """
    Sinteriza la pista y la reprodece en loop infinito
    llama despúes de pygame. init(). Devuelve el sound (grupos la ferencias)
    """
    print("[Música] Sintetizando pista chiptune...")
    loop = _build_loop(volume)
    sound = _to_stereo_sound(loop)
    sound.play(loops=-1)
    print(f"[Música] Reproduciendo en loop({len(loop) / SR:.1f} s por vuelta )")
    return sound

def build_full_track(total_seconds: float, volume: float = 0.72) -> np.ndarray:
    """Devuelve PCM estéreo int16 con duración total_seconds, repitiendo el loop."""
    loop = _build_loop(volume)
    needed = int(total_seconds * SR) + SR   # +1 s de margen
    reps = -(-needed // len(loop))          # ceil division
    full = np.tile(loop, reps)[:needed]
    stereo = np.stack([full, full], axis=1)
    return (stereo * 32767).astype(np.int16)

def _to_stereo_sound(mono: np.ndarray) -> pygame.mixer.Sound:
    stereo = np.stack([mono, mono], axis = 1)
    pcm = (stereo * 32767).astype(np.int16)
    return pygame.sndarray.make_sound(pcm)

