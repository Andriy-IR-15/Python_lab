class Fridge:
    instance = None

    def __init__(self, brand="", model="", capacity=23, is_defrosting=True, energy_efficiency_class="A"):
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.is_defrosting = is_defrosting
        self.energy_efficiency_class = energy_efficiency_class

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = Fridge()
        return cls.instance

    def turn_on_defrosting(self):
        self.is_defrosting = True

    def turn_off_defrosting(self):
        self.is_defrosting = False

    def delete_model_info(self):
        self.model = None


fridge_array = [
    Fridge("Samsung", "RT21M63SG", 23, False, "A"),
]

for fridge in fridge_array:
    print(vars(fridge))
