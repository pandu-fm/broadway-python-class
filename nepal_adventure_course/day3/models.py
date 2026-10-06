from exceptions import InsufficientMoneyError, InsufficientResourceError, InvalidActionError
from utils import format_money, print_header, prompt_int

ITEM_CATALOG = {
    "Food": {"price": 150, "description": "Restores 15 Health", "effect_type": "health", "effect_value": 15},
    "Water": {"price": 50, "description": "Restores 20 Energy", "effect_type": "energy", "effect_value": 20},
    "Medicine": {"price": 500, "description": "Restores 40 Health", "effect_type": "health", "effect_value": 40},
    "First Aid Kit": {"price": 900, "description": "Restores 60 Health", "effect_type": "health", "effect_value": 60},
    "Tent": {"price": 1500, "description": "Gear: +15 extra Energy when you rest", "effect_type": "gear", "effect_value": 15},
    "Jacket": {"price": 1000, "description": "Gear: halves Energy lost to bad weather", "effect_type": "gear", "effect_value": 0},
    "Torch": {"price": 300, "description": "Gear: keeps wild animals away at night", "effect_type": "gear", "effect_value": 0},
    "Rope": {"price": 400, "description": "Gear: helps with landslides and broken shoes", "effect_type": "gear", "effect_value": 0},
    "Map": {"price": 350, "description": "Gear: stops you getting lost in fog", "effect_type": "gear", "effect_value": 0},
    "Hiking Shoes": {"price": 1200, "description": "Gear: travel costs 5 less Energy", "effect_type": "gear", "effect_value": 5},
}

ITEM_PRICES = {}
for name, details in ITEM_CATALOG.items():
    ITEM_PRICES[name] = details["price"]


class Item:
    def __init__(self, name, quantity=1):
        details = ITEM_CATALOG[name]
        self.name = name
        self.quantity = quantity
        self.price = details["price"]
        self.description = details["description"]
        self.effect_type = details["effect_type"]
        self.effect_value = details["effect_value"]

    def is_usable(self):
        return self.effect_type in ("health", "energy")

    def __str__(self):
        return f"{self.name} x{self.quantity} - {self.description}"

    def __repr__(self):
        return f"Item('{self.name}', {self.quantity})"

    def __eq__(self, other):
        return isinstance(other, Item) and self.name == other.name


class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def interact(self, player):
        return f"{self.name} greets you warmly."

    def __str__(self):
        return f"{self.name} ({self.role})"


class Guide(Person):
    def __init__(self, name, fee, next_stop):
        super().__init__(name, "Guide")
        self.fee = fee
        self.next_stop = next_stop

    def interact(self, player):
        print(f"{self.name}: \"I know a safer route. Next stop is {self.next_stop}.\"")
        try:
            player.spend_money(self.fee)
        except InsufficientMoneyError:
            return f"You cannot pay the guide's fee of {format_money(self.fee)}."
        player.safe_route = True
        player.experience += 15
        return f"You hire {self.name} for {format_money(self.fee)}. Your next trip costs less Energy. Experience +15."


class Merchant(Person):
    def __init__(self, name, price_multiplier):
        super().__init__(name, "Merchant")
        self.prices = {}
        for item_name, price in ITEM_PRICES.items():
            self.prices[item_name] = int(price * price_multiplier)

    def interact(self, player):
        print(f"{self.name}: \"I have useful equipment for your journey.\"")
        item_names = list(self.prices)
        while True:
            print_header("MERCHANT SHOP")
            print(f"Your money: {format_money(player.money)}\n")
            for number, item_name in enumerate(item_names, 1):
                description = ITEM_CATALOG[item_name]["description"]
                print(f"{number:>2}. {item_name:<14} {format_money(self.prices[item_name]):>10}   {description}")
            print(" 0. Leave the shop")
            choice = prompt_int("\nBuy which item? ", 0, len(item_names))
            if choice == 0:
                return f"You thank {self.name} and leave the shop."
            item_name = item_names[choice - 1]
            quantity = prompt_int("How many? (1-10): ", 1, 10)
            try:
                player.spend_money(self.prices[item_name] * quantity)
            except InsufficientMoneyError as error:
                print(f"\n{error}")
            else:
                player.add_item(item_name, quantity)
                print(f"\nYou bought {quantity} x {item_name}.")


class Traveler(Person):
    def __init__(self, name, story):
        super().__init__(name, "Traveler")
        self.story = story

    def interact(self, player):
        player.reputation += 5
        return f"{self.name}: \"{self.story}\" You share tea and trail stories. Reputation +5."


