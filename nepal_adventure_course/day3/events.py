import random

from exceptions import InsufficientMoneyError
from utils import print_header, prompt_int


class RandomEvent:
    title = "Event"
    description = ""
    choices = []
    min_altitude = 0
    max_altitude = 6000

    def is_possible(self, altitude):
        return self.min_altitude <= altitude <= self.max_altitude

    def play(self, player):
        print_header("🎲 RANDOM EVENT")
        print(f"** {self.title} **\n")
        print(self.description)
        choice = 0
        if self.choices:
            print()
            for number, text in enumerate(self.choices, 1):
                print(f"{number}. {text}")
            choice = prompt_int("\nChoose: ", 1, len(self.choices))
        message = self.resolve(choice, player)
        return message

    def resolve(self, choice, player):
        raise NotImplementedError


class HeavyRainEvent(RandomEvent):
    title = "Heavy Rain"
    description = "A heavy rain has started. The trail turns to mud."
    choices = ["Continue walking", "Find shelter", "Turn back to the last teahouse"]
    max_altitude = 4500

    def resolve(self, choice, player):
        if choice == 1:
            player.change_energy(-20)
            player.change_health(-5)
            player.experience += 10
            return "You push through the mud. Energy -20, Health -5, Experience +10."
        if choice == 2:
            player.change_energy(-5)
            lost_food = player.lose_item("Food", 1)
            return f"You wait under a rock overhang. Energy -5, Food -{lost_food}."
        if player.money >= 200:
            player.money -= 200
            player.change_energy(10)
            return "You pay Rs. 200 for tea and a warm bed. Energy +10."
        player.change_energy(-10)
        return "You cannot afford a bed and spend a cold night. Energy -10."


class LandslideEvent(RandomEvent):
    title = "Landslide"
    description = "Rocks have fallen and block the trail ahead!"
    choices = ["Climb over the rocks", "Take a long detour", "Use your Rope"]
    min_altitude = 1500

    def resolve(self, choice, player):
        if choice == 1:
            if random.random() < 0.5:
                player.change_health(-20)
                return "A rock slips and hurts your knee. Health -20."
            player.experience += 20
            return "You climb across safely. Experience +20."
        if choice == 2:
            player.change_energy(-15)
            return "The detour is long and tiring. Energy -15."
        if player.has_item("Rope"):
            player.experience += 30
            return "Your Rope makes the crossing safe. Experience +30."
        player.change_health(-15)
        return "You have no Rope and slip on the rocks. Health -15."


class LostTrailEvent(RandomEvent):
    title = "Lost Trail"
    description = "The path has disappeared and you are not sure which way to go."
    choices = ["Retrace your steps", "Check your Map", "Keep going and hope for the best"]

    def resolve(self, choice, player):
        if choice == 1:
            player.change_energy(-15)
            return "You walk back and find the trail again. Energy -15."
        if choice == 2:
            if player.has_item("Map"):
                player.experience += 10
                return "Your Map shows the way. Experience +10."
            player.change_energy(-20)
            return "You do not own a Map and wander for a while. Energy -20."
        if random.random() < 0.5:
            player.experience += 15
            return "Lucky! You stumble onto an old shepherd path. Experience +15."
        player.change_health(-10)
        player.change_energy(-10)
        return "You scramble over rough ground. Health -10, Energy -10."


class WildAnimalEvent(RandomEvent):
    title = "Wild Animal"
    description = "A Himalayan snow leopard watches you from a high ridge!"
    choices = ["Stand firm and make noise", "Slowly back away", "Throw food to distract it"]
    min_altitude = 3000

    def resolve(self, choice, player):
        if choice == 1:
            if random.random() < 0.6:
                player.experience += 30
                return "The leopard runs away! Experience +30."
            player.change_health(-15)
            return "The leopard swipes at you before leaving. Health -15."
        if choice == 2:
            player.change_energy(-10)
            return "You back away safely but take a long way around. Energy -10."
        if player.has_item("Food"):
            player.lose_item("Food", 1)
            player.reputation += 5
            return "The leopard eats the food and leaves. Food -1, Reputation +5."
        player.change_health(-15)
        return "You have no food to throw! The leopard scratches you. Health -15."


