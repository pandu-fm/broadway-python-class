import random

from locations import build_nepal_map
from models import Guide, Local, Merchant, Player, Traveler

DESTINATION = "Muktinath"


def ask_number(prompt_text, minimum, maximum):
    while True:
        answer = input(prompt_text).strip()
        if not answer.isdigit():
            print("Please type a number.")
            continue
        number = int(answer)
        if minimum <= number <= maximum:
            return number
        print(f"Please choose a number from {minimum} to {maximum}.")


def show_status(player, map_data):
    location = map_data[player.location]
    print("\n========================================")
    print("             PLAYER STATUS")
    print("========================================")
    print(player)
    print(f"Destination : {player.destination}")
    print(f"Altitude    : {location.altitude}m")
    print(f"💰 Money    : Rs. {player.money:,}")
    print(f"🍎 Food     : {player.food}")
    print(f"💧 Water    : {player.water}")
    print(f"🤝 Reputation: {player.reputation}")
    print(f"Day {player.days_survived}")
    print(f"Supplies carried: {len(player)}")
    print("========================================")


def show_map(player, map_data):
    print("\n🗺️ NEPAL MAP")
    for name, location in map_data.items():
        marker = " <-- YOU ARE HERE" if name == player.location else ""
        print(f"{name} | {location.altitude}m | {location.difficulty}{marker}")
        print(f"    Paths to: {', '.join(location.neighbors)}")


def travel(player, map_data):
    current = map_data[player.location]
    names = list(current.neighbors)
    print("\nWhere do you want to go?")
    for number, name in enumerate(names, 1):
        target = map_data[name]
        print(f"{number}. {name:<20} {target.altitude}m | {target.difficulty} | "
              f"Cost: Rs. {target.travel_cost} | Energy: {target.energy_cost()}")
    print("0. Stay here")
    choice = ask_number("Choose: ", 0, len(names))
    if choice == 0:
        return
    target = map_data[names[choice - 1]]
    if player.energy < target.energy_cost():
        print("You are too tired. Try resting first.")
        return
    if player.money < target.travel_cost:
        print("You do not have enough money for that trip.")
        return
    player.change_energy(-target.energy_cost())
    player.money -= target.travel_cost
    player.location = target.name
    print(f"\n🚶 You travel to {target.name} ({target.altitude}m).")
    player.pass_day()
    print(f"Day {player.days_survived} begins.")


def rest(player):
    print("\n⛺ You set up camp for the night.")
    player.change_energy(30)
    player.change_health(10)
    player.pass_day()
    print(f"Energy +30, Health +10. Day {player.days_survived} begins.")


def talk_to_npc(player):
    people = [
        Guide("Pasang Sherpa", 300),
        Merchant("Pema the Shopkeeper"),
        Traveler("John from Canada"),
        Local("Kanchi Maya"),
    ]
    person = random.choice(people)
    print(f"\n🗣️ You meet {person}.")
    print(person.interact(player))


def play_game(player, map_data):
    while True:
        print(f"\n--- {player.location} | Day {player.days_survived} | ❤️ {player.health} ⚡ {player.energy} ---")
        print("1. Travel")
        print("2. Rest")
        print("3. Talk to NPC")
        print("4. Status")
        print("5. Map")
        print("6. Exit")
        choice = ask_number("Choose: ", 1, 6)
        if choice == 1:
            travel(player, map_data)
        elif choice == 2:
            rest(player)
        elif choice == 3:
            talk_to_npc(player)
        elif choice == 4:
            show_status(player, map_data)
        elif choice == 5:
            show_map(player, map_data)
        else:
            print("\nGoodbye, trekker!")
            return
        if player.health <= 0:
            print("\n💀 Your health reached zero. The journey is over.")
            return
        if player.location == DESTINATION:
            print(f"\n🎉 You reached {DESTINATION}! You created your own game world!")
            return


def main():
    print("========================================")
    print("          🏔️ NEPAL ADVENTURE")
    print("========================================")
    name = input("\nEnter your name: ").strip() or "Trekker"
    age = ask_number("Enter your age (10-90): ", 10, 90)
    player = Player(name, age, DESTINATION)
    map_data = build_nepal_map()
    print(f"\nWelcome, {player.name}! Your goal is {DESTINATION}.")
    play_game(player, map_data)


main()
