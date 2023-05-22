"""
Модуль, що містить клас VegetableFridge для представлення холодильника для овочів.
"""

from models.fridge import Fridge


class VegetableFridge(Fridge):
    """
    Клас, що представляє холодильник для овочів.
    """

    def __init__(self, max_vegetable_count, max_vegetable_weight):
        """
        Ініціалізує об'єкт холодильника для овочів.

        :param max_vegetable_count: Максимальна кількість овочів.
        :param max_vegetable_weight: Максимальна вага овочів.
        """
        self.max_vegetable_count = max_vegetable_count
        self.max_vegetable_weight = max_vegetable_weight

    def get_max_usable_capacity(self):
        """
        Отримати максимальну корисну ємність холодильника для овочів.

        :return: Максимальна корисна ємність холодильника для овочів.
        """
        return self.max_vegetable_count * self.max_vegetable_weight

    def __str__(self):
        """
        Повертає рядок, що представляє холодильник для овочів.

        :return: Рядок, що представляє холодильник для овочів.
        """
        return f"Vegetable Fridge (Max Vegetable Count: {self.max_vegetable_count}, " \
               f"Max Vegetable Weight: {self.max_vegetable_weight}, " \
               f"Max Usable Capacity: {self.get_max_usable_capacity()})"
