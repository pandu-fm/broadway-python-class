ROUTE = ["Kathmandu", "Pokhara", "Jomsom", "Muktinath"]


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 100
        self.money = 10000
        self.location = "Kathmandu"

    def show_status(self):
        print("\n================================")
        print(f"Player   : {self.name}")
        print(f"❤️ Health : {self.health}")
        print(f"⚡ Energy : {self.energy}")
        print(f"💰 Money  : Rs. {self.money}")
        print(f"📍 Location: {self.location}")
        print("================================")


def ask_number(prompt_text, minimum, maximum):
    while True:
        answer = input(prompt_text)
        if not answer.isdigit():
            print("Please type a number.")
            continue
        number = int(answer)
        if minimum <= number <= maximum:
            return number
        print(f"Please choose a number from {minimum} to {maximum}.")


def show_menu():
    print("\n1. Travel")
    print("2. Rest")
    print("3. Status")
    print("4. Exit")


def travel(player):
    position = ROUTE.index(player.location)
    if position == len(ROUTE) - 1:
        print("You are already at your destination!")
        return
    if player.energy < 20:
        print("You are too tired to travel. Try resting first.")
        return
    player.location = ROUTE[position + 1]
    player.energy -= 20
    player.money -= 500
    print(f"\n🚶 You travel to {player.location}.")
    print("Energy -20, Money -Rs. 500")


def rest(player):
    player.energy = min(100, player.energy + 30)
    player.health = min(100, player.health + 10)
    print("\n⛺ You rest for the night. Energy +30, Health +10")


def play_game(player):
    while True:
        show_menu()
        choice = ask_number("\nChoose: ", 1, 4)
        if choice == 1:
            travel(player)
        elif choice == 2:
            rest(player)
        elif choice == 3:
            player.show_status()
        else:
            print("\nGoodbye, trekker!")
            break
        if player.location == "Muktinath":
            print("\n🎉 You reached Muktinath! You have a working game!")
            break


def main():
    print("================================")
    print("      🏔️ NEPAL ADVENTURE")
    print("================================")
    name = input("\nEnter your name: ")
    player = Player(name)
    print(f"\nWelcome, {player.name}!")
    player.show_status()
    play_game(player)


main()
