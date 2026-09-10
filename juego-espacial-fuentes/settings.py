WIDTH, HEIGHT = 800, 600
FPS = 60
TITLE = "Juego Espacial"

BLACK  = (0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (220,  50,  50)
YELLOW = (255, 220,   0)
CYAN   = (0,   200, 255)

PLAYER_ACCEL      = 0.3
PLAYER_ROT_SPEED  = 4       # degrees per frame
PLAYER_MAX_SPEED  = 7
PLAYER_FRICTION   = 0.985
SHOOT_COOLDOWN    = 300     # ms
PLAYER_LIVES      = 3
INVULNERABLE_TIME = 2000    # ms
PLAYER_RADIUS     = 44

BULLET_SPEED    = 14
BULLET_LIFETIME = 1000  # ms
BULLET_RADIUS   = 4

ENEMY_DATA = {
    'large':  {'hp': 3, 'speed': 1.0, 'points': 100, 'radius': 76, 'amplitude': 60, 'freq': 0.5},
    'medium': {'hp': 2, 'speed': 2.0, 'points': 200, 'radius': 52, 'amplitude': 40, 'freq': 1.0},
    'small':  {'hp': 1, 'speed': 3.5, 'points': 300, 'radius': 32, 'amplitude': 20, 'freq': 2.0},
}

BASE_WAVE_COUNTS = {'large': 2, 'medium': 3, 'small': 4}
WAVE_INCREMENT   = {'large': 1, 'medium': 1, 'small': 2}
