import pygame
from settings import WIDTH, HEIGHT, BLACK, WHITE, YELLOW, GREEN


class MenuScene:
    def __init__(self, screen: pygame.Surface, last_recording: str = None, record: bool = False):
        self.screen = screen
        self.last_recording = last_recording
        self.record = record
        self.font_title = pygame.font.SysFont("Arial", 46, bold=True)
        self.font_sub   = pygame.font.SysFont("Arial", 24)
        self.font_small = pygame.font.SysFont("Arial", 18)

    def update(self, dt: int):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            from scenes.game_scene import GameScene
            return GameScene(self.screen, record=self.record)
        return self

    def draw(self):
        self.screen.fill((10, 45, 10))

        # Título
        title = self.font_title.render("GUARDIANES DEL RECICLAJE", True, GREEN)
        self.screen.blit(title, title.get_rect(center=(WIDTH // 2, 80)))

        subtitle = self.font_sub.render(
            "¡Sopla el aire para reciclar los desechos que caen!", True, YELLOW
        )
        self.screen.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 140)))

        start = self.font_sub.render("Presiona ENTER o ESPACIO para jugar", True, WHITE)
        self.screen.blit(start, start.get_rect(center=(WIDTH // 2, 185)))

        # Instrucciones
        instructions = [
            ("Control:",   "tu rostro mueve al guardián — ¡mira a la cámara!"),
            ("Soplar:",    "automático — el guardián dispara aire hacia arriba"),
            ("Reciclar:",  "posiciónate debajo de cada desecho para reciclarlo"),
            ("Orgánico:",  "manzana, plátano, cáscara de huevo  →  +10 pts"),
            ("Inorgánico:", "lata, botella, frasco  →  +15 pts"),
            ("Vidas:",     "3 vidas — se pierde una si un desecho llega al suelo"),
            ("Terminar:",  "presiona  C  o  ESC  para salir"),
        ]
        y = 235
        for label, desc in instructions:
            lbl = self.font_small.render(label, True, (140, 220, 140))
            dsc = self.font_small.render(desc,  True, WHITE)
            row_w = lbl.get_width() + 10 + dsc.get_width()
            x0 = WIDTH // 2 - row_w // 2
            self.screen.blit(lbl, (x0, y))
            self.screen.blit(dsc, (x0 + lbl.get_width() + 10, y))
            y += 27

        if self.record:
            rec_note = self.font_small.render(
                "Modo grabación activo — la sesión se guardará en recordings/", True, (220, 80, 80)
            )
            self.screen.blit(rec_note, rec_note.get_rect(center=(WIDTH // 2, y + 10)))

        if self.last_recording:
            saved = self.font_small.render(
                f"Grabación guardada: {self.last_recording}", True, (100, 220, 100)
            )
            self.screen.blit(saved, saved.get_rect(center=(WIDTH // 2, HEIGHT - 28)))
