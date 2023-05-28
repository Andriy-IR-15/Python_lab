from models.fridge import Fridge


def method_calls_counter(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            global count
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
            except FileNotFoundError:
                lines = []

            method_name = func.__name__
            method_call = None
            for i, line in enumerate(lines):
                if line.startswith(f"{method_name}="):
                    method_call = line
                    count = int(line.split('=')[1].strip())
                    count += 1
                    lines[i] = f"{method_name}={count}\n"
                    break

            if not method_call:
                count = 1
                lines.append(f"{method_name}={count}\n")

            with open(file_path, 'w') as file:
                file.writelines(lines)

            print(f"Method called: {method_name} - Count: {count}")

            return func(*args, **kwargs)

        return wrapper

    return decorator


class FridgeCamera(Fridge):
    VOLUME_PER_KILOGRAM = 10

    def __init__(self, number_of_entries, tape_drive_type, sausage_movement_type, tape_speed, max_sausage_weight):
        super().__init__()
        self.number_of_entries = number_of_entries
        self.tape_drive_type = tape_drive_type
        self.sausage_movement_type = sausage_movement_type
        self.tape_speed = tape_speed
        self.max_sausage_weight = max_sausage_weight

    def do_something(self):
        return "Doing something in FridgeCamera"

    @method_calls_counter('text.txt')
    def get_max_usable_capacity(self):
        return self.max_sausage_weight * self.VOLUME_PER_KILOGRAM

    def __str__(self):
        return f"Fridge Camera (Number of Entries: {self.number_of_entries}, Max Usable Capacity: {self.get_max_usable_capacity()})"


class WineFridge(Fridge):
    def __init__(self, number_of_bottles, bottle_capacity):
        super().__init__()
        self.number_of_bottles = number_of_bottles
        self.bottle_capacity = bottle_capacity

    def get_max_usable_capacity(self):
        return self.number_of_bottles * self.bottle_capacity

    def do_something(self):
        return "Doing something in WineFridge"

    def __str__(self):
        return f"Wine Fridge (Number of Bottles: {self.number_of_bottles}, Max Usable Capacity: {self.get_max_usable_capacity()})"
