import random

class Gen_Quota:
    def __init__(self,cities):
        self.cities = cities
        self.gen_quota()
    def gen_quota(self):
        for i, city in enumerate(self.cities):
            self.cities[i] = city.replace("\n", "")
            self.cities[i] += f",{random.randint(51, 100)}\n"

        with open('cities_quota.txt', 'w') as file:
            file.writelines(self.cities)