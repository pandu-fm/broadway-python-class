import json
import os

from locations import DESTINATIONS, build_nepal_map
from models import Player
from utils import DATA_DIR, ensure_directories, write_log

SAVE_FILE = os.path.join(DATA_DIR, "savegame.json")
LEADERBOARD_FILE = os.path.join(DATA_DIR, "leaderboard.json")
REQUIRED_ENTRY_KEYS = {"name", "score", "destination", "outcome"}


def save_game(player):
    ensure_directories()
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as save_file:
            json.dump(player.to_dict(), save_file, indent=4)
    except (OSError, TypeError):
        write_log("Saving the game failed")
        return False
    write_log(f"{player.name} saved the game")
    return True


def load_game():
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as save_file:
            player = Player.from_dict(json.load(save_file))
    except (OSError, ValueError, KeyError, TypeError):
        write_log("No valid save file could be loaded")
        return None
    if player.location not in build_nepal_map() or player.destination not in DESTINATIONS:
        write_log("Save file had an unknown location or destination")
        return None
    write_log(f"{player.name} loaded the saved game")
    return player


def get_leaderboard():
    try:
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as leaderboard_file:
            entries = json.load(leaderboard_file)
    except (OSError, ValueError):
        return []
    if not isinstance(entries, list):
        return []
    return [entry for entry in entries if isinstance(entry, dict) and REQUIRED_ENTRY_KEYS <= entry.keys()]


def save_leaderboard(name, score, destination, outcome):
    ensure_directories()
    entries = get_leaderboard()
    entries.append({"name": name, "score": score, "destination": destination, "outcome": outcome})
    entries = sorted(entries, key=lambda entry: entry["score"], reverse=True)[:10]
    try:
        with open(LEADERBOARD_FILE, "w", encoding="utf-8") as leaderboard_file:
            json.dump(entries, leaderboard_file, indent=4)
    except OSError:
        write_log("Saving the leaderboard failed")
