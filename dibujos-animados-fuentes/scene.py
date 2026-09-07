import math
import random
import pygame
import config

random.seed(42)

# superficie de fondo reutilizada -se alloca una sola vez tras pygame.init()
_bg_surf: pygame.Surface | None = None

def _get_bg_surf() -> pygame.Surface:
    global _bg_surf
    if _bg_surf is None:
        _bg_surf = pygame.Surface((config.WIDTH, config.HEIGHT))
    return _bg_surf

# cielo pre-renderizado (gradiente estático, se dibuja una sola vez)
_sky_cache: pygame.Surface | None = None

def _get_sky_cache() -> pygame.Surface:
    global _sky_cache
    if _sky_cache is None:
        _sky_cache = pygame.Surface((config.WIDTH, config.HEIGHT))
        top, bot = config.SKY_TOP, config.SKY_BOTTOM
        for y in range(config.HEIGHT):
            t = y / config.HEIGHT
            r = int(top[0] + (bot[0] - top[0]) * t)
            g = int(top[1] + (bot[1] - top[1]) * t)
            b = int(top[2] + (bot[2] - top[2]) * t)
            pygame.draw.line(_sky_cache, (r, g, b), (0, y), (config.WIDTH, y))
    return _sky_cache

# halo de luna pre-renderizado (anillos concéntricos estáticos)
_moon_halo: pygame.Surface | None = None

def _get_moon_halo() -> pygame.Surface:
    global _moon_halo
    if _moon_halo is None:
        size = 108
        _moon_halo = pygame.Surface((size, size), pygame.SRCALPHA)
        for r in range(52, 24, -4):
            alpha = int(30 * (52 - r) / 24)
            pygame.draw.circle(_moon_halo, (*config.MOON_GLOW, alpha), (size // 2, size // 2), r)
    return _moon_halo

# superficie compartida para halos de luciérnagas (evita allocs por frame)
_halo_surf: pygame.Surface | None = None

def _get_halo_surf() -> pygame.Surface:
    global _halo_surf
    if _halo_surf is None:
        _halo_surf = pygame.Surface((14, 14), pygame.SRCALPHA)
    return _halo_surf

# superficies de brillo pre-alocadas por radio de copa (evita allocs por árbol/frame)
_GLOW_SURFS: dict[int, pygame.Surface] = {}

def _get_glow_surf(crown_r: int) -> pygame.Surface:
    if crown_r not in _GLOW_SURFS:
        size = crown_r * 4
        _GLOW_SURFS[crown_r] = pygame.Surface((size, size), pygame.SRCALPHA)
    return _GLOW_SURFS[crown_r]

# superficies de partículas pre-alocadas por (tamaño, color)
_PARTICLE_SURF_CACHE: dict[tuple, pygame.Surface] = {}

def _get_particle_surf(size: int, color: tuple) -> pygame.Surface:
    key = (size, *color)
    if key not in _PARTICLE_SURF_CACHE:
        s = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*color, 255), (size, size), size)
        _PARTICLE_SURF_CACHE[key] = s
    return _PARTICLE_SURF_CACHE[key]

#---------------------------------------------  
# cielo nocturno con estrellas
#---------------------------------------------  

STARS = [
    (random.randint(0, config.WIDTH), random.randint(0, int(config.HEIGHT * 0.68)),
     random.uniform(0.4, 1.2) , random.uniform(0, math.pi * 2))
    for _ in range(120)
]

def draw_gradient_sky(surface):
    surface.blit(_get_sky_cache(), (0, 0))

def draw_stars(surface, elapsed_sec):
    for (sx, sy, size, phase) in STARS:
        flicker = 0.5 + 0.5 * math.sin(elapsed_sec * 2.5 + phase)
        alpha = int(160 + 90 * flicker)
        r = int(config.STAR[0] * alpha / 255)
        g = int(config.STAR[1] * alpha / 255)
        b = int(config.STAR[2] * alpha / 255)
        radius = max(1, int(size))
        pygame.draw.circle(surface, (r, g, b), (sx, sy), radius)

