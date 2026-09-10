import pygame
import math
import random


class Particle:
    def __init__(self, x, y):
        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 7)
        self.x = x
        self.y = y
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.lifetime = random.randint(300, 600)
        self.max_life = self.lifetime
        self.radius = random.randint(2, 5)
        self.color = random.choice([
            (255, 180, 0), (255, 120, 0), (255, 220, 50), (255, 80, 0)
        ])

    def update(self, dt):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.08
        self.vx *= 0.96
        self.vy *= 0.96
        self.lifetime -= dt

    @property
    def alive(self):
        return self.lifetime > 0

    def draw(self, surface):
        r = max(1, int(self.radius * self.lifetime / self.max_life))
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), r)


class ParticleSystem:
    def __init__(self):
        self.particles = []

    def spawn_explosion(self, x, y, count=18):
        for _ in range(count):
            self.particles.append(Particle(x, y))

    def update(self, dt):
        for p in self.particles:
            p.update(dt)
        self.particles = [p for p in self.particles if p.alive]

    def draw(self, surface):
        for p in self.particles:
            p.draw(surface)
