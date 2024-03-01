import random
class Passenger_generator:
    def __init__(self,cities,routes):
        self.cities = cities
        self.routes = routes
        self.passengers = 0
        self.generate_list()

    def generate_route(self):
        """return two random cities as route"""
        route = [random.randint(0,random.randint(0,len(self.cities)-1))]
        b = random.randint(0,random.randint(0,len(self.cities)-1))
        while route[0]==b:
            b = random.randint(0,random.randint(0,len(self.cities)-1))
        route.append(b)
        return tuple(route)

    def generate_list(self):
        """creates a file containing routes list"""
        with open('routes_p.txt','w') as file:
            for i in range(self.routes):
                route = self.generate_route()
                passengers = random.randint(5, 30)
                self.passengers += passengers
                file.write(f"{self.cities[route[0]]} to {self.cities[route[1]]},{passengers}\n")


