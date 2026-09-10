import pygame
from settings import WIDTH, HEIGHT, BLACK, WHITE, YELLOW, CYAN


class MenuScene:
    def __init__(self, screen, last_recording=None, record=True):
        self.screen = screen
        self.last_recording = last_recording
        self.record = record
        self.font_title = pygame.font.SysFont("Arial", 64, bold=True)
        self.font_sub   = pygame.font.SysFont("Arial", 24)
        self.font_small = pygame.font.SysFont("Arial", 18)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            from scenes.game_scene import GameScene
            return GameScene(self.screen, record=self.record)
        return self

    def draw(self):
        self.screen.fill(BLACK)

        title = self.font_title.render("JUEGO ESPACIAL", True, CYAN)
        self.screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 110)))

        start = self.font_sub.render("Presiona ENTER o ESPACIO para jugar", True, YELLOW)
        self.screen.blit(start, start.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30)))

        instructions = [
            ("Control:",   "tu rostro mueve la nave — ¡mira a la cámara!"),
            ("Disparo:",   "automático hacia los enemigos"),
            ("Terminar:",  "presiona  C  o  ESC  (o cierra la ventana)"),
        ]
        y = HEIGHT // 2 + 18
        for label, desc in instructions:
            lbl = self.font_small.render(label, True, (180, 180, 180))
            dsc = self.font_small.render(desc,  True, WHITE)
            row_w = lbl.get_width() + 10 + dsc.get_width()
            x0 = WIDTH // 2 - row_w // 2
            self.screen.blit(lbl, (x0, y))
            self.screen.blit(dsc, (x0 + lbl.get_width() + 10, y))
            y += 24

        if self.last_recording:
            saved = self.font_small.render(
                f"Grabación guardada: {self.last_recording}", True, (100, 220, 100)
            )
            self.screen.blit(saved, saved.get_rect(center=(WIDTH // 2, HEIGHT - 28)))
