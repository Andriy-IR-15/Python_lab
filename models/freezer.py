# freezer.py
from models.fridge import Fridge


class Freezer(Fridge):
    @staticmethod
    def get_temperature():
        return -20

    @staticmethod
    def method1():
        print("Freezer Maximum temperature: -15 degrees")

    @staticmethod
    def method2():
        print("Freezer Minimum temperature: -2 degrees")

    def get_max_usable_capacity(self):
        return 48

    def __str__(self):
        return f"Freezer (Temperature: {self.get_temperature()}, Max Usable Capacity: {self.get_max_usable_capacity()})"

