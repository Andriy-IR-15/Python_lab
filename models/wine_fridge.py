# wine_fridge.py
from models.fridge import Fridge


class WineFridge(Fridge):
    def __init__(self, max_bottle_count, max_bottle_volume):
        self.max_bottle_count = max_bottle_count
        self.max_bottle_volume = max_bottle_volume

    def get_max_usable_capacity(self):
        return self.max_bottle_count * self.max_bottle_volume

    def __str__(self):
        return f"Wine Fridge (Max Bottle Count: {self.max_bottle_count}, Max Bottle Volume: {self.max_bottle_volume}, Max Usable Capacity: {self.get_max_usable_capacity()})"
