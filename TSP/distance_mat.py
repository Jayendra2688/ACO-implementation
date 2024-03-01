from math import radians, sin, cos, sqrt, atan2
import numpy as np
class Distance_matrix:
    def __init__(self,co_ordinates):
        self.co_ordinates = co_ordinates
        self.tot_cities = len(co_ordinates)
        self.distance_mat = np.zeros((self.tot_cities,self.tot_cities))

    def create_distance_mat(self):
        """calculate distance matrix"""
        for i in range(self.tot_cities):
            for j in range(self.tot_cities):
                self.distance_mat[i][j] = round(self.haversine_distance(self.co_ordinates[i],self.co_ordinates[j]),2)

        return self.distance_mat
    def haversine_distance(self,coord1, coord2):
        """takes tuples and calculate distance between two lat and long Using haversine formula (taken from ChatGPT)"""
        # Radius of the Earth in kilometers
        R = 6371.0

        # Convert latitude and longitude from degrees to radians
        lat1, lon1 = radians(coord1[0]), radians(coord1[1])
        lat2, lon2 = radians(coord2[0]), radians(coord2[1])

        # Calculate the differences between latitudes and longitudes
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Haversine formula
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Distance in kilometers
        distance = R * c

        return distance

