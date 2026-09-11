import math
import pygame
from settings import WHITE, RED, ORANGE, PLAYER_LIVES


class HUD:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font_label = pygame.font.SysFont("Arial", 22, bold=True)
        self.font_num   = pygame.font.SysFont("Arial", 22, bold=True)

    @staticmethod
    def _draw_heart(surface: pygame.Surface, color: tuple, cx: int, cy: int, size: int):
        points = []
        for deg in range(0, 360, 6):
            t = math.radians(deg)
            x = size * (16 * math.sin(t) ** 3) / 16
            y = -size * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) / 16
            points.append((cx + x, cy + y))
        pygame.draw.polygon(surface, color, points)

    def draw(self, score: int, lives: int):
        # Score — esquina superior izquierda
        label    = self.font_label.render("score", True, WHITE)
        num_surf = self.font_num.render(str(score), True, WHITE)

        pad_x, pad_y = 10, 6
        badge_w = num_surf.get_width() + pad_x * 2
        badge_h = num_surf.get_height() + pad_y

        lx, ly = 10, 12
        self.screen.blit(label, (lx, ly))

        bx = lx + label.get_width() + 8
        by = ly - 2
        pygame.draw.rect(self.screen, ORANGE, (bx, by, badge_w, badge_h), border_radius=10)
        self.screen.blit(num_surf, (bx + pad_x, by + pad_y // 2))

        # Vidas — esquina superior derecha: posiciones fijas, corazón lleno/vacío
        heart_size = 13
        gap = 8
        total_w = PLAYER_LIVES * (heart_size * 2 + gap) - gap
        sx = self.screen.get_width() - total_w - 10
        cy = 22

        for i in range(PLAYER_LIVES):
            cx = sx + i * (heart_size * 2 + gap) + heart_size
            if i < lives:
                self._draw_heart(self.screen, RED, cx, cy, heart_size)
                # Brillo interior
                self._draw_heart(self.screen, (255, 120, 120), cx - 3, cy - 3, heart_size // 3)
            else:
                self._draw_heart(self.screen, (60, 20, 20), cx, cy, heart_size)
