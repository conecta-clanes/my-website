WIDTH, HEIGHT = 800, 600
FPS = 60
TITLE = "Guardianes del Reciclaje"

BLACK      = (  0,   0,   0)
WHITE      = (255, 255, 255)
RED        = (220,  50,  50)
YELLOW     = (255, 220,   0)
GREEN      = ( 50, 200,  50)
DARK_GREEN = ( 10,  50,  10)
CYAN       = (  0, 200, 255)
ORANGE     = (220, 110,   0)
LIGHT_BLUE = (100, 180, 255)

PLAYER_RADIUS     = 44
BLOW_COOLDOWN     = 400   # ms entre disparos de aire
BLOW_SPEED        = 11    # píxeles por frame
BLOW_RADIUS       = 14
BLOW_LIFETIME     = 1100  # ms

PLAYER_LIVES      = 3
INVULNERABLE_TIME = 2000  # ms

WASTE_ITEMS = [
    {"image": "assets/inorganic-aluminum-can.png",   "type": "inorganic", "points": 15},
    {"image": "assets/inorganic-glass-jar.png",      "type": "inorganic", "points": 15},
    {"image": "assets/inorganic-plastic-bottle.png", "type": "inorganic", "points": 15},
    {"image": "assets/organic-apple-core.png",       "type": "organic",   "points": 10},
    {"image": "assets/organic-banana-peel.png",      "type": "organic",   "points": 10},
    {"image": "assets/organic-eggshell.png",         "type": "organic",   "points": 10},
]

ITEM_RADIUS          = 32
SPAWN_INTERVAL_START = 2000  # ms
SPAWN_INTERVAL_MIN   = 700   # ms (máxima dificultad)
ITEM_SPEED_START     = 1.5   # píxeles por frame
ITEM_SPEED_MAX       = 4.5
