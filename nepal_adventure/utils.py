import functools
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "game.log")


def ensure_directories():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)


def write_log(message):
    ensure_directories()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(f"[{timestamp}] [LOG] {message}\n")
    except OSError:
        pass


def log_action(action):
    @functools.wraps(action)
    def wrapper(self, *args, **kwargs):
        start_location = self.player.location
        result = action(self, *args, **kwargs)
        end_location = self.player.location
        if start_location != end_location:
            write_log(f"{self.player.name} travelled from {start_location} to {end_location}")
        else:
            write_log(f"{self.player.name} did '{action.__name__}' at {end_location}")
        return result
    return wrapper


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_header(title):
    print("=" * 40)
    print(title.center(40))
    print("=" * 40)


def format_money(amount):
    return f"Rs. {amount:,}"


def prompt_int(prompt_text, minimum, maximum):
    while True:
        answer = input(prompt_text).strip()
        try:
            number = int(answer)
        except ValueError:
            print("That is not a number. Please type digits only.")
            continue
        if minimum <= number <= maximum:
            return number
        print(f"Please choose a number from {minimum} to {maximum}.")


def prompt_string(prompt_text, max_length=15):
    while True:
        answer = input(prompt_text).strip()
        if not answer:
            print("This cannot be empty. Please try again.")
        elif len(answer) > max_length:
            print(f"Please use {max_length} characters or fewer.")
        else:
            return answer


def prompt_yes_no(prompt_text):
    while True:
        answer = input(prompt_text + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type y or n.")
