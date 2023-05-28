class FridgeManager:
    def __init__(self):
        self.fridges = []

    def add_fridge(self, fridge):
        self.fridges.append(fridge)

    def search_by_max_usable_capacity(self, capacity):
        return [fridge for fridge in self.fridges if fridge.get_max_usable_capacity() >= capacity]

    def search_by_class(self, fridge_class):
        return [fridge for fridge in self.fridges if isinstance(fridge, fridge_class)]

    def __str__(self):
        return "Fridge Manager"

    def __len__(self):
        return len(self.fridges)

    def __getitem__(self, index):
        return self.fridges[index]

    def __iter__(self):
        return iter(self.fridges)

    def do_something_for_all(self):
        return [fridge.do_something() for fridge in self.fridges]

    def get_object_with_index(self):
        return [(index, fridge) for index, fridge in enumerate(self.fridges)]

    def get_object_with_do_something(self):
        return [(fridge, fridge.do_something()) for fridge in self.fridges]

    def get_object_with_index_and_do_something(self):
        return [(index, fridge, fridge.do_something()) for index, fridge in enumerate(self.fridges)]

    def get_attributes_by_type(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    def check_conditions(self, condition):
        return {
            "all": all(condition(fridge) for fridge in self.fridges),
            "any": any(condition(fridge) for fridge in self.fridges)
        }
