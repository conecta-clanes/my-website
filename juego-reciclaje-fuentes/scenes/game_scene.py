import pygame
import cv2
from settings import WIDTH, HEIGHT, PLAYER_LIVES
from entities.player import Player
from systems.spawner import Spawner
from systems.collision import check_blasts_items
from systems.hud import HUD
from systems.particles import ParticleSystem
from systems.recorder import Recorder
from systems.audio import AudioManager


class GameScene:
    def __init__(self, screen: pygame.Surface, record: bool = False):
        self.screen = screen
        self.hud = HUD(screen)

        self.cap = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        self._last_face = (WIDTH * 0.5, HEIGHT * 0.5)
        self._detect_every = 3
        self._frame_count = 0
        self._webcam_surf = None

        self.recorder = Recorder(WIDTH, HEIGHT) if record else None
        self.audio = AudioManager()
        self._reset()

    def _reset(self):
        self.player = Player(WIDTH, HEIGHT)
        self.blasts = []
        self.items = []
        self.score = 0
        self.lives = PLAYER_LIVES
        self.spawner = Spawner()
        self.particles = ParticleSystem()
        self.game_over = False
        self._life_flash = 0

    def _stop_and_go_menu(self):
        filename = None
        if self.recorder:
            filename = self.recorder.filename
            self.recorder.stop()
        self.audio.stop()
        if self.cap.isOpened():
            self.cap.release()
        from scenes.menu_scene import MenuScene
        return MenuScene(self.screen, last_recording=filename, record=self.recorder is not None)

    def _read_webcam(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        frame = cv2.flip(frame, 1)

        self._frame_count += 1
        if self._frame_count % self._detect_every == 0:
            small = cv2.resize(frame, (320, 240))
            gray  = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(40, 40))
            if len(faces) > 0:
                fx, fy, fw, fh = faces[0]
                face_cx = (fx + fw / 2) / 320 * frame.shape[1]
                face_cy = (fy + fh / 2) / 240 * frame.shape[0]
                sx = face_cx / frame.shape[1] * WIDTH
                sy = face_cy / frame.shape[0] * HEIGHT
                self._last_face = (sx, sy)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_rgb = cv2.resize(frame_rgb, (WIDTH, HEIGHT))
        return pygame.surfarray.make_surface(frame_rgb.transpose(1, 0, 2))

    def update(self, dt: int):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c] or keys[pygame.K_ESCAPE]:
            return self._stop_and_go_menu()

        if self.game_over:
            if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                self._reset()
            return self

        self._webcam_surf = self._read_webcam()
        self.player.set_target(*self._last_face)
        prev_blasts = len(self.blasts)
        self.player.update(dt, self.blasts)
        if len(self.blasts) > prev_blasts:
            self.audio.play_blow()

        for blast in self.blasts:
            blast.update(dt)
        self.blasts = [b for b in self.blasts if b.alive]

        new_item = self.spawner.update(dt)
        if new_item:
            self.items.append(new_item)

        for item in self.items:
            item.update(dt, HEIGHT)

        # Colisión aire → desecho
        hits = check_blasts_items(self.blasts, self.items)
        for blast, item in hits:
            if not blast.alive or not item.alive:
                continue
            blast.alive = False
            pts = item.recycle()
            self.score += pts
            self.particles.spawn_recycle(item.x, item.y, pts, item.item_type)
            self.audio.play_recycle(item.item_type)

        # Desechos que llegaron al suelo sin ser reciclados
        for item in self.items:
            if not item.alive and item.reached_bottom:
                self.lives -= 1
                self.particles.spawn_miss(item.x, HEIGHT - 20)
                self.audio.play_miss()
                self._life_flash = 500
                if self.lives <= 0:
                    self.lives = 0
                    self.game_over = True

        self.items = [i for i in self.items if i.alive]

        if self._life_flash > 0:
            self._life_flash -= dt

        self.particles.update(dt)
        return self

    def draw(self, dt: int):
        if self._webcam_surf:
            self.screen.blit(self._webcam_surf, (0, 0))
        else:
            self.screen.fill((10, 45, 10))

        # Flash rojo al perder vida
        if self._life_flash > 0:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            alpha = int(110 * self._life_flash / 500)
            overlay.fill((220, 30, 30, alpha))
            self.screen.blit(overlay, (0, 0))

        for item in self.items:
            item.draw(self.screen)
        for blast in self.blasts:
            blast.draw(self.screen)
        self.player.draw(self.screen)
        self.particles.draw(self.screen)
        self.hud.draw(self.score, self.lives)

        if self.game_over:
            self._draw_game_over()
        if self.recorder:
            self.recorder.draw_indicator(self.screen, dt)
            self.recorder.capture(self.screen)

    def _draw_game_over(self):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        font_big = pygame.font.SysFont("Arial", 56, bold=True)
        font_med = pygame.font.SysFont("Arial", 30)
        font_sml = pygame.font.SysFont("Arial", 22)

        cx = WIDTH // 2
        go  = font_big.render("JUEGO TERMINADO", True, (220, 50, 50))
        sc  = font_med.render(f"Puntaje final: {self.score}", True, (255, 220, 0))
        rst = font_sml.render("Presiona ENTER para reiniciar", True, (200, 200, 200))

        self.screen.blit(go,  go.get_rect(center=(cx, HEIGHT // 2 - 70)))
        self.screen.blit(sc,  sc.get_rect(center=(cx, HEIGHT // 2 + 0)))
        self.screen.blit(rst, rst.get_rect(center=(cx, HEIGHT // 2 + 60)))

    def __del__(self):
        if hasattr(self, "recorder") and self.recorder:
            self.recorder.stop()
        if hasattr(self, "cap") and self.cap.isOpened():
            self.cap.release()
