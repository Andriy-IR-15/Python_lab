"""
Модуль, що містить клас FridgeManager для управління холодильниками.
"""

from models.fridge import Fridge


class FridgeManager(Fridge):
    """
    Клас, що представляє менеджер холодильників.
    """

    def __init__(self):
        self.fridges = []

    def add_fridge(self, fridge):
        """
        Додає холодильник до списку холодильників в FridgeManager.

        :param fridge: Холодильник, який слід додати.
        """
        self.fridges.append(fridge)

    def search_by_max_usable_capacity(self, capacity):
        """
        Пошук холодильників за максимальною корисною ємністю.

        :param capacity: Максимальна корисна ємність для пошуку.
        :return: Список холодильників, які мають максимальну корисну ємність, більшу або рівну вказаній ємності.
        """
        return [fridge for fridge in self.fridges if fridge.get_max_usable_capacity() >= capacity]

    def search_by_class(self, fridge_class):
        """
        Пошук холодильників за класом.

        :param fridge_class: Клас холодильника для пошуку.
        :return: Список холодильників, які належать до вказаного класу.
        """
        return [fridge for fridge in self.fridges if isinstance(fridge, fridge_class)]

    def get_max_usable_capacity(self):
        """
        Отримання максимальної корисної ємності FridgeManager.

        :return: Максимальна корисна ємність FridgeManager.
        """
        return 0

    def __str__(self):
        """
        Повертає рядок, що представляє FridgeManager.

        :return: Рядок, що представляє FridgeManager.
        """
        return "Менеджер холодильників"
