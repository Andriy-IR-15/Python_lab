"""
Модуль, що містить абстрактний клас Fridge для представлення холодильника.
"""

from abc import ABC, abstractmethod


class Fridge(ABC):
    """
    Абстрактний клас, що представляє холодильник.
    """

    @abstractmethod
    def get_max_usable_capacity(self):
        """
        Абстрактний метод для отримання максимальної корисної ємності холодильника.
        """
        pass
