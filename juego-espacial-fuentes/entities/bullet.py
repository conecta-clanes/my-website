import pygame
from settings import BULLET_SPEED, BULLET_LIFETIME, BULLET_RADIUS, YELLOW


class Bullet:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.vx = dx * BULLET_SPEED
        self.vy = dy * BULLET_SPEED
        self.radius = BULLET_RADIUS
        self.lifetime = BULLET_LIFETIME
        self.alive = True

    def update(self, dt, width, height):
        self.x = (self.x + self.vx) % width
        self.y = (self.y + self.vy) % height
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.alive = False

    def draw(self, surface):
        pygame.draw.circle(surface, YELLOW, (int(self.x), int(self.y)), self.radius)
