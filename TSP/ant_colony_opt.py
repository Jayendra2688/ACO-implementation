import numpy as np
import random


class Aco:
    def __init__(self, generations: int, ants: int, colonies: int, alpha: float, beta: float, rho: float, dist):

        self.generations = generations
        self.ants = ants
        self.alpha = alpha  # for pheromones
        self.beta = beta  # for dis-1
        self.rho = rho  # rate of evapouration
        self.colonies = colonies
        self.dist = dist
        print(self.dist)
        self.Q = 1

        self.pheromones = np.ones((self.colonies, self.colonies))
        self.delta_pheromones = np.zeros((self.colonies, self.colonies))
        self.to_visit = {}
        self.run_aco()


    def binary_search_upper_bound(self, arr, target):
        """upper bound for target in array(arr)"""
        low, high = 0, len(arr)
        ans = -1
        while low < high:
            mid = low + (high - low) // 2

            if arr[mid] <= target:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1

        return ans

    def generate_path(self):
        """generating the path based on pheromone level and distances and updating to_visit list"""
        to_visit = set(range(self.colonies))
        # rand_city = random.randint(0,self.colonies-1)
        path_taken = [0]
        to_visit.remove(0)

        while len(to_visit) != 0:
            # generate a probablity scale
            curr_city = path_taken[-1]
            next_cities = list(to_visit)
            # sum of rewards (phremone * 1/distance)
            reward_sum = 0
            for next_city in next_cities:

                reward = (self.pheromones[curr_city][next_city] ** self.alpha) / ((self.dist[curr_city][next_city]) ** self.beta)

                reward_sum += reward

            prob_prefix = []
            pre = 0
            for next_city in next_cities:
                reward = (self.pheromones[curr_city][next_city] ** self.alpha) / ((self.dist[curr_city][next_city]) ** self.beta)
                # print(reward)
                city_prob = reward / reward_sum
                pre += city_prob
                prob_prefix.append(pre)

            # just to avoid unexpected error
            prob_prefix[-1] = 1.0000001
            rand_num = random.random()
            rand_city = next_cities[self.binary_search_upper_bound(prob_prefix, rand_num)]
            path_taken.append(rand_city)
            to_visit.remove(rand_city)
        path_taken.append(path_taken[0])

        return path_taken
    def calculate_pathlen(self,path_taken):
        len_path = 0
        for i in range(len(path_taken) - 1):
            x_colony = path_taken[i]
            y_colony = path_taken[i + 1]
            len_path += self.dist[x_colony][y_colony]
        return round(len_path,2)
    def update_delta(self, path_taken):
        """adds the change in pheromone values by each ant to delta_pheromone ,so that it is useful for next generation"""
        len_path = self.calculate_pathlen(path_taken)
        print(len_path)
        delta_p = self.Q / len_path
        for i in range(len(path_taken) - 1):
            x_city = path_taken[i]
            y_city = path_taken[i + 1]

            self.delta_pheromones[x_city][y_city] += delta_p

    def update_pheromone(self):
        """update pheromone table after each generation (evaporation + delta_addition)"""
        for i in range(self.colonies):
            for j in range(self.colonies):
                self.pheromones[i][j] += self.delta_pheromones[i][j]

                self.pheromones[i][j] = (1 - self.rho) * self.pheromones[i][j]

        #changing delta pheromones to zero
        for i in range(self.colonies):
            for j in range(self.colonies):
                self.delta_pheromones[i][j] = 0

    def run_aco(self):
        for gen in range(self.generations):
            for ant in range(self.ants):
                path_taken = self.generate_path()
                self.update_delta(path_taken)
            print(f"\n\n")
            self.update_pheromone()

    def optimal_path(self):
        path = self.generate_path()
        print(self.calculate_pathlen(path))
        return path

