from models.freezer import Freezer
from models.fridge_camera import FridgeCamera
from models.wine_fridge import WineFridge
from models.vegetable_fridge import VegetableFridge
from managers.fridge_manager import FridgeManager

if __name__ == "__main__":
    fridge_manager = FridgeManager()
    freezer1 = Freezer()
    freezer2 = Freezer()
    fridge_camera1 = FridgeCamera(2, "electric", "mechanical", 10, 5)
    fridge_camera2 = FridgeCamera(3, "electric", "mechanical", 15, 7)
    wine_fridge1 = WineFridge(10, 750)
    wine_fridge2 = WineFridge(20, 1500)
    vegetable_fridge1 = VegetableFridge(5, 200)
    vegetable_fridge2 = VegetableFridge(8, 150)

    fridge_manager.add_fridge(freezer1)
    fridge_manager.add_fridge(freezer2)
    fridge_manager.add_fridge(fridge_camera1)
    fridge_manager.add_fridge(fridge_camera2)
    fridge_manager.add_fridge(wine_fridge1)
    fridge_manager.add_fridge(wine_fridge2)
    fridge_manager.add_fridge(vegetable_fridge1)
    fridge_manager.add_fridge(vegetable_fridge2)

    print("All fridges:")
    for fridge in fridge_manager.fridges:
        print(fridge)

    print("\nSearch by capacity >= 100:")
    for fridge in fridge_manager.search_by_max_usable_capacity(100):
        print(fridge)

    print("\nSearch by class WineFridge:")
    for fridge in fridge_manager.search_by_class(WineFridge):
        print(fridge)
