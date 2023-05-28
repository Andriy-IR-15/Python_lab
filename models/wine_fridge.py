from models.fridge import Fridge


def create_result_file(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, 'a') as file:
                file.write(str(result) + '\n')
            return result
        return wrapper
    return decorator


class WineFridge(Fridge):
    def __init__(self, number_of_bottles, bottle_capacity):
        super().__init__()
        self.number_of_bottles = number_of_bottles
        self.bottle_capacity = bottle_capacity

    @create_result_file('get_max_usable_capacity.txt')
    def get_max_usable_capacity(self):
        return self.number_of_bottles * self.bottle_capacity

    def do_something(self):
        return "Doing something in WineFridge"

    def __str__(self):
        return f"Wine Fridge (Number of Bottles: {self.number_of_bottles}, Max Usable Capacity: {self.get_max_usable_capacity()})"
