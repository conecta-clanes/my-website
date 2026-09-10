import pygame
from settings import WHITE, RED


class HUD:
    def __init__(self, screen):
        self.screen = screen
        self.font_label = pygame.font.SysFont("Arial", 22, bold=True)
        self.font_num = pygame.font.SysFont("Arial", 22, bold=True)
        self.font_small = pygame.font.SysFont("Arial", 18)

    def draw(self, score, lives, wave):
        # "score [badge]" top-left
        label = self.font_label.render("score", True, WHITE)
        num_surf = self.font_num.render(str(score), True, WHITE)

        pad_x, pad_y = 10, 6
        badge_w = num_surf.get_width() + pad_x * 2
        badge_h = num_surf.get_height() + pad_y

        lx, ly = 10, 12
        self.screen.blit(label, (lx, ly))

        bx = lx + label.get_width() + 8
        by = ly - 2
        pygame.draw.rect(self.screen, (220, 110, 0),
                         (bx, by, badge_w, badge_h), border_radius=10)
        self.screen.blit(num_surf, (bx + pad_x, by + pad_y // 2))

        # Wave — centered top
        wave_surf = self.font_small.render(f"Wave {wave}", True, (220, 220, 220))
        cx = self.screen.get_width() // 2 - wave_surf.get_width() // 2
        self.screen.blit(wave_surf, (cx, 14))

        # Lives — top right
        hearts = "♥ " * lives
        lives_surf = self.font_label.render(hearts, True, RED)
        rx = self.screen.get_width() - lives_surf.get_width() - 10
        self.screen.blit(lives_surf, (rx, 12))
