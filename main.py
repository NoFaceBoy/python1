from datetime import datetime
from operator import itemgetter
from typing import List, Union
from unicodedata import name


# method
# attributes
class FishInfo(object):
    def __init__(self,  fish_name: str, origin: str, price_in_uah_per_kilo:float, catch_date: datetime,
                 due_date: datetime) -> None:
        self.fish_name = fish_name
        self.origin = origin
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date
        self.due_date = due_date


class Fish(FishInfo):
    def __init__(self, fish_name: str, origin: str, price_in_uah_per_kilo:float, catch_date: datetime,
                 due_date: datetime, age_in_month: int, weight: float) -> None:
        self.fish_info = FishInfo(fish_name, origin, price_in_uah_per_kilo, catch_date, due_date)
        self.age_in_month = age_in_month
        self.weight = weight


class FishBox(FishInfo):
    def __init__(self, fish_name: str, origin: str, price_in_uah_per_kilo: float, catch_date: datetime,
                 due_date: datetime, weight: float, package_date: datetime, height: float,
                 width: float, length: float) -> None:
        self.fish_info = FishInfo(fish_name, origin, price_in_uah_per_kilo, catch_date, due_date)
        self.weight = weight
        self.package_date = package_date
        self.height = height
        self.width = width
        self.length = length


class FishShop(FishBox, Fish):
    def __init__(self) -> None:
        pass
    fish_box = []
    fresh_fish = []

    def add_fish_box(self, fish_box: FishBox) -> None:
        self.fish_box.append([fish_box.fish_info.fish_name, fish_box])

    def add_fish(self, fresh_fish: Fish) -> None:
        self.fresh_fish.append([fresh_fish.fish_info.fish_name, fresh_fish])
        pass

    def get_fish_names_sorted_by_price(self) -> Union[str, bool, float]:
        all_fishes = []
        for current_fish in self.fish_box:
            all_fishes.append((current_fish[0], current_fish[1].fish_info.price_in_uah_per_kilo, False))
        for current_fish in self.fresh_fish:
            all_fishes.append((current_fish[0], current_fish[1].fish_info.price_in_uah_per_kilo, True))
        all_fishes.sort(key=itemgetter(1))
        return all_fishes

    def sell_fish(self, name: str, weight: float, is_alive: bool) -> [Union[str, float, float]]:
        if is_alive:
            for current_fish in self.fresh_fish:
                if current_fish[0] == name:
                    current_fish[1].weight = current_fish[1].weight - weight
                    return name, weight, current_fish[1].fish_info.price_in_uah_per_kilo * weight

        else:
            for current_fish_box in self.fish_box:
                if current_fish_box[0] == name:
                    current_fish_box[1].weight = current_fish_box[1].weight - weight
                    return name, weight, current_fish_box[1].fish_info.price_in_uah_per_kilo * weight


herring = Fish("Herring", "Norway", 74.2, datetime(2022, 1, 25), datetime(2022, 2, 2), 2, 1.2)
herring_box = FishBox("Herring", "Norway", 50.4, datetime(2022, 1, 25), datetime(2022, 2, 2), 40, datetime(2022, 1, 26),
                      1, 1, 1)
salmon = Fish("Salmon", "Norway", 223.6, datetime(2022, 1, 27), datetime(2022, 2, 3), 3, 2.4)
cod_box = FishBox("Cod", "Norway", 100, datetime(2022, 1, 28), datetime(2022, 2, 5), 60, datetime(2022, 1, 30), 1.5,
                  1.5, 1.5)

aushan = FishShop()
aushan.add_fish_box(herring_box)
aushan.add_fish(herring)
aushan.add_fish(salmon)
aushan.add_fish_box(cod_box)

for i in aushan.fish_box:
    print("List of fish boxes:" + " " + i[0], i[1].weight)
for i in aushan.fresh_fish:
    print("List of fresh fishes:" + " " + i[0], i[1].weight)


print("\nSold:", aushan.sell_fish("Herring", 2, False))
print("Sold:",aushan.sell_fish("Herring", 1.2, True))

for i in aushan.fish_box:
    print("List of fish boxes:" + " " + i[0], i[1].weight)
for i in aushan.fresh_fish:
    print("List of fresh fishes:" + " " + i[0], i[1].weight)

print("\nFishes sorted by price:", aushan.get_fish_names_sorted_by_price())