class Local(Person):
    def __init__(self, name, advice):
        super().__init__(name, "Local")
        self.advice = advice

    def interact(self, player):
        player.change_energy(10)
        return f"{self.name}: \"{self.advice}\" You enjoy warm butter tea. Energy +10."


class Player:
    def __init__(self, name, age, destination):
        self.name = name
        self.age = age
        self.destination = destination
        self.location = "Kathmandu"
        self.health = 100
        self.energy = 100
        self.money = 10000
        self.inventory = [Item("Food", 5), Item("Water", 5), Item("Medicine", 1), Item("Torch", 1)]
        self.experience = 0
        self.reputation = 10
        self.distance_traveled = 0
        self.days_survived = 1
        self.safe_route = False

    @property
    def food(self):
        return self.count_item("Food")

    @property
    def water(self):
        return self.count_item("Water")

    def change_health(self, amount):
        self.health = max(0, min(100, self.health + amount))

    def change_energy(self, amount):
        self.energy = max(0, min(100, self.energy + amount))

    def spend_money(self, amount):
        if amount > self.money:
            raise InsufficientMoneyError(
                f"You need {format_money(amount)} but you only have {format_money(self.money)}."
            )
        self.money -= amount

    def count_item(self, name):
        return sum(item.quantity for item in self.inventory if item.name == name)

    def has_item(self, name):
        return self.count_item(name) > 0

    def add_item(self, name, quantity=1):
        for item in self.inventory:
            if item.name == name:
                item.quantity += quantity
                return
        self.inventory.append(Item(name, quantity))

    def remove_item(self, name, quantity=1):
        for item in self.inventory:
            if item.name == name and item.quantity >= quantity:
                item.quantity -= quantity
                if item.quantity == 0:
                    self.inventory.remove(item)
                return
        raise InsufficientResourceError(f"You do not have enough {name}.")

    def lose_item(self, name, quantity=1):
        quantity_to_lose = min(quantity, self.count_item(name))
        if quantity_to_lose > 0:
            self.remove_item(name, quantity_to_lose)
        return quantity_to_lose

    def use_item(self, name):
        if not self.has_item(name):
            raise InsufficientResourceError(f"You do not have any {name}.")
        item = next(item for item in self.inventory if item.name == name)
        if not item.is_usable():
            raise InvalidActionError(f"{name} is gear. It helps you automatically, so you cannot use it.")
        if item.effect_type == "health":
            self.change_health(item.effect_value)
            result = f"You used {name}. Health +{item.effect_value}."
        else:
            self.change_energy(item.effect_value)
            result = f"You used {name}. Energy +{item.effect_value}."
        self.remove_item(name)
        return result

    def pass_day(self):
        self.days_survived += 1
        messages = []
        if self.has_item("Food"):
            self.remove_item("Food")
            messages.append("Food -1.")
        else:
            self.change_health(-15)
            messages.append("No Food left! Health -15.")
        if self.has_item("Water"):
            self.remove_item("Water")
            messages.append("Water -1.")
        else:
            self.change_energy(-20)
            messages.append("No Water left! Energy -20.")
        return " ".join(messages)

    def to_dict(self):
        inventory = []
        for item in self.inventory:
            inventory.append({"name": item.name, "quantity": item.quantity})
        return {
            "name": self.name,
            "age": self.age,
            "destination": self.destination,
            "location": self.location,
            "health": self.health,
            "energy": self.energy,
            "money": self.money,
            "inventory": inventory,
            "experience": self.experience,
            "reputation": self.reputation,
            "distance_traveled": self.distance_traveled,
            "days_survived": self.days_survived,
            "safe_route": self.safe_route,
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(str(data["name"]), int(data["age"]), str(data["destination"]))
        player.location = str(data["location"])
        player.health = int(data["health"])
        player.energy = int(data["energy"])
        player.money = int(data["money"])
        player.inventory = []
        for entry in data["inventory"]:
            player.inventory.append(Item(entry["name"], int(entry["quantity"])))
        player.experience = int(data["experience"])
        player.reputation = int(data["reputation"])
        player.distance_traveled = int(data["distance_traveled"])
        player.days_survived = int(data["days_survived"])
        player.safe_route = bool(data["safe_route"])
        return player

    def __len__(self):
        return sum(item.quantity for item in self.inventory)

    def __str__(self):
        return (f"{self.name} (age {self.age}) | Health {self.health} | Energy {self.energy} "
                f"| {format_money(self.money)} | at {self.location}")

    def __repr__(self):
        return f"Player('{self.name}', {self.age}, '{self.destination}')"
