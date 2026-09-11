import pygame
import random
from settings import WIDTH, ITEM_RADIUS


class WasteItem:
    _fonts: dict = {}

    @classmethod
    def _font(cls, size: int):
        if size not in cls._fonts:
            cls._fonts[size] = pygame.font.SysFont("Arial", size, bold=True)
        return cls._fonts[size]

    def __init__(self, image_path: str, item_type: str, points: int, speed: float):
        self.radius = ITEM_RADIUS
        self.x = float(random.randint(self.radius, WIDTH - self.radius))
        self.y = float(-self.radius)
        self.item_type = item_type
        self.points = points
        self.speed = speed
        self.alive = True
        self.reached_bottom = False

        from utils import load_transparent
        self.image = load_transparent(image_path, (self.radius * 2, self.radius * 2))

    def update(self, dt: int, screen_height: int):
        self.y += self.speed
        if self.y > screen_height + self.radius:
            self.alive = False
            self.reached_bottom = True

    def recycle(self) -> int:
        self.alive = False
        return self.points

    def draw(self, surface: pygame.Surface):
        if not self.alive:
            return
        rect = self.image.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(self.image, rect)

        # Colored type label below the item
        color   = (80, 220, 80) if self.item_type == "organic" else (100, 180, 255)
        label   = "orgánico" if self.item_type == "organic" else "inorgánico"
        lbl = self._font(11).render(label, True, color)
        lx = int(self.x) - lbl.get_width() // 2
        ly = int(self.y) + self.radius + 2
        surface.blit(lbl, (lx, ly))
