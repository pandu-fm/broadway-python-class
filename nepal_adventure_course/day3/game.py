import random

from events import get_random_event
from exceptions import InsufficientEnergyError, InvalidActionError, NepalAdventureError
from locations import DESTINATIONS, Weather, build_nepal_map, get_altitude_effects
from models import Guide, Local, Merchant, Traveler
from storage import save_game
from utils import format_money, print_header, prompt_int

BASE_TRAVEL_ENERGY = 20
EXPLORE_ENERGY = 10
GUIDE_FEE = 300

EXPLORE_OUTCOMES = ["money", "food", "medicine", "hidden path", "wildlife", "nothing", "injury", "local"]
GUIDE_NAMES = ["Pasang Sherpa", "Nima Tamang", "Dawa Gurung"]
TRAVELER_STORIES = [
    "Don't go ahead. There's a storm.",
    "I heard the weather ahead is getting worse.",
    "The trail past the next village is steep, so save your energy.",
    "A landslide was reported near the river last week.",
]
LOCAL_ADVICE = [
    "There is a small shelter nearby if you need to rest.",
    "Drink plenty of water. The air is thin up there.",
    "Walk slowly and you will walk far.",
]
TRAVELER_NAMES = ["John from Canada", "Mika from Japan", "Sara from Spain"]
LOCAL_NAMES = ["Kanchi Maya", "Ram Bahadur", "Sunita Rai"]
MERCHANT_NAMES = ["Pema the Shopkeeper", "Hari the Trader", "Lhakpa the Merchant"]


