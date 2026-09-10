import pygame
import math
import random
from settings import WIDTH, HEIGHT, ENEMY_DATA


class Enemy:
    SPRITES = {}

    @classmethod
    def load_sprites(cls):
        from utils import load_transparent
        target_sizes = {
            'large':  (152, 152),
            'medium': (104, 104),
            'small':  (64,  64),
        }
        for name, dims in target_sizes.items():
            cls.SPRITES[name] = load_transparent(f"assets/enemy-ship-{name}-sprite.png", dims)

    def __init__(self, size_name, x=None, y=None):
        data = ENEMY_DATA[size_name]
        self.size = size_name
        self.hp = data['hp']
        self.speed = data['speed']
        self.points = data['points']
        self.radius = data['radius']
        self.amplitude = data['amplitude']
        self.freq = data['freq']
        self.alive = True

        self.x = x if x is not None else random.randint(WIDTH + 40, WIDTH + 200)
        self.y = y if y is not None else random.randint(60, HEIGHT - 60)
        self.base_y = self.y
        self.time = random.uniform(0, math.pi * 2)

        self.image = self.SPRITES.get(size_name)

    def update(self, dt):
        self.time += self.freq * dt / 1000.0
        self.x -= self.speed
        self.y = self.base_y + math.sin(self.time) * self.amplitude
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

        # Wrap: when leaving left, re-enter from right
        if self.x < -self.radius:
            self.x = WIDTH + self.radius
            self.base_y = random.randint(60, HEIGHT - 60)

    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.alive = False
            return True
        return False

    def draw(self, surface):
        if self.image:
            rect = self.image.get_rect(center=(int(self.x), int(self.y)))
            surface.blit(self.image, rect)
        else:
            colors = {'large': (255, 50, 50), 'medium': (255, 150, 50), 'small': (255, 200, 50)}
            pygame.draw.circle(surface, colors[self.size], (int(self.x), int(self.y)), self.radius)