class FriendlyTravelerEvent(RandomEvent):
    title = "Friendly Traveler"
    description = "You find an injured traveler sitting by the trail. They ask for help."
    choices = ["Give food", "Give water", "Ignore them", "Ask another traveler for help"]

    def resolve(self, choice, player):
        if choice == 1:
            if player.lose_item("Food", 1):
                player.reputation += 10
                return "The traveler thanks you warmly. Food -1, Reputation +10."
            return "You have no food to give. The traveler understands."
        if choice == 2:
            if player.lose_item("Water", 1):
                player.reputation += 10
                player.experience += 10
                return "The traveler is grateful. Water -1, Reputation +10, Experience +10."
            return "You have no water to give. The traveler understands."
        if choice == 3:
            player.reputation -= 5
            return "You walk past. Reputation -5."
        if random.random() < 0.5:
            player.reputation += 5
            player.experience += 10
            return "Another traveler arrives and helps. Reputation +5, Experience +10."
        player.change_energy(-10)
        return "Nobody comes and you waste time searching. Energy -10."


class BrokenShoesEvent(RandomEvent):
    title = "Broken Shoes"
    description = "The sole of your shoe has torn open."
    choices = ["Patch them with Rope", "Buy new Hiking Shoes (Rs. 800)", "Limp on"]

    def resolve(self, choice, player):
        if choice == 1:
            if player.lose_item("Rope", 1):
                player.experience += 10
                return "You tie the shoe together. Rope -1, Experience +10."
            player.change_energy(-10)
            return "You have no Rope. Walking is hard. Energy -10."
        if choice == 2:
            try:
                player.spend_money(800)
            except InsufficientMoneyError:
                player.change_energy(-10)
                return "You cannot afford new shoes. Energy -10."
            player.add_item("Hiking Shoes", 1)
            return "A local sells you sturdy shoes. Money -Rs. 800, Hiking Shoes +1."
        player.change_health(-8)
        player.change_energy(-10)
        return "Your feet get blisters. Health -8, Energy -10."


class FoodShortageEvent(RandomEvent):
    title = "Food Shortage"
    description = "A hungry mule has torn open your food bag!"
    choices = ["Chase the mule", "Let it eat", "Buy replacement food (Rs. 400)"]

    def resolve(self, choice, player):
        if choice == 1:
            player.change_energy(-10)
            lost = player.lose_item("Food", 1)
            return f"You chase it off but lose some food. Energy -10, Food -{lost}."
        if choice == 3 and player.money >= 400:
            player.money -= 400
            return "You pay Rs. 400 to replace the spoiled food. No food lost."
        lost = player.lose_item("Food", 2)
        return f"The mule eats your supplies. Food -{lost}."


class BeautifulSunriseEvent(RandomEvent):
    title = "Beautiful Sunrise"
    description = "The sun rises over the snowy peaks and turns the sky gold."

    def resolve(self, choice, player):
        player.change_energy(10)
        player.experience += 20
        return "You feel inspired and refreshed. Energy +10, Experience +20."


class HelpfulLocalEvent(RandomEvent):
    title = "Helpful Local"
    description = "A friendly local invites you into their home for tea."
    choices = ["Accept the offer", "Politely decline"]

    def resolve(self, choice, player):
        if choice == 2:
            player.reputation += 2
            return "You thank them and move on. Reputation +2."
        if player.reputation >= 20:
            player.add_item("Food", 1)
            player.change_energy(15)
            return "They remember your good name and give you a free meal. Energy +15, Food +1."
        if player.money >= 200:
            player.money -= 200
            player.change_energy(20)
            return "You pay Rs. 200 for tea and a rest. Energy +20."
        player.change_energy(10)
        return "You cannot pay, but they let you rest by the fire. Energy +10."


class SnowfallEvent(RandomEvent):
    title = "Snowfall"
    description = "Thick snow starts falling and the wind grows cold."
    choices = ["Keep walking", "Build a snow shelter", "Wait at a teahouse (Rs. 300)"]
    min_altitude = 2500

    def resolve(self, choice, player):
        if choice == 1:
            if player.has_item("Jacket"):
                player.change_energy(-5)
                return "Your Jacket keeps you warm. Energy -5."
            player.change_energy(-15)
            player.change_health(-5)
            return "The cold bites hard. Energy -15, Health -5."
        if choice == 2:
            if player.has_item("Tent"):
                player.change_energy(5)
                return "You use your Tent as a shelter and rest well. Energy +5."
            player.change_energy(-10)
            player.change_health(-3)
            return "Building a shelter by hand is hard work. Energy -10, Health -3."
        if player.money >= 300:
            player.money -= 300
            player.change_energy(5)
            return "You warm up with hot soup. Money -Rs. 300, Energy +5."
        player.change_energy(-10)
        return "You cannot afford the teahouse. Energy -10."


