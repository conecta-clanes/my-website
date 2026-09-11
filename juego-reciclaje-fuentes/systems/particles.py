import pygame
import math
import random


class Particle:
    def __init__(self, x: float, y: float, item_type: str = "organic"):
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 7)
        self.x = x
        self.y = y
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.lifetime = random.randint(300, 700)
        self.max_life = self.lifetime
        self.radius = random.randint(2, 5)
        if item_type == "organic":
            self.color = random.choice([
                (80, 200, 80), (50, 180, 50), (120, 255, 80), (200, 240, 80)
            ])
        else:
            self.color = random.choice([
                (100, 160, 255), (150, 200, 255), (200, 220, 255), (80, 120, 220)
            ])

    def update(self, dt: int):
        self.x  += self.vx
        self.y  += self.vy
        self.vy += 0.08
        self.vx *= 0.96
        self.vy *= 0.96
        self.lifetime -= dt

    @property
    def alive(self) -> bool:
        return self.lifetime > 0

    def draw(self, surface: pygame.Surface):
        r = max(1, int(self.radius * self.lifetime / self.max_life))
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), r)


class FloatingText:
    _fonts: dict = {}

    @classmethod
    def _font(cls, size: int):
        if size not in cls._fonts:
            cls._fonts[size] = pygame.font.SysFont("Arial", size, bold=True)
        return cls._fonts[size]

    def __init__(self, x: float, y: float, text: str, color: tuple):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.lifetime = 900
        self.max_life = 900
        self._alive = True

    def update(self, dt: int):
        self.y -= 0.7
        self.lifetime -= dt
        if self.lifetime <= 0:
            self._alive = False

    @property
    def alive(self) -> bool:
        return self._alive

    def draw(self, surface: pygame.Surface):
        alpha = int(255 * max(0, self.lifetime / self.max_life))
        surf = self._font(20).render(self.text, True, self.color)
        surf.set_alpha(alpha)
        surface.blit(surf, (int(self.x) - surf.get_width() // 2, int(self.y)))


class ParticleSystem:
    def __init__(self):
        self.particles: list[Particle] = []
        self.texts: list[FloatingText] = []

    def spawn_recycle(self, x: float, y: float, points: int, item_type: str):
        for _ in range(22):
            self.particles.append(Particle(x, y, item_type))
        color = (80, 220, 80) if item_type == "organic" else (100, 180, 255)
        self.texts.append(FloatingText(x, y - 24, f"+{points}", color))

    def spawn_miss(self, x: float, y: float):
        for _ in range(10):
            self.particles.append(Particle(x, y, "inorganic"))
        self.texts.append(FloatingText(x, y - 20, "¡Vida perdida!", (220, 50, 50)))

    def update(self, dt: int):
        for p in self.particles:
            p.update(dt)
        for t in self.texts:
            t.update(dt)
        self.particles = [p for p in self.particles if p.alive]
        self.texts     = [t for t in self.texts if t.alive]

    def draw(self, surface: pygame.Surface):
        for p in self.particles:
            p.draw(surface)
        for t in self.texts:
            t.draw(surface)
