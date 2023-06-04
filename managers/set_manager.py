class SM:
    def __init__(self, rm):
        self.rm = rm

    def __iter__(self):
        for fridge in self.rm:
            for food in fridge:
                yield food

    def __len__(self):
        return sum(len(fridge.favorite_food_set) for fridge in self.rm)

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")

        for fridge in self.rm:
            if index < len(fridge.favorite_food_set):
                return list(fridge.favorite_food_set)[index]
            else:
                index -= len(fridge.favorite_food_set)

    def __next__(self):
        for fridge in self.rm:
            for food in fridge:
                return food
        raise StopIteration()
