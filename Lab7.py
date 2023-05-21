class Fridge:
    __instance = None

    def __init__(self, brand="", model="", capacity="", is_defrosting=False, energy_efficiency_class="A"):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.is_defrosting = is_defrosting
        self.energy_efficiency_class = energy_efficiency_class

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Fridge()
        return cls.__instance

    @staticmethod
    def turn_on_defrosting(self):
        self.is_defrosting = True

    def turn_off_defrosting(self):
        self.is_defrosting = False

    def delete_model_info(self):
        self.model = None


fridge_array = [
    Fridge("Samsung", "RT21M63SG", "23", False, "A"),
    Fridge("Xiaomi", "BM34G9KF", "18", True, "B")
]

if __name__ == '__main__':
    for fridge in fridge_array:
        print(vars(fridge))
