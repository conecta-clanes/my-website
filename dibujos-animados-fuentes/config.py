import os

WIDTH, HEIGHT = 1280, 720

#WIDTH, HEIGHT = 1960, 1280
FPS = 30
#TOTAL_SECONDS = 180                 # 3 minutos -- ajusta según necesitas

TOTAL_SECONDS = 480

#Rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#assets default
ASSETS_DIR = os.path.join(BASE_DIR, "assets" , "scanned")
# bandera para --grabar
OUTPUT_PATH = os.path.join(BASE_DIR, "output" , "animation.mp4")

#Tamaño máximo de dibujos escaneados(ancho en pixeles)
MAX_DRAWING_WIDTH = 300

#Umbral para eliminar fondo blanco (0-255); pixeles con R, G, B > THRESHOLD se vuelven transparentes
WHITE_THRESHOLD = 220
#160 transparente # 240 opaco
BG_ALPHA = 200

#Colores de la escena
SKY_TOP     = ( 20, 10,  70)    # noche profunda violeta
SKY_BOTTOM  = ( 45, 80, 160)    # horizonte azul medianoche
GROUND      = ( 35,110,  60)    # musgo oscuro
GROUND_DARK = ( 20, 70,  38)    # sombra del suelo

MOON      = (240, 250, 255)     # luna plateada
MOON_GLOW = (200, 230,  30)     # halo lunar

TRUNK       = ( 80, 40, 120)    # tronco púrpura oscuro
LEAVES_COLORS = [
    (255,  80, 200),    # magenta alebrije
    ( 80, 160, 255),    # azul-turquesa
    (255, 160,   0),    # naranja fuego
    (160,  90, 255),    # violeta intenso
    ( 80, 240, 100),    # verde neón
    (255, 235,  60),    # amarillo dorado
]

MUSHROOM_CAP    = (255,  80, 160)
MUSHROOM_STEM   = (245, 215, 175)
MUSHROOM_SPOTS  = (255, 255, 210)

FIREFLY = (210, 255, 110) # luciérnagas verde-amarillo
STAR    = (255, 255, 240) # estrella blanca cálida

MAGIC_COLORS = [
    (255,  90, 220),
    ( 90, 255, 230),
    (255, 200,  50),
    (160, 100, 255),
]