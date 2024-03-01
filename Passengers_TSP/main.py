import requests
import distance_mat
import ant_colony_opt
import passengers_genrator
import map_generator
#your api key
OW_KEY = "x"

OW_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"

#TODO: generating the passenger routes info if required

with open('cities.txt',mode='r') as file:
    cities = file.readlines()

cities = cities[:30]

for i in range(len(cities)):
    cities[i] = cities[i].replace("\n","")


# gen_passengers = passengers_genrator.Passenger_generator(cities,50)
#
# print(gen_passengers.passengers) #919



with open('routes_p.txt','r') as file:
        routes = file.readlines()

routes = routes[:50]

for i in range(len(routes)):
    routes[i] = routes[i].replace("\n","")

#TODO:creating a map called route_info {(route):passengers}

route_info = {}

for route in routes:
    route = route.split(',')
    a = route[0].split('to')[0].strip()
    a = cities.index(a)
    b = route[0].split('to')[1].strip()
    b = cities.index(b)

    p = int(route[1])

    route_info[(a,b)] = p


# #TODO:using api for cities co-ord
#
# # co_ordinates = []
# # for city in cities:
# #     PARAMS = {
# #         "q": f"{city},IN",
# #         "limit": 1,
# #         "appid": OW_KEY,
# #     }
# #     print(city)
# #     response = requests.get(url=OW_ENDPOINT, params=PARAMS).json()[0]
# #     co_ordinates.append((response['lat'], response['lon']))
# # print(co_ordinates)
#
#
co_ordinates = [(25.3356491, 83.0076292), (16.4329976, 80.9937151), (14.6783221, 77.6065039), (17.360589, 78.4740613), (25.4381302, 81.8338005), (9.2844657, 79.3125553), (19.7668121, 74.4754386), (25.1737019, 75.8574194), (26.9154576, 75.8189817), (28.6517178, 77.2219388), (23.0216238, 72.5797068), (22.5414185, 88.35769124388872), (23.2584857, 77.401989), (34.0747444, 74.8204443), (25.6093239, 85.1235252), (23.3700501, 85.3250387), (23.1608938, 79.9497702), (19.0785451, 72.878176), (31.1041526, 77.1709729), (23.7952809, 86.4309638), (25.6618755, 94.1019156), (24.7991162, 93.9364419), (25.5760446, 91.8825282), (14.4493717, 79.9873763), (13.0836939, 80.270186), (28.0159286, 73.3171367), (26.4609135, 80.3217588), (12.9767936, 77.590082), (20.4686, 85.8792), (9.931308, 76.2674136)]

#TODO:creating distance matrix

dist_mat = distance_mat.Distance_matrix(co_ordinates)

distance_matrix = dist_mat.create_distance_mat()

#TODO:Running aco algo

aco = ant_colony_opt.Aco(500,30,len(cities),1,1,0.4,distance_matrix,route_info)

path_generated = aco.optimal_path()

print(path_generated)

#TODO:Creating map

map = map_generator.Map_generator(cities,co_ordinates,path_generated)
