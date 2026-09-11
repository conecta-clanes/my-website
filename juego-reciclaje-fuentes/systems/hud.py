import pygame
from settings import WHITE, RED, ORANGE


class HUD:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font_label = pygame.font.SysFont("Arial", 22, bold=True)
        self.font_num   = pygame.font.SysFont("Arial", 22, bold=True)

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

        # Vidas — esquina superior derecha
        hearts     = "♥ " * lives
        lives_surf = self.font_label.render(hearts, True, RED)
        rx = self.screen.get_width() - lives_surf.get_width() - 10
        self.screen.blit(lives_surf, (rx, 12))
