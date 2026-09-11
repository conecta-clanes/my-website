import random
from settings import (
    WASTE_ITEMS,
    SPAWN_INTERVAL_START,
    SPAWN_INTERVAL_MIN,
    ITEM_SPEED_START,
    ITEM_SPEED_MAX,
)
from entities.waste_item import WasteItem


class Spawner:
    def __init__(self):
        self._timer = 0.0
        self._interval = float(SPAWN_INTERVAL_START)
        self._count = 0

    def update(self, dt: int):
        self._timer += dt
        if self._timer < self._interval:
            return None

        self._timer = 0.0
        self._count += 1

        # Dificultad progresiva: interval decrece, speed aumenta
        progress = min(self._count / 30, 1.0)
        self._interval = SPAWN_INTERVAL_MIN + (1 - progress) * (
            SPAWN_INTERVAL_START - SPAWN_INTERVAL_MIN
        )
        speed = ITEM_SPEED_START + progress * (ITEM_SPEED_MAX - ITEM_SPEED_START)

        data = random.choice(WASTE_ITEMS)
        return WasteItem(data["image"], data["type"], data["points"], speed)
