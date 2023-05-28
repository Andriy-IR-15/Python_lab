from models.fridge import Fridge


class VegetableFridge(Fridge):
    def __init__(self, number_of_drawers, drawer_capacity):
        super().__init__()
        self.number_of_drawers = number_of_drawers
        self.drawer_capacity = drawer_capacity

    def get_max_usable_capacity(self):
        return self.number_of_drawers * self.drawer_capacity

    def do_something(self):
        return "Doing something in VegetableFridge"

    def __str__(self):
        return f"Vegetable Fridge (Number of Drawers: {self.number_of_drawers}, Max Usable Capacity: {self.get_max_usable_capacity()})"

    def __iter__(self):
        return iter(self.favorite_food_set)
