from abc import ABC, abstractmethod


class Fridge(ABC):
    def __init__(self):
        self.favorite_food_set = set()

    @abstractmethod
    def get_max_usable_capacity(self):
        pass

    @abstractmethod
    def do_something(self):
        return "Doing something in VegetableFridge"

    def __iter__(self):
        return iter(self.favorite_food_set)
