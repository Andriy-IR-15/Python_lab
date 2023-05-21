from models.fridge import Fridge


class FridgeManager(Fridge):
    def __init__(self):
        self.fridges = []

    def add_fridge(self, fridge):
        self.fridges.append(fridge)

    def search_by_max_usable_capacity(self, capacity):
        return [fridge for fridge in self.fridges if fridge.get_max_usable_capacity() >= capacity]

    def search_by_class(self, fridge_class):
        return [fridge for fridge in self.fridges if isinstance(fridge, fridge_class)]

    def get_max_usable_capacity(self):
        return 0

    def __str__(self):
        return "Fridge Manager"
