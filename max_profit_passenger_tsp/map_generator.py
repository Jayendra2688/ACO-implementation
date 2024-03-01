import folium


class Map_generator:
    def __init__(self, cities, co_ordinates, path_taken):
        self.cities = cities
        self.co_ordinates = co_ordinates
        self.path_taken = path_taken
        self.generate_map()

    def generate_map(self):
        """generate a map based on path_taken with popups as city names"""

        my_map = folium.Map(location=(14.166436893249724, 77.77736663818361), zoom_start=13)

        for i, co_ordinate in enumerate(self.co_ordinates):
            folium.CircleMarker(location=co_ordinate, popup=folium.Popup(f"{self.cities[i]}"), radius=3,
                                fill=True).add_to(my_map)

        co_ordinates_list = []

        for city_ind in self.path_taken:
            co_ordinates_list.append(list(self.co_ordinates[city_ind]))

        folium.PolyLine(locations=co_ordinates_list, color="red").add_to(my_map)

        my_map.save('aco_generated_for_p_tsp.html')
