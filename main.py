from datetime import datetime
from typing import List, Union
from unicodedata import name


# method
# attributes
class Fish:
    def __init__(self, fish_name, price_in_uah_per_kilo, catch_date, origin, body_only, weight) -> None:
        self.fish_name = fish_name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date
        self.origin = origin
        self.body_only = body_only
        self.weight = weight


class FishShop:

    def __init__(self, shop_name) -> None:
        self.shop_name = shop_name
        self.fish_list = []

    def add_fish(self, fish_name: Fish, total_weight: float) -> None:
        self.fish_list.append([fish_name, total_weight])

    def get_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        #sorted_list = self.fish_list
        #sorted()

        pass

    def sell_fish(self, fish_name: Fish, weight: float) -> float:
        for i in aushan.fish_list:
            if i[0].fish_name == fish_name.fish_name:
                i[1] = i[1] - weight
                for i in aushan.fish_list:
                    print(i[0].fish_name, i[1])

    def cast_out_old_fish(self) -> List[Union[str, float]]:
        #today_date = datetime.today().date()
        #difference_in_days = 2
        #for i in aushan.fish_list:
        #    difference_in_days = today_date  i[0].catch_date
        #    print(difference_in_days)
        pass


class Seller:

    def calculate_fish_price_in_uah(self, fish_name: str, weight: float, price_in_uah_per_kilo: float,
                                    body_only: bool) -> float:
        pass

    def inform_fish_freshness(self, fish_name: str, catch_date: datetime) -> bool:
        pass


class Buyer:

    def buy_fish(self, fish_name: str, weight:float, price_in_uah_for_fish: float,
                 money_available_to_spend: float, fish_is_fresh: bool) -> bool:
        pass


herring = Fish("Herring", 50, 2022-1-26, "Norway", True, 0.6)
salmon = Fish("Salmon", 400, 2022-1-20, "Norway", False, 3)
cod = Fish("Cod", 100, 2022-1-25, "Norway", False, 3)
catfish = Fish("Catfish", 80, 2022-1-24, "Australia", True, 2)
mackerel = Fish("Mackerel", 120 , 2022-1-26, "Spain", True, 0.4)

aushan = FishShop("aushan")

aushan.add_fish(herring, 40)
aushan.add_fish(salmon, 30)
aushan.add_fish(cod, 45)
aushan.add_fish(catfish, 35)
aushan.add_fish(mackerel, 50)

for i in aushan.fish_list:
    print (i[0].fish_name, i[1])

aushan.sell_fish(salmon, 2)
aushan.sell_fish(mackerel, 6)
#aushan.cast_out_old_fish()
