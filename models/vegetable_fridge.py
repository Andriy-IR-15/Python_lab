# vegetable_fridge.py
from models.fridge import Fridge


class VegetableFridge(Fridge):
    def __init__(self, max_vegetable_count, max_vegetable_weight):
        self.max_vegetable_count = max_vegetable_count
        self.max_vegetable_weight = max_vegetable_weight

    def get_max_usable_capacity(self):
        return self.max_vegetable_count * self.max_vegetable_weight

    def __str__(self):
        return f"Vegetable Fridge (Max Vegetable Count: {self.max_vegetable_count}, Max Vegetable Weight: {self.max_vegetable_weight}, Max Usable Capacity: {self.get_max_usable_capacity()})"

