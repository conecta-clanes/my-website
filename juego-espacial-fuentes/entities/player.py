import pygame
from settings import WIDTH, HEIGHT, PLAYER_RADIUS, SHOOT_COOLDOWN, INVULNERABLE_TIME
from entities.bullet import Bullet


class Player:
    def __init__(self, screen_w, screen_h):
        self.x = screen_w / 2
        self.y = screen_h / 2
        self.target_x = self.x
        self.target_y = self.y
        self.radius = PLAYER_RADIUS
        self.shoot_timer = 0
        self.invulnerable = 0
        self.alive = True

        from utils import load_transparent
        self.image = load_transparent("assets/player-ship-sprite.png", (self.radius * 2, self.radius * 2))

    def set_target(self, x, y):
        self.target_x = x
        self.target_y = y

    def update(self, dt, bullets):
        if not self.alive:
            return

        # Smooth follow of face position
        self.x += (self.target_x - self.x) * 0.12
        self.y += (self.target_y - self.y) * 0.12

        # Clamp to screen
        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

        self.shoot_timer -= dt
        if self.invulnerable > 0:
            self.invulnerable -= dt

        # Auto-shoot to the right
        if self.shoot_timer <= 0:
            self.shoot_timer = SHOOT_COOLDOWN
            bullets.append(Bullet(self.x + self.radius, self.y, 1, 0))

    def draw(self, surface):
        if not self.alive:
            return
        if self.invulnerable > 0 and (int(self.invulnerable) // 100) % 2 == 0:
            return
        rect = self.image.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(self.image, rect)
