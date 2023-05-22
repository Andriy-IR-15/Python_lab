"""
Модуль, що містить клас WineFridge для представлення холодильника для вина.
"""

from models.fridge import Fridge


class WineFridge(Fridge):
    """
    Клас, що представляє холодильник для вина.
    """

    def __init__(self, max_bottle_count, max_bottle_volume):
        """
        Ініціалізує об'єкт холодильника для вина.

        :param max_bottle_count: Максимальна кількість пляшок.
        :param max_bottle_volume: Максимальний об'єм пляшок.
        """
        self.max_bottle_count = max_bottle_count
        self.max_bottle_volume = max_bottle_volume

    def get_max_usable_capacity(self):
        """
        Отримати максимальну корисну ємність холодильника для вина.

        :return: Максимальна корисна ємність холодильника для вина.
        """
        return self.max_bottle_count * self.max_bottle_volume

    def __str__(self):
        """
        Повертає рядок, що представляє холодильник для вина.

        :return: Рядок, що представляє холодильник для вина.
        """
        return f"Wine Fridge (Max Bottle Count: {self.max_bottle_count}, " \
               f"Max Bottle Volume: {self.max_bottle_volume}, " \
               f"Max Usable Capacity: {self.get_max_usable_capacity()})"
