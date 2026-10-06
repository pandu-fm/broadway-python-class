import random


class Player:
    def __init__(self, name, age, destination):
        self.name = name
        self.age = age
        self.destination = destination
        self.location = "Kathmandu"
        self.health = 100
        self.energy = 100
        self.money = 10000
        self.food = 5
        self.water = 5
        self.reputation = 10
        self.days_survived = 1

    def change_health(self, amount):
        self.health = max(0, min(100, self.health + amount))

    def change_energy(self, amount):
        self.energy = max(0, min(100, self.energy + amount))

    def pass_day(self):
        self.days_survived += 1
        if self.food > 0:
            self.food -= 1
        else:
            self.change_health(-15)
            print("No Food left! Health -15.")
        if self.water > 0:
            self.water -= 1
        else:
            self.change_energy(-20)
            print("No Water left! Energy -20.")

    def __len__(self):
        return self.food + self.water

    def __str__(self):
        return f"{self.name} | Health {self.health} | Energy {self.energy} | at {self.location}"

    def __repr__(self):
        return f"Player('{self.name}', {self.age}, '{self.destination}')"


class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def interact(self, player):
        return f"{self.name} greets you warmly."

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name and self.role == other.role

    def __str__(self):
        return f"{self.name} ({self.role})"


class Guide(Person):
    def __init__(self, name, fee):
        super().__init__(name, "Guide")
        self.fee = fee

    def interact(self, player):
        print(f"{self.name}: \"I know a safer route.\"")
        if player.money < self.fee:
            return f"You cannot pay the guide's fee of Rs. {self.fee}."
        player.money -= self.fee
        player.change_energy(20)
        return f"The guide shows you a shortcut. Money -Rs. {self.fee}, Energy +20."


class Merchant(Person):
    def __init__(self, name):
        super().__init__(name, "Merchant")

    def interact(self, player):
        print(f"{self.name}: \"I have equipment for you. Food and Water, Rs. 100 each.\"")
        if player.money < 200:
            return "You do not have enough money to buy anything."
        player.money -= 200
        player.food += 1
        player.water += 1
        return "You buy 1 Food and 1 Water. Money -Rs. 200."


class Traveler(Person):
    def __init__(self, name):
        super().__init__(name, "Traveler")

    def interact(self, player):
        player.reputation += 5
        story = random.choice([
            "Don't go ahead. There's a storm.",
            "The trail ahead is steep, so save your energy.",
            "I heard a landslide blocked the road last week.",
        ])
        return f"{self.name}: \"{story}\" Reputation +5."


class Local(Person):
    def __init__(self, name):
        super().__init__(name, "Local")

    def interact(self, player):
        player.change_energy(10)
        return f"{self.name}: \"There is a small shelter nearby.\" You drink warm tea. Energy +10."
