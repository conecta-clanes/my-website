import os
import cv2
import pygame
from datetime import datetime


class Recorder:
    def __init__(self, width: int, height: int, fps: int = 60):
        os.makedirs("recordings", exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.filename = f"recordings/sesion_{ts}.mp4"

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self._writer = cv2.VideoWriter(self.filename, fourcc, fps, (width, height))
        self.active = True
        self._blink = 0

    def capture(self, surface: pygame.Surface):
        if not self.active:
            return
        frame = pygame.surfarray.array3d(surface).transpose(1, 0, 2)
        self._writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def stop(self) -> str:
        if not self.active:
            return self.filename
        self.active = False
        self._writer.release()
        return self.filename

    def draw_indicator(self, surface: pygame.Surface, dt: int):
        self._blink = (self._blink + dt) % 1000
        if self._blink < 500:
            w = surface.get_width()
            pygame.draw.circle(surface, (220, 30, 30), (w - 22, 52), 9)
            font = pygame.font.SysFont("Arial", 15, bold=True)
            surface.blit(font.render("REC", True, (220, 30, 30)), (w - 52, 45))
