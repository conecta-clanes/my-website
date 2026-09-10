import pygame
from PIL import Image


def load_transparent(path, size):
    """Load a pre-processed sprite (already has correct alpha) and resize."""
    img = Image.open(path).convert("RGBA")
    img = img.resize(size, Image.LANCZOS)
    return pygame.image.fromstring(img.tobytes(), img.size, "RGBA").convert_alpha()
