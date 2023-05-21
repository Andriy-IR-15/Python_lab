# fridge_camera.py
from models.fridge import Fridge


class FridgeCamera(Fridge):
    VOLUME_PER_KILOGRAM = 10

    def __init__(self, number_of_entries, tape_drive_type, sausage_movement_type, tape_speed, max_sausage_weight):
        self.number_of_entries = number_of_entries
        self.tape_drive_type = tape_drive_type
        self.sausage_movement_type = sausage_movement_type
        self.tape_speed = tape_speed
        self.max_sausage_weight = max_sausage_weight

    def get_max_usable_capacity(self):
        return self.max_sausage_weight * self.VOLUME_PER_KILOGRAM

    def __str__(self):
        return f"Fridge Camera (Number of Entries: {self.number_of_entries}, Max Usable Capacity: {self.get_max_usable_capacity()})"

