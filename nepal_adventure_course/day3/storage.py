import json
import os

from locations import DESTINATIONS, build_nepal_map
from models import Player
from utils import DATA_DIR, ensure_directories

SAVE_FILE = os.path.join(DATA_DIR, "savegame.json")


def save_game(player):
    ensure_directories()
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as save_file:
            json.dump(player.to_dict(), save_file, indent=4)
    except (OSError, TypeError):
        return False
    return True


def load_game():
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as save_file:
            player = Player.from_dict(json.load(save_file))
    except (OSError, ValueError, KeyError, TypeError):
        return None
    if player.location not in build_nepal_map() or player.destination not in DESTINATIONS:
        return None
    return player
