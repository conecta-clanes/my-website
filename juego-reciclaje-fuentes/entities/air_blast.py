import pygame
from settings import BLOW_SPEED, BLOW_RADIUS, BLOW_LIFETIME


class AirBlast:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BLOW_RADIUS
        self.lifetime = float(BLOW_LIFETIME)
        self.max_life = float(BLOW_LIFETIME)
        self.alive = True

    def update(self, dt):
        self.y -= BLOW_SPEED
        self.lifetime -= dt
        if self.lifetime <= 0 or self.y < -self.radius:
            self.alive = False

    def draw(self, surface):
        if not self.alive:
            return
        ratio = self.lifetime / self.max_life
        alpha = int(220 * ratio)
        r = self.radius
        size = r * 2 + 4
        surf = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(surf, (180, 230, 255, alpha),         (size // 2, size // 2), r)
        pygame.draw.circle(surf, (255, 255, 255, int(alpha * 0.5)), (size // 2, size // 2), r // 2)
        surface.blit(surf, (int(self.x) - size // 2, int(self.y) - size // 2))
