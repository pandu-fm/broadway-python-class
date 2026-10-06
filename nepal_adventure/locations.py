import random

TOWN_ACTIVITIES = ["Rest", "Explore", "Talk", "Shop"]
TREK_ACTIVITIES = ["Rest", "Explore", "Talk"]


class Weather:
    CONDITIONS = ["Sunny", "Cloudy", "Rainy", "Foggy", "Snowy", "Storm"]

    EFFECTS = {
        "Sunny": {"energy_loss": 0, "lost_chance": 0, "injury_chance": 0, "description": "Clear skies. Perfect trekking weather."},
        "Cloudy": {"energy_loss": 0, "lost_chance": 0, "injury_chance": 0, "description": "Cool and cloudy. Easy walking."},
        "Rainy": {"energy_loss": 10, "lost_chance": 0, "injury_chance": 0, "description": "Slippery trails drain your energy."},
        "Foggy": {"energy_loss": 5, "lost_chance": 0.35, "injury_chance": 0, "description": "Thick fog. It is easy to lose the trail."},
        "Snowy": {"energy_loss": 15, "lost_chance": 0, "injury_chance": 0, "description": "Freezing snow slows you down."},
        "Storm": {"energy_loss": 20, "lost_chance": 0, "injury_chance": 0.4, "description": "A dangerous mountain storm!"},
    }

    def __init__(self, condition="Sunny"):
        self.condition = condition
        self.effects = Weather.EFFECTS[condition]

    @classmethod
    def for_location(cls, location):
        if location.temperature <= 0:
            weights = [5, 10, 0, 15, 60, 10]
        elif location.altitude >= 3500:
            weights = [10, 15, 5, 20, 40, 10]
        elif location.altitude >= 2500:
            weights = [25, 25, 15, 15, 15, 5]
        else:
            weights = [40, 25, 20, 10, 0, 5]
        condition = random.choices(cls.CONDITIONS, weights=weights)[0]
        return cls(condition)

    def __str__(self):
        return self.condition


def get_altitude_effects(altitude):
    if altitude >= 4500:
        return {"name": "Extreme altitude", "travel_energy": 10, "sickness_chance": 0.6, "health_loss": 10, "energy_loss": 15}
    if altitude >= 3500:
        return {"name": "High altitude", "travel_energy": 5, "sickness_chance": 0.3, "health_loss": 5, "energy_loss": 10}
    if altitude >= 2500:
        return {"name": "Thin air", "travel_energy": 5, "sickness_chance": 0, "health_loss": 0, "energy_loss": 0}
    return {"name": "Normal", "travel_energy": 0, "sickness_chance": 0, "health_loss": 0, "energy_loss": 0}


class Location:
    def __init__(self, name, altitude, temperature, difficulty, travel_cost, distance, activities, neighbors):
        self.name = name
        self.altitude = altitude
        self.temperature = temperature
        self.difficulty = difficulty
        self.travel_cost = travel_cost
        self.distance = distance
        self.activities = activities
        self.neighbors = neighbors

    def distance_to(self, other):
        return abs(self.distance - other.distance)

    def __str__(self):
        return f"{self.name} ({self.altitude}m, {self.difficulty})"

    def __repr__(self):
        return f"Location('{self.name}', {self.altitude})"


DESTINATIONS = {
    "Muktinath": {"location": "Muktinath", "difficulty": "Medium", "multiplier": 1.0, "gear": "Hiking Shoes, Jacket"},
    "Langtang Valley": {"location": "Langtang", "difficulty": "Medium", "multiplier": 1.0, "gear": "Hiking Shoes, Map"},
    "Annapurna Base Camp": {"location": "Annapurna Base Camp", "difficulty": "Hard", "multiplier": 1.5, "gear": "Jacket, Tent, Medicine"},
    "Everest Base Camp": {"location": "Everest Base Camp", "difficulty": "Extreme", "multiplier": 2.0, "gear": "Jacket, Tent, Hiking Shoes, Medicine"},
    "Mustang": {"location": "Mustang", "difficulty": "Hard", "multiplier": 1.5, "gear": "Jacket, Rope, Map"},
}

def build_nepal_map():
    locations = [
        Location("Kathmandu", 1400, 22, "Easy", 0, 0, TOWN_ACTIVITIES, ["Pokhara", "Syabrubesi", "Lukla"]),
        Location("Pokhara", 822, 25, "Easy", 500, 200, TOWN_ACTIVITIES, ["Kathmandu", "Nayapul", "Jomsom"]),
        Location("Nayapul", 1070, 24, "Easy", 300, 240, TREK_ACTIVITIES, ["Pokhara", "Ghandruk"]),
        Location("Ghandruk", 1940, 18, "Medium", 400, 270, TOWN_ACTIVITIES, ["Nayapul", "Annapurna Base Camp"]),
        Location("Annapurna Base Camp", 4130, 2, "Hard", 1000, 310, TREK_ACTIVITIES, ["Ghandruk"]),
        Location("Jomsom", 2743, 12, "Medium", 1200, 350, TOWN_ACTIVITIES, ["Pokhara", "Marpha"]),
        Location("Marpha", 2670, 14, "Medium", 300, 365, TOWN_ACTIVITIES, ["Jomsom", "Muktinath", "Mustang"]),
        Location("Muktinath", 3800, 5, "Hard", 600, 400, TOWN_ACTIVITIES, ["Marpha"]),
        Location("Mustang", 3840, 4, "Hard", 2000, 445, TREK_ACTIVITIES, ["Marpha"]),
        Location("Syabrubesi", 1550, 19, "Medium", 600, 120, TOWN_ACTIVITIES, ["Kathmandu", "Langtang"]),
        Location("Langtang", 3430, 8, "Hard", 800, 160, TOWN_ACTIVITIES, ["Syabrubesi", "Kyanjin Gompa"]),
        Location("Kyanjin Gompa", 3870, 3, "Hard", 500, 180, TREK_ACTIVITIES, ["Langtang"]),
        Location("Lukla", 2860, 10, "Hard", 5000, 130, TOWN_ACTIVITIES, ["Kathmandu", "Namche Bazaar"]),
        Location("Namche Bazaar", 3440, 6, "Hard", 1000, 160, TOWN_ACTIVITIES, ["Lukla", "Everest Base Camp"]),
        Location("Everest Base Camp", 5364, -10, "Extreme", 2000, 210, TREK_ACTIVITIES, ["Namche Bazaar"]),
    ]
    return {location.name: location for location in locations}


def find_route(map_data, start, goal):
    waiting_paths = [[start]]
    visited = {start}
    while waiting_paths:
        path = waiting_paths.pop(0)
        if path[-1] == goal:
            return path
        for neighbor in map_data[path[-1]].neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                waiting_paths.append(path + [neighbor])
    return []


def journey(map_data, start, goal):
    previous_stop = None
    for stop in find_route(map_data, start, goal):
        kilometers = 0 if previous_stop is None else map_data[previous_stop].distance_to(map_data[stop])
        yield stop, kilometers
        previous_stop = stop