class BusBreakdownEvent(RandomEvent):
    title = "Bus Breakdown"
    description = "Your bus has broken down on the mountain road."
    choices = ["Wait for the repair", "Walk to the next village", "Hire a taxi (Rs. 700)"]
    max_altitude = 2000

    def resolve(self, choice, player):
        if choice == 1:
            lost_food = player.lose_item("Food", 1)
            lost_water = player.lose_item("Water", 1)
            return f"You wait for hours. Food -{lost_food}, Water -{lost_water}."
        if choice == 3 and player.money >= 700:
            player.money -= 700
            player.change_energy(5)
            return "A taxi takes you onward. Money -Rs. 700, Energy +5."
        player.change_energy(-20)
        return "You walk a long way on foot. Energy -20."


class InjuryEvent(RandomEvent):
    title = "Injury"
    description = "You twist your ankle on a loose stone."
    choices = ["Use a First Aid Kit", "Use Medicine", "Rest and walk it off", "Push on"]

    def resolve(self, choice, player):
        if choice in (1, 2):
            item_name = ["First Aid Kit", "Medicine"][choice - 1]
            if player.has_item(item_name):
                return "You treat the injury. " + player.use_item(item_name)
            player.change_health(-10)
            return f"You do not have {item_name}. The ankle hurts badly. Health -10."
        if choice == 3:
            player.change_energy(-10)
            player.change_health(-5)
            return "You rest and walk slowly. Energy -10, Health -5."
        player.change_health(-15)
        return "You push through the pain. Health -15."


class FoundMoneyEvent(RandomEvent):
    title = "Found Money"
    description = "You spot an old leather pouch near a teahouse bench."

    def resolve(self, choice, player):
        amount = random.randint(500, 2000)
        player.money += amount
        return f"Inside the pouch you find Rs. {amount:,}!"


class HiddenShortcutEvent(RandomEvent):
    title = "Hidden Shortcut"
    description = "A narrow path leaves the main trail. A local says it is a shortcut."
    choices = ["Take the shortcut", "Stay on the main trail"]

    def resolve(self, choice, player):
        if choice == 2:
            player.experience += 5
            return "You stay safe on the main trail. Experience +5."
        if random.random() < 0.6:
            player.change_energy(10)
            player.experience += 15
            return "The shortcut saves you time. Energy +10, Experience +15."
        player.change_health(-10)
        player.change_energy(-5)
        return "The shortcut is steep and slippery. Health -10, Energy -5."


class AltitudeSicknessEvent(RandomEvent):
    title = "Altitude Sickness"
    description = "You struggle to breathe at this altitude. Your head is pounding."
    choices = ["Take Medicine", "Rest and drink water", "Ignore it and keep going"]
    min_altitude = 3000

    def resolve(self, choice, player):
        if choice == 1:
            if player.lose_item("Medicine", 1):
                player.experience += 10
                return "The Medicine helps. Medicine -1, Experience +10."
            player.change_health(-10)
            return "You have no Medicine. Health -10."
        if choice == 2:
            if player.lose_item("Water", 1):
                player.change_energy(5)
                return "Slow breaths and water help. Water -1, Energy +5."
            player.change_health(-5)
            return "You have no water to drink. Health -5."
        player.change_health(-10)
        player.change_energy(-15)
        return "The sickness gets worse. Health -10, Energy -15."


EVENT_CLASSES = [
    HeavyRainEvent,
    LandslideEvent,
    LostTrailEvent,
    WildAnimalEvent,
    FriendlyTravelerEvent,
    BrokenShoesEvent,
    FoodShortageEvent,
    BeautifulSunriseEvent,
    HelpfulLocalEvent,
    SnowfallEvent,
    BusBreakdownEvent,
    InjuryEvent,
    FoundMoneyEvent,
    HiddenShortcutEvent,
    AltitudeSicknessEvent,
]


def get_random_event(altitude):
    possible_events = []
    for event_class in EVENT_CLASSES:
        event = event_class()
        if event.is_possible(altitude):
            possible_events.append(event)
    return random.choice(possible_events)
