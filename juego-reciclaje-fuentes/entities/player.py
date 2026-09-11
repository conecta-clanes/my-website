import pygame
from settings import WIDTH, HEIGHT, PLAYER_RADIUS, BLOW_COOLDOWN
from entities.air_blast import AirBlast


class Player:
    def __init__(self, screen_w: int, screen_h: int):
        self.x = float(screen_w / 2)
        self.y = float(screen_h / 2)
        self.target_x = self.x
        self.target_y = self.y
        self.radius = PLAYER_RADIUS
        self.blow_timer = 0
        self.invulnerable = 0
        self.alive = True

        from utils import load_transparent
        self.image = load_transparent(
            "assets/waste-guardian-air-blower.png",
            (self.radius * 2, self.radius * 2),
        )

    def set_target(self, x: float, y: float):
        self.target_x = x
        self.target_y = y

    def update(self, dt: int, blasts: list):
        if not self.alive:
            return

        self.x += (self.target_x - self.x) * 0.12
        self.y += (self.target_y - self.y) * 0.12
        self.x = max(self.radius, min(WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(HEIGHT - self.radius, self.y))

        self.blow_timer -= dt
        if self.invulnerable > 0:
            self.invulnerable -= dt

        if self.blow_timer <= 0:
            self.blow_timer = BLOW_COOLDOWN
            # Dispara hacia arriba desde la parte superior del personaje
            blasts.append(AirBlast(self.x, self.y - self.radius + 4))

    def draw(self, surface: pygame.Surface):
        if not self.alive:
            return
        # Parpadeo durante invulnerabilidad
        if self.invulnerable > 0 and (int(self.invulnerable) // 100) % 2 == 0:
            return
        rect = self.image.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(self.image, rect)
