"""
Модуль, що містить клас FridgeCamera для представлення холодильника з камерою.
"""

from models.fridge import Fridge


class FridgeCamera(Fridge):
    """
    Клас, що представляє холодильник з камерою.
    """

    VOLUME_PER_KILOGRAM = 10

    def __init__(self, number_of_entries, tape_drive_type, sausage_movement_type,
                 tape_speed, max_sausage_weight):
        """
        Ініціалізує об'єкт холодильника з камерою.

        :param number_of_entries: Кількість входів в холодильник.
        :param tape_drive_type: Тип приводу стрічки.
        :param sausage_movement_type: Тип руху ковбаси.
        :param tape_speed: Швидкість руху стрічки.
        :param max_sausage_weight: Максимальна вага ковбаси.
        """
        self.number_of_entries = number_of_entries
        self.tape_drive_type = tape_drive_type
        self.sausage_movement_type = sausage_movement_type
        self.tape_speed = tape_speed
        self.max_sausage_weight = max_sausage_weight

    def get_max_usable_capacity(self):
        """
        Отримати максимальну корисну ємність холодильника з камерою.

        :return: Максимальна корисна ємність холодильника з камерою.
        """
        return self.max_sausage_weight * self.VOLUME_PER_KILOGRAM

    def __str__(self):
        """
        Повертає рядок, що представляє холодильник з камерою.

        :return: Рядок, що представляє холодильник з камерою.
        """
        return f"Fridge Camera (Number of Entries: {self.number_of_entries}, " \
               f"Max Usable Capacity: {self.get_max_usable_capacity()})"
