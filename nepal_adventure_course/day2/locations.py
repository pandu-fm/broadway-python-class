ENERGY_BY_DIFFICULTY = {"Easy": 10, "Medium": 20, "Hard": 30, "Extreme": 40}


class Location:
    def __init__(self, name, altitude, difficulty, travel_cost, neighbors):
        self.name = name
        self.altitude = altitude
        self.difficulty = difficulty
        self.travel_cost = travel_cost
        self.neighbors = neighbors

    def energy_cost(self):
        return ENERGY_BY_DIFFICULTY[self.difficulty]

    def __str__(self):
        return f"{self.name} ({self.altitude}m, {self.difficulty})"


def build_nepal_map():
    locations = [
        Location("Kathmandu", 1400, "Easy", 0, ["Pokhara", "Lukla"]),
        Location("Pokhara", 822, "Easy", 500, ["Kathmandu", "Jomsom"]),
        Location("Jomsom", 2743, "Medium", 1200, ["Pokhara", "Marpha"]),
        Location("Marpha", 2670, "Medium", 300, ["Jomsom", "Muktinath"]),
        Location("Muktinath", 3800, "Hard", 600, ["Marpha"]),
        Location("Lukla", 2860, "Hard", 5000, ["Kathmandu", "Namche Bazaar"]),
        Location("Namche Bazaar", 3440, "Hard", 1000, ["Lukla", "Everest Base Camp"]),
        Location("Everest Base Camp", 5364, "Extreme", 2000, ["Namche Bazaar"]),
    ]
    map_data = {}
    for location in locations:
        map_data[location.name] = location
    return map_data