def draw_moon(surface, elapsed_sec):
    progress = elapsed_sec /config.TOTAL_SECONDS
    angle = math.pi * (0.1 + progress * 0.8)
    cx = int(config.WIDTH * 0.5 + math.cos(math.pi - angle) * config.WIDTH * 0.38)
    cy = int(config.HEIGHT * 0.5 - math.sin(angle) * config.HEIGHT * 0.48)
    
    halo = _get_moon_halo()
    surface.blit(halo, (cx - halo.get_width() // 2, cy - halo.get_height() // 2))

    pygame.draw.circle(surface, config.MOON, (cx, cy), 30)
    # sombra interior para efecto creciente
    pygame.draw.circle(surface, (config.SKY_TOP[0] + 5, config.SKY_TOP[1] + 5,
                                 config.SKY_TOP[2] + 10),  (cx + 8, cy - 4), 26)

#------------------------------
# suelo del bosque
#------------------------------

def draw_ground(surface):
    ground_y = int(config.HEIGHT * 0.72)
    pygame.draw.rect(surface, config.GROUND,      
                     (0, ground_y, config.WIDTH, config.HEIGHT - ground_y))
    pygame.draw.rect(surface, config.GROUND_DARK, (0, ground_y, config.WIDTH, 5))
    
    # manchas de musgo con colors sutiles
    moss_spots = [
        (150,  ground_y + 8, 60, 14, (20, 80, 40)),
        (380,  ground_y + 5, 80, 16, (25, 90, 45)),
        (620,  ground_y + 9, 55, 12, (18, 70, 35)),
        (850,  ground_y + 6, 70, 15, (22, 85, 42)),
        (1100, ground_y + 8, 65, 13, (20, 75, 38)),
    ]
    for (mx, my, mw, mh, mc) in moss_spots:
        pygame.draw.ellipse(surface, mc, (mx, my, mw, mh))

#----------------------------------------------------
# árboles mágicos con copas de colores alerbrije
#----------------------------------------------------

TREE_DEFS = [
    (  75, int(config.HEIGHT * 0.72),  85, 48, 0),
    ( 215, int(config.HEIGHT * 0.72), 100, 58, 1),
    ( 360, int(config.HEIGHT * 0.72),  70, 42, 2),
    ( 980, int(config.HEIGHT * 0.72),  90, 54, 3),
    (1090, int(config.HEIGHT * 0.72),  75, 46, 4),
    (1200, int(config.HEIGHT * 0.72),  68, 40, 5),
]

def draw_magic_tree(surface, x, y, trunk_h, crown_r, color_idx, elapsed_sec):
    trunk_w = 16
    pygame.draw.rect(surface, config.TRUNK,
                        (x - trunk_w // 2, y - trunk_h, trunk_w, trunk_h))    


    leaf_color = config.LEAVES_COLORS[color_idx % len(config.LEAVES_COLORS)]
    # pulsación suave de brillo
    pulse = 0.85 + 0.15 * math.sin(elapsed_sec * 1.8 + color_idx * 1.1)
    lc = tuple(min(255, int(c * pulse)) for c in leaf_color)  

    dark = tuple(max(0, int(c * 0.55)) for c in leaf_color)
    cx_t = x
    cy_t = y - trunk_h - crown_r + 10

    pygame.draw.circle(surface, dark, (cx_t, cy_t),  crown_r + 5)
    pygame.draw.circle(surface, lc,   (cx_t, cy_t), crown_r )

    # pequeños puntos de colores complementarios sobre la copa (estilo alebrije)
    accent = config.LEAVES_COLORS[(color_idx + 2) % len(config.LEAVES_COLORS)]
    for i in range(5):
        a = (2 * math.pi /5) * i
        dx = int(math.cos(a) * crown_r * 0.55)
        dy = int(math.sin(a) * crown_r * 0.55)
        pygame.draw.circle(surface, accent, (cx_t + dx, cy_t + dy), 4)

    glow_surf = _get_glow_surf(crown_r)
    glow_surf.fill((0, 0, 0, 0))
    pygame.draw.circle(glow_surf, (*lc, int(35 * pulse)),
                       (crown_r * 2, crown_r * 2), crown_r + 8)
    surface.blit(glow_surf, (cx_t - crown_r * 2, cy_t - crown_r * 2))

#----------------------------------------------------
# hongos magicos
#----------------------------------------------------

MUSHROOMS = [
    ( 310, int(config.HEIGHT * 0.72), 1.2),
    ( 480, int(config.HEIGHT * 0.72), 0.8),
    ( 700, int(config.HEIGHT * 0.72), 1.0),
    ( 820, int(config.HEIGHT * 0.72), 0.7),
    (1020, int(config.HEIGHT * 0.72), 1.1),
]

def draw_mushroom(surface, x, base_y, scale, elapsed_sec):
    stem_h = int(28 * scale)        
    stem_w = int(10 * scale)
    cap_w  = int(40 * scale)
    cap_h  = int(22 * scale)
    stem_x = x - stem_w // 2
    stem_y = base_y - stem_h
    pygame.draw.rect(surface, config.MUSHROOM_STEM,
                     (stem_x, stem_y, stem_w, stem_h))
    
    cap_x = x - cap_w // 2
    cap_y = stem_y - cap_h // 2
    pulse = 0.88 + 0.12 * math.sin(elapsed_sec * 2.2 + x * 0.01)
    cap_color = tuple(min(255, int(c * pulse)) for c in config.MUSHROOM_CAP)
    pygame.draw.ellipse(surface, cap_color, (cap_x, cap_y, cap_w, cap_h))

    # puntos blancos
    for i, (ox, oy) in enumerate([(-8, 4), (5, 2), (0, 8) , (-4, 10)]):
        sx = int(ox * scale)
        sy = int(oy * scale)
        pygame.draw.circle(surface, config.MUSHROOM_SPOTS,
                           (x + sx, cap_y + sy), max(2, int(3 * scale)))

#---------------------------------------------  
# luciernagas                    
#---------------------------------------------  
class Firefly:
    def __init__(self):
        self._reset(init=True)

    def _reset(self, init=False):
        self.x  = random.uniform(50, config.WIDTH - 50)
        self.y = random.uniform(config.HEIGHT * 0.25, config.HEIGHT * 0.70)
        self.phase = random.uniform(0, math.pi * 2)
        self.freq = random.uniform(1.5, 3.5)
        self.vx = random.uniform(-18, 18) 
        self.vy = random.uniform(-12, 12) 
        if init:
            self.elapsed = random.uniform(0, 6)
        else:
            self.elapsed = 0
    def update(self, dt):
        self.elapsed += dt
        self.x += self.vx * dt + math.sin(self.elapsed * 1.3 + self.phase) * 12 * dt
        self.y += self.vy * dt + math.cos(self.elapsed * 1.1 + self.phase) * 8 * dt
        if self.x < 0 or self.x > config.WIDTH or self.y < 0 or self.y > config.HEIGHT * 0.72:
            self._reset()
    
    def draw(self, surface, elapsed_sec):
        glow = 0.5 + 0.5 * math.sin(elapsed_sec * self.freq + self.phase)
        if glow < 0.2:
            return
        alpha = int(glow * 220)
        r = min(255, int(config.FIREFLY[0] * glow + 40))
        g = min(255, int(config.FIREFLY[1] * glow))
        b = min(255, int(config.FIREFLY[2] * glow))
        pygame.draw.circle(surface, (r, g, b), (int(self.x), int(self.y)), 3)
        halo = _get_halo_surf()
        halo.fill((0, 0, 0, 0))
        pygame.draw.circle(halo, (r, g, b, int(alpha * 0.35)), (7, 7), 7)
        surface.blit(halo, (int(self.x) - 7, int(self.y) - 7))

FIREFLIES = [Firefly() for _ in range(28)]


#--------------------------------
# particulas mágicas flotantes (polvo de hadas)
#--------------------------------
class MagicParticle:
    def __init__(self):
        self._reset(init=True)
    
    def _reset(self, init=False):
        self.x = random.uniform(0, config.WIDTH)
        self.y =  random.uniform(config.HEIGHT * 0.1, config.HEIGHT * 0.68)
        self.color = random.choice(config.MAGIC_COLORS)
        self.life = random.uniform(1.5, 4.0)
        self.age = random.uniform(0, self.life) if init else 0
        self.vy = random.uniform(-15, -30)
        self.vx = random.uniform(-8, 8)
        self.size = random.randint(2, 4)

    def update(self, dt):
        self.age +=  dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        if self.age >= self.life:
            self._reset()

    def draw(self, surface):
        t = self.age / self.life
        alpha = int(255 * (1 - t) * min(1, t * 6))
        if alpha < 10:
            return
        s = _get_particle_surf(self.size, self.color)
        s.set_alpha(alpha)
        surface.blit(s, (int(self.x) - self.size, int(self.y) - self.size))

MAGIC_PARTICLES = [MagicParticle() for _ in range(60)]

#---------------------------------------
# update /draw principal
#---------------------------------------
def update(dt):
    for ff in FIREFLIES:
        ff.update(dt)
    for mp in  MAGIC_PARTICLES:
        mp.update(dt)

def draw(surface, elapsed_sec):
    bg = _get_bg_surf()

    draw_gradient_sky(bg)
    draw_stars(bg, elapsed_sec)
    draw_moon(bg, elapsed_sec)
    draw_ground(bg)

    for (x, y, th, cr, cidx) in TREE_DEFS:
        draw_magic_tree(bg, x, y, th, cr, cidx, elapsed_sec)

    for (mx, my, ms) in MUSHROOMS:
        draw_mushroom(bg, mx, my, ms, elapsed_sec)

    for mp in MAGIC_PARTICLES:
        mp.draw(bg)

    for ff in FIREFLIES:
        ff.draw(bg, elapsed_sec)

    # blit del fondo con la transparencia configuada; base negra
    surface.fill((0,0,0))
    bg.set_alpha(config.BG_ALPHA)
    surface.blit(bg, (0,0))





