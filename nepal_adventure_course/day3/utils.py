import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def ensure_directories():
    os.makedirs(DATA_DIR, exist_ok=True)


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
