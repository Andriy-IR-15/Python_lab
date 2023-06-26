from models.fridge import Fridge
import logging


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.error(str(e))
                elif mode == "file":
                    logging.basicConfig(filename='log.txt', level=logging.ERROR)
                    logging.error(str(e))
                else:
                    logging.error(f"Invalid logging mode: {mode}")
        return wrapper
    return decorator


class TemperatureOutOfRange(Exception):
    pass


class Freezer(Fridge):
    def __init__(self):
        super().__init__()
        self.favorite_food_set = {"worms", "grain"}

    @staticmethod
    def get_temperature():
        return -20

    @staticmethod
    def method1():
        print("Freezer Maximum temperature: -15 degrees")

    @staticmethod
    def method2():
        print("Freezer Minimum temperature: -2 degrees")

    @staticmethod
    def check_temperature(temperature):
        min_temperature = -15
        max_temperature = -2
        if temperature < min_temperature or temperature > max_temperature:
            raise TemperatureOutOfRange("Temperature is out of range!")

    @logged(TemperatureOutOfRange, "console")
    def do_something(self, temperature=None):
        if temperature is None:
            temperature = int(input("Enter the temperature: "))
        try:
            self.check_temperature(temperature)
            return "Doing something in Freezer"
        except TemperatureOutOfRange as e:
            print(f"Error: {e}")
            return None

    def get_max_usable_capacity(self):
        return 48

    def __str__(self):
        return f"Freezer (Temperature: {self.get_temperature()}, Max Usable Capacity: {self.get_max_usable_capacity()})"
