import random
from settings import WIDTH, HEIGHT, BASE_WAVE_COUNTS, WAVE_INCREMENT
from entities.enemy import Enemy


class Spawner:
    def __init__(self):
        self.wave = 0
        self.enemies = []

    def next_wave(self):
        self.wave += 1
        self.enemies = []
        offset = 0
        for size in ('large', 'medium', 'small'):
            count = BASE_WAVE_COUNTS[size] + (self.wave - 1) * WAVE_INCREMENT[size]
            for i in range(count):
                x = WIDTH + 60 + offset + i * 80
                y = random.randint(60, HEIGHT - 60)
                self.enemies.append(Enemy(size, x, y))
            offset += count * 80 + 60
        return self.enemies

    def all_dead(self):
        return all(not e.alive for e in self.enemies)
