import pygame
import random
import cv2
import numpy as np
from settings import WIDTH, HEIGHT, PLAYER_LIVES
from entities.player import Player
from entities.enemy import Enemy
from systems.collision import check_player_enemy
from systems.spawner import Spawner
from systems.hud import HUD
from systems.particles import ParticleSystem
from systems.recorder import Recorder
from systems.audio import AudioManager


def _build_space_overlay(width, height):
    surf = pygame.Surface((width, height), pygame.SRCALPHA)

    nebula_palette = [
        (80,  30, 180, 40),
        (30,  90, 200, 35),
        (180, 50,  80, 30),
        (50, 180, 130, 32),
        (120, 60, 200, 28),
    ]
    for _ in range(7):
        cx = random.randint(0, width)
        cy = random.randint(0, height)
        color = random.choice(nebula_palette)
        for _ in range(5):
            r  = random.randint(45, 110)
            ox = random.randint(-50, 50)
            oy = random.randint(-50, 50)
            blob = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
            pygame.draw.circle(blob, color, (r, r), r)
            surf.blit(blob, (cx + ox - r, cy + oy - r))

    for _ in range(180):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.choices([1, 2, 3], weights=[60, 30, 10])[0]
        b = random.randint(170, 255)
        tint = random.choices(
            [(b, b, b), (b, b, int(b * 0.65)), (int(b * 0.65), int(b * 0.65), b)],
            weights=[50, 25, 25]
        )[0]
        pygame.draw.circle(surf, (*tint, b), (x, y), r)

    return surf


class GameScene:
    def __init__(self, screen, record=True):
        self.screen = screen
        Enemy.load_sprites()
        self.hud = HUD(screen)
        self.space_overlay = _build_space_overlay(WIDTH, HEIGHT)

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
        self.bullets = []
        self.score = [0]
        self.lives = PLAYER_LIVES
        self.spawner = Spawner()
        self.enemies = self.spawner.next_wave()
        self.particles = ParticleSystem()
        self.respawn_timer = 0
        self.game_over = False

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

    def update(self, dt):
        # C or ESC = end session at any moment
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c] or keys[pygame.K_ESCAPE]:
            return self._stop_and_go_menu()

        if self.game_over:
            if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                self._reset()
            return self

        self._webcam_surf = self._read_webcam()
        self.player.set_target(*self._last_face)

        if self.respawn_timer > 0:
            self.respawn_timer -= dt
            if self.respawn_timer <= 0:
                self.player.alive = True
                self.player.x = WIDTH / 2
                self.player.y = HEIGHT / 2
        else:
            prev_bullets = len(self.bullets)
            self.player.update(dt, self.bullets)
            if len(self.bullets) > prev_bullets:
                self.audio.play_shoot()
                if self.recorder:
                    self.recorder.log_sfx("shoot")

        for bullet in self.bullets:
            bullet.update(dt, WIDTH, HEIGHT)
        self.bullets = [b for b in self.bullets if b.alive]

        for enemy in self.enemies:
            enemy.update(dt)

        for bullet in self.bullets:
            if not bullet.alive:
                continue
            for enemy in self.enemies:
                if not enemy.alive:
                    continue
                dist_sq = (bullet.x - enemy.x) ** 2 + (bullet.y - enemy.y) ** 2
                if dist_sq < (bullet.radius + enemy.radius) ** 2:
                    bullet.alive = False
                    if enemy.hit():
                        self.score[0] += enemy.points
                        self.particles.spawn_explosion(enemy.x, enemy.y)
                        self.audio.play_explosion()
                        if self.recorder:
                            self.recorder.log_sfx("explosion")

        if check_player_enemy(self.player, self.enemies):
            self.player.invulnerable = 2000
            self.lives -= 1
            self.particles.spawn_explosion(self.player.x, self.player.y, 10)
            self.audio.play_explosion()
            if self.recorder:
                self.recorder.log_sfx("explosion")
            if self.lives <= 0:
                self.lives = 0
                self.player.alive = False
                self.game_over = True
            else:
                self.player.alive = False
                self.respawn_timer = 2000

        self.enemies = [e for e in self.enemies if e.alive]
        if not self.enemies:
            self.enemies = self.spawner.next_wave()

        self.particles.update(dt)
        return self

    def draw(self, dt):
        if self._webcam_surf:
            self.screen.blit(self._webcam_surf, (0, 0))
        else:
            self.screen.fill((20, 30, 50))

        self.screen.blit(self.space_overlay, (0, 0))

        for bullet in self.bullets:
            bullet.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        self.player.draw(self.screen)
        self.particles.draw(self.screen)
        self.hud.draw(self.score[0], self.lives, self.spawner.wave)
        if self.game_over:
            self._draw_game_over()
        if self.recorder:
            self.recorder.draw_indicator(self.screen, dt)
            self.recorder.capture(self.screen)

    def _draw_game_over(self):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        self.screen.blit(overlay, (0, 0))

        font_big = pygame.font.SysFont("Arial", 64, bold=True)
        font_med = pygame.font.SysFont("Arial", 30)
        font_sml = pygame.font.SysFont("Arial", 22)

        cx = WIDTH // 2
        go   = font_big.render("JUEGO TERMINADO", True, (220, 50, 50))
        sc   = font_med.render(f"Puntaje: {self.score[0]}", True, (255, 220, 0))
        wave = font_sml.render(f"Wave alcanzada: {self.spawner.wave}", True, (180, 180, 255))
        rst  = font_med.render("Presiona ENTER para reiniciar", True, (200, 200, 200))

        self.screen.blit(go,   go.get_rect(center=(cx, HEIGHT // 2 - 80)))
        self.screen.blit(sc,   sc.get_rect(center=(cx, HEIGHT // 2 - 10)))
        self.screen.blit(wave, wave.get_rect(center=(cx, HEIGHT // 2 + 30)))
        self.screen.blit(rst,  rst.get_rect(center=(cx, HEIGHT // 2 + 80)))

    def __del__(self):
        if hasattr(self, "recorder") and self.recorder:
            self.recorder.stop()
        if hasattr(self, "cap") and self.cap.isOpened():
            self.cap.release()