class GameEngine:
    def __init__(self, player):
        self.player = player
        self.map_data = build_nepal_map()
        self.game_over = False
        self.weather = Weather.for_location(self.current_location())

    def current_location(self):
        return self.map_data[self.player.location]

    def goal_location_name(self):
        return DESTINATIONS[self.player.destination]["location"]

    def has_reached_goal(self):
        return self.player.location == self.goal_location_name()

    def display_status(self):
        player = self.player
        print()
        print_header("PLAYER STATUS")
        print(f"Player      : {player.name}")
        print(f"Age         : {player.age}")
        print(f"Location    : {player.location}")
        print(f"Destination : {player.destination}")
        print()
        print(f"❤️ Health   : {player.health}")
        print(f"⚡ Energy   : {player.energy}")
        print(f"💰 Money    : {format_money(player.money)}")
        print(f"🍎 Food     : {player.food}")
        print(f"💧 Water    : {player.water}")
        print()
        print(f"⭐ Experience : {player.experience}")
        print(f"🤝 Reputation : {player.reputation}")
        print()
        print(f"Day         : {player.days_survived}")
        print(f"Distance    : {player.distance_traveled} km")
        print("=" * 40)

    def display_inventory(self):
        print()
        print_header("🎒 INVENTORY")
        if not self.player.inventory:
            print("Your inventory is empty.")
        for number, item in enumerate(self.player.inventory, 1):
            print(f"{number}. {item.name:<14} x{item.quantity:<3} {item.description}")

    def display_map(self):
        print()
        print_header("🗺️ NEPAL MAP")
        for name, location in self.map_data.items():
            marker = ""
            if name == self.player.location:
                marker += " <-- YOU ARE HERE"
            if name == self.goal_location_name():
                marker += " <-- DESTINATION"
            print(f"{name} | {location.altitude}m | {location.temperature}°C | {location.difficulty}{marker}")
            print(f"    Paths to: {', '.join(location.neighbors)}")
            print(f"    Activities: {', '.join(location.activities)}")

    def travel_energy_cost(self, target):
        cost = BASE_TRAVEL_ENERGY + get_altitude_effects(target.altitude)["travel_energy"]
        if self.player.has_item("Hiking Shoes"):
            cost -= 5
        if self.player.safe_route:
            cost -= 10
        return max(5, cost)

    def travel(self):
        current = self.current_location()
        names = list(current.neighbors)
        print("\nWhere do you want to go?")
        for number, name in enumerate(names, 1):
            target = self.map_data[name]
            print(f"{number}. {name:<20} {current.distance_to(target):>3} km | {target.altitude}m | "
                  f"Cost: {format_money(target.travel_cost)} | Energy: {self.travel_energy_cost(target)}")
        print("0. Stay here")
        choice = prompt_int("Choose: ", 0, len(names))
        if choice == 0:
            return
        target = self.map_data[names[choice - 1]]
        energy_cost = self.travel_energy_cost(target)
        if self.player.energy < energy_cost:
            raise InsufficientEnergyError(f"You need {energy_cost} Energy to go there. Try resting first.")
        self.player.spend_money(target.travel_cost)
        self.player.change_energy(-energy_cost)
        self.player.distance_traveled += current.distance_to(target)
        self.player.location = target.name
        self.player.experience += 15
        self.player.safe_route = False
        print(f"\n🚶 You travel to {target.name} ({target.altitude}m).")
        self.apply_weather()
        self.apply_altitude(target)
        if random.random() < 0.6:
            event = get_random_event(target.altitude)
            print()
            print("➡️  " + event.play(self.player))
        self.advance_day()

    def apply_weather(self):
        effects = self.weather.effects
        print(f"Weather: {self.weather} - {effects['description']}")
        energy_loss = effects["energy_loss"]
        if self.player.has_item("Jacket"):
            energy_loss = energy_loss // 2
        if energy_loss:
            self.player.change_energy(-energy_loss)
            print(f"Energy -{energy_loss}.")
        if random.random() < effects["lost_chance"] and not self.player.has_item("Map"):
            self.player.change_energy(-10)
            print("You got lost in the fog! Energy -10.")
        if random.random() < effects["injury_chance"]:
            self.player.change_health(-15)
            print("The storm throws you to the ground! Health -15.")

    def apply_altitude(self, location):
        effects = get_altitude_effects(location.altitude)
        if effects["sickness_chance"] and random.random() < effects["sickness_chance"]:
            print("\n⚠️ ALTITUDE SICKNESS")
            print("You are struggling to breathe at this altitude.")
            self.player.change_health(-effects["health_loss"])
            self.player.change_energy(-effects["energy_loss"])
            print(f"Health -{effects['health_loss']}, Energy -{effects['energy_loss']}")

    def advance_day(self):
        message = self.player.pass_day()
        print(f"\n🌙 Night falls. {message}")
        print(f"☀️ Day {self.player.days_survived} begins.")
        self.weather = Weather.for_location(self.current_location())
        print(f"Morning weather in {self.player.location}: {self.weather}")

    def rest(self):
        print("\n⛺ You set up camp for the night.")
        energy_gain = 30
        if self.player.has_item("Tent"):
            energy_gain += 15
        self.player.change_energy(energy_gain)
        self.player.change_health(10)
        print(f"Energy +{energy_gain}, Health +10.")
        if not self.player.has_item("Torch") and random.random() < 0.3:
            event = get_random_event(self.current_location().altitude)
            print("\nSomething happens in the night...")
            print("➡️  " + event.play(self.player))
        self.advance_day()

    def eat(self):
        if self.player.health >= 100:
            raise InvalidActionError("Your health is already full. Save your food for later.")
        print("\n" + self.player.use_item("Food"))

    def drink(self):
        if self.player.energy >= 100:
            raise InvalidActionError("Your energy is already full. Save your water for later.")
        print("\n" + self.player.use_item("Water"))

    def use_item(self):
        usable_items = []
        for item in self.player.inventory:
            if item.is_usable():
                usable_items.append(item)
        if not usable_items:
            raise InvalidActionError("You have nothing to use right now.")
        print()
        print_header("USE ITEM")
        for number, item in enumerate(usable_items, 1):
            print(f"{number}. {item.name:<14} x{item.quantity:<3} {item.description}")
        print("0. Cancel")
        choice = prompt_int("Choose: ", 0, len(usable_items))
        if choice > 0:
            print("\n" + self.player.use_item(usable_items[choice - 1].name))

    def found_item(self, name, quantity):
        self.player.add_item(name, quantity)
        print(f"You found {quantity} x {name}!")

    def explore(self):
        if "Explore" not in self.current_location().activities:
            raise InvalidActionError("There is nothing to explore here.")
        if self.player.energy < EXPLORE_ENERGY:
            raise InsufficientEnergyError(f"You need {EXPLORE_ENERGY} Energy to explore. Try resting first.")
        self.player.change_energy(-EXPLORE_ENERGY)
        self.player.experience += 5
        print(f"\n🔍 You explore around {self.player.location}. Energy -{EXPLORE_ENERGY}, Experience +5.")
        outcome = random.choice(EXPLORE_OUTCOMES)
        if outcome == "money":
            amount = random.randint(200, 800)
            self.player.money += amount
            print(f"You find a lost wallet with Rs. {amount}!")
        elif outcome == "food":
            self.found_item("Food", random.randint(1, 2))
        elif outcome == "medicine":
            self.found_item("Medicine", 1)
        elif outcome == "hidden path":
            self.player.safe_route = True
            print("You discover a hidden path! Your next trip costs less Energy.")
        elif outcome == "wildlife":
            self.player.experience += 10
            print("You watch a herd of blue sheep on the cliffs. Experience +10.")
        elif outcome == "injury":
            self.player.change_health(-10)
            print("You trip on a loose rock. Health -10.")
        elif outcome == "local":
            print(Local(random.choice(LOCAL_NAMES), random.choice(LOCAL_ADVICE)).interact(self.player))
        else:
            print("You search for a while but find nothing.")

    def talk_to_npc(self):
        location = self.current_location()
        if "Talk" not in location.activities:
            raise InvalidActionError("There is nobody to talk to here.")
        people = [
            Guide(random.choice(GUIDE_NAMES), GUIDE_FEE, "the next village"),
            Traveler(random.choice(TRAVELER_NAMES), random.choice(TRAVELER_STORIES)),
            Local(random.choice(LOCAL_NAMES), random.choice(LOCAL_ADVICE)),
        ]
        if "Shop" in location.activities:
            people.append(Merchant(random.choice(MERCHANT_NAMES), 1 + location.altitude / 10000))
        nearby = random.sample(people, 3)
        print("\nPeople nearby:")
        for number, person in enumerate(nearby, 1):
            print(f"{number}. {person}")
        print("0. Walk away")
        choice = prompt_int("Talk to: ", 0, len(nearby))
        if choice > 0:
            print()
            print(nearby[choice - 1].interact(self.player))

    def finish_turn(self):
        player = self.player
        if player.health <= 0:
            print("\n💀 Your health reached zero. The journey is over.")
            self.game_over = True
        elif self.has_reached_goal():
            print(f"\n🎉 You reached {player.destination} in {player.days_survived} days!")
            print("You have built a game where every journey is different!")
            self.game_over = True
        elif player.energy <= 0:
            player.change_health(-15)
            player.change_energy(20)
            print("\n😵 You collapse from exhaustion! Health -15, Energy +20.")
        if self.game_over:
            input("\nPress Enter to return to the main menu...")

    def show_action_menu(self):
        player = self.player
        print()
        print(f"--- {player.location} | Day {player.days_survived} | Weather: {self.weather} "
              f"| ❤️ {player.health} ⚡ {player.energy} ---")
        print("1. Travel")
        print("2. Rest")
        print("3. Eat")
        print("4. Drink")
        print("5. Explore")
        print("6. Talk to NPC")
        print("7. Use Item")
        print("8. View Status")
        print("9. View Map")
        print("10. View Inventory")
        print("0. Save and return to main menu")

    def play(self):
        print(f"\nMorning weather in {self.player.location}: {self.weather}")
        while not self.game_over:
            self.show_action_menu()
            choice = prompt_int("Choose action: ", 0, 10)
            if choice == 0:
                if save_game(self.player):
                    print("\nGame saved. See you soon!")
                else:
                    print("\nSorry, the game could not be saved.")
                return
            try:
                if choice == 1:
                    self.travel()
                elif choice == 2:
                    self.rest()
                elif choice == 3:
                    self.eat()
                elif choice == 4:
                    self.drink()
                elif choice == 5:
                    self.explore()
                elif choice == 6:
                    self.talk_to_npc()
                elif choice == 7:
                    self.use_item()
                elif choice == 8:
                    self.display_status()
                elif choice == 9:
                    self.display_map()
                else:
                    self.display_inventory()
            except NepalAdventureError as error:
                print(f"\n⚠️ {error}")
            self.finish_turn()
