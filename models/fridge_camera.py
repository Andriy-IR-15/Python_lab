from models.freezer import TemperatureOutOfRange, logged
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
        self.fridges = []

    @staticmethod
    def check_temperature(temperature):
        min_temperature = -15
        max_temperature = -2
        if temperature < min_temperature or temperature > max_temperature:
            raise TemperatureOutOfRange("Temperature is out of range!")

    @logged(TemperatureOutOfRange, "console")
    def do_something(self, temperature):
        try:
            self.check_temperature(temperature)
            return "Doing something in FridgeCamera"
        except TemperatureOutOfRange as e:
            print(f"Error: {e}")
            return None

    @method_calls_counter('text.txt')
    def get_max_usable_capacity(self):
        return self.max_sausage_weight * self.VOLUME_PER_KILOGRAM

    def __str__(self):
        return f"Fridge Camera (Number of Entries: {self.number_of_entries}, Max Usable Capacity: {self.get_max_usable_capacity()})"

    def add_fridge(self, fridge):
        self.fridges.append(fridge)

    def do_something_for_all(self, temperature=None):
        return [fridge.do_something(temperature) for fridge in self.fridges]
