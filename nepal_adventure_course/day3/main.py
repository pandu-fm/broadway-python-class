from game import GameEngine
from locations import DESTINATIONS, build_nepal_map
from models import Player
from storage import load_game
from utils import clear_screen, ensure_directories, format_money, print_header, prompt_int, prompt_string


def display_main_menu():
    print_header("🏔️ NEPAL ADVENTURE")
    print("\n1. New Game")
    print("2. Load Game")
    print("3. Exit\n")


def create_player():
    clear_screen()
    print_header("CREATE YOUR TREKKER")
    name = prompt_string("Enter your name: ")
    age = prompt_int("Enter your age (10-90): ", 10, 90)
    map_data = build_nepal_map()
    destination_names = list(DESTINATIONS)
    print("\nChoose your destination:\n")
    for number, destination_name in enumerate(destination_names, 1):
        details = DESTINATIONS[destination_name]
        goal = map_data[details["location"]]
        print(f"{number}. {destination_name:<22} {goal.altitude}m | {details['difficulty']}")
        print(f"   Recommended gear: {details['gear']}")
    choice = prompt_int("\nChoose: ", 1, len(destination_names))
    return Player(name, age, destination_names[choice - 1])


def confirm_start(player):
    clear_screen()
    print_header("🏔️ NEPAL ADVENTURE")
    print("\nYou are standing in Kathmandu.")
    print(f"\nYour destination is {player.destination}.")
    print("\nYou have:")
    print(f"❤️ {player.health} Health")
    print(f"⚡ {player.energy} Energy")
    print(f"💰 {format_money(player.money)}")
    print(f"🍎 {player.food} Food")
    print(f"💧 {player.water} Water")
    print("\nBut you don't know what will happen on the journey...")
    print("\nDo you want to begin?\n")
    print("1. YES")
    print("2. NO")
    return prompt_int("\nChoose: ", 1, 2) == 1


def start_new_game():
    player = create_player()
    if confirm_start(player):
        GameEngine(player).play()


def continue_saved_game():
    player = load_game()
    if player is None:
        print("\nNo valid saved game was found. The save file is missing or damaged.")
        input("\nPress Enter to return to the main menu...")
        return
    print(f"\nWelcome back, {player.name}!")
    GameEngine(player).play()


def main():
    ensure_directories()
    try:
        while True:
            clear_screen()
            display_main_menu()
            choice = prompt_int("Choose: ", 1, 3)
            if choice == 1:
                start_new_game()
            elif choice == 2:
                continue_saved_game()
            else:
                break
    except (KeyboardInterrupt, EOFError):
        print()
    print("Thank you for playing Nepal Adventure! Namaste 🙏")


if __name__ == "__main__":
    main()
