from managers.set_manager import SM
from models.freezer import Freezer
from models.fridge_camera import FridgeCamera
from models.wine_fridge import WineFridge
from models.vegetable_fridge import VegetableFridge
from managers.fridge_manager import FridgeManager

if __name__ == "__main__":
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
        freezer_manager = FridgeManager()

        for freezer in freezer_manager.fridges:
            freezer.do_something()

        print("Fridge Manager Fridges:")
        for fridge in fridge_manager.fridges:
            print(fridge)

    print("All fridges:")
    for fridge in fridge_manager:
        print(fridge)

    print("\nSearch by capacity >= 100:")
    for fridge in fridge_manager.search_by_max_usable_capacity(100):
        print(fridge)

    print("\nSearch by class WineFridge:")
    for fridge in fridge_manager.search_by_class(WineFridge):
        print(fridge)

    print("\nResults of do_something() for all fridges:")
    for result in fridge_manager.do_something_for_all():
        print(result)

    print("\nObject with index:")
    for index, fridge in fridge_manager.get_object_with_index():
        print(f"Index: {index}, Fridge: {fridge}")

    print("\nObject with do_something() result:")
    for fridge, result in fridge_manager.get_object_with_do_something():
        print(f"Fridge: {fridge}, Result: {result}")

    print("\nObject with index and do_something() result:")
    for index, fridge, result in fridge_manager.get_object_with_index_and_do_something():
        print(f"Index: {index}, Fridge: {fridge}, Result: {result}")

    print("\nAttributes with int values:")
    attributes = fridge_manager.get_attributes_by_type(int)
    for key, value in attributes.items():
        print(f"{key}: {value}")

    print("\nCheck conditions:")
    conditions = fridge_manager.check_conditions(lambda fridge: fridge.get_max_usable_capacity() > 10)
    print("All:", conditions["all"])
    print("Any:", conditions["any"])

    print("\nSet Manager:")
    sm = SM(fridge_manager)
    print("Length:", len(sm))
    print("Items:")
    for item in sm:
        print(item)
