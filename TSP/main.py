import requests
import distance_mat
import ant_colony_opt
import map_generator

from lower_bound import one_tree

#your api key
OW_KEY = "x"

OW_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"


with open('cities2.txt',mode='r') as file:
    cities = file.readlines()

for i in range(len(cities)):
    cities[i] = cities[i].replace("\n","")

# co_ordinates = []
# for city in cities:
#     PARAMS = {
#         "q": f"{city},Andhra Pradesh,IN",
#         "limit": 1,
#         "appid": OW_KEY,
#     }
#     print(city)
#     response = requests.get(url=OW_ENDPOINT, params=PARAMS).json()[0]
#     co_ordinates.append((response['lat'], response['lon']))
#
# print(co_ordinates)
# print(len(co_ordinates))
co_ordinates = [(14.1585816, 77.7588613), (14.1676112, 77.7325256), (14.1636778, 77.8124982), (14.1545109, 77.7395881), (14.2043896, 77.7902939), (14.2002721, 77.8066191), (14.1934853, 77.8195093), (14.1870879, 77.7671355), (14.1477877, 77.7541295), (14.1814879, 77.7180866), (14.1825338, 77.7473444), (14.1531882, 77.82317), (14.1453545, 77.7891237), (14.1317162, 77.7725651), (14.129813, 77.7829945)]


dist_mat = distance_mat.Distance_matrix(co_ordinates)

distance_matrix = dist_mat.create_distance_mat()

aco = ant_colony_opt.Aco(1000,20,len(cities),1,1,0.08,distance_matrix)

path_generated = aco.optimal_path()

print(f"\n{path_generated}")

print(f"TSP cost : {aco.calculate_pathlen(path_generated)}")

OneTree = one_tree.OneTreeMst()

print(f"Max-one-tree-cost : {OneTree.cal_one_tree_mst(distance_matrix)}")

map = map_generator.Map_generator(cities,co_ordinates,path_generated)
