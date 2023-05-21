from abc import ABC, abstractmethod


class Fridge(ABC):
    @abstractmethod
    def get_max_usable_capacity(self):
        pass
