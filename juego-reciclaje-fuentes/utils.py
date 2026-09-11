import pygame
from PIL import Image


def load_transparent(path, size):
    img = Image.open(path).convert("RGBA")
    img = img.resize(size, Image.LANCZOS)
    return pygame.image.fromstring(img.tobytes(), img.size, "RGBA").convert_alpha()
