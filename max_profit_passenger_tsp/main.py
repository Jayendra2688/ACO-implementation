import requests
import distance_mat
import ant_colony_opt
import passengers_genrator
import map_generator
#your api key
OW_KEY = "x"

OW_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"

#TODO: generating the passenger routes info if required

with open('cities2.txt',mode='r') as file:
    cities = file.readlines()

cities = cities[:30]

for i in range(len(cities)):
    cities[i] = cities[i].replace("\n","")


# gen_passengers = passengers_genrator.Passenger_generator(cities,20)

# print(gen_passengers.passengers) #112



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
# #
# co_ordinates = []
# for city in cities:
#     PARAMS = {
#         "q": f"{city},IN",
#         "limit": 1,
#         "appid": OW_KEY,
#     }
#     print(city)
#     response = requests.get(url=OW_ENDPOINT, params=PARAMS).json()[0]
#     co_ordinates.append((response['lat'], response['lon']))
# print(co_ordinates)

#
co_ordinates = [(14.1585816, 77.7588613), (14.1676112, 77.7325256), (14.1545109, 77.7395881), (14.1636778, 77.8124982), (14.2043896, 77.7902939), (14.2002721, 77.8066191), (14.1934853, 77.8195093), (14.1870879, 77.7671355), (14.1477877, 77.7541295), (14.1814879, 77.7180866), (14.1825338, 77.7473444), (14.1531882, 77.82317), (14.1453545, 77.7891237), (14.1317162, 77.7725651), (14.129813, 77.7829945)]

#TODO:creating distance matrix

dist_mat = distance_mat.Distance_matrix(co_ordinates)

distance_matrix = dist_mat.create_distance_mat()

#TODO:Running aco algo

aco = ant_colony_opt.Aco(1000,30,len(cities),1,2,0.15,distance_matrix,route_info)

path_generated = aco.optimal_path()

print("best Route : ")
print(path_generated)

#TODO:Creating map

map = map_generator.Map_generator(cities,co_ordinates,path_generated)
