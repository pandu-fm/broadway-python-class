# Nepal Adventure: 4-Day Teacher Guide

Each day has its own runnable folder. Students start a day from the previous day's finished code and add that day's ideas.

| Day | Folder | Run it with |
| --- | --- | --- |
| 1 | `day1/` | `cd day1` then `python main.py` |
| 2 | `day2/` | `cd day2` then `python main.py` |
| 3 | `day3/` | `cd day3` then `python main.py` |
| 4 | `../nepal_adventure/` (the finished game) | `cd ../nepal_adventure` then `python main.py` |

Requirements: Python 3.9 or newer, standard library only, and a terminal that can show emoji.

The code in these folders has no comments on purpose. Use the names of functions and classes to explain it. If you want students to take notes, ask them to write their own.

---

## How to open Day 1

Run the finished game from `../nepal_adventure/` for two minutes. Do not explain it yet. Then say:

> "Imagine you have four days to build your own Python game. We are going to build this from zero. Today we make the player. Tomorrow we build the world. On Day 3 we add danger and randomness. On Day 4 you turn it into your own game."

---

## Day 1: Build the Adventure

**Folder:** `day1/` (one file, `main.py`, about 100 lines)

**Goal:** a working game on day one.

**Concepts:** variables, `input`, conditions, loops, functions, a first small class.

**What is in the finished Day 1 code**
- A welcome screen and name prompt
- `Player` class with health, energy, money and location
- `ask_number()` so that letters and wrong numbers never crash the game
- A menu loop: Travel, Rest, Status, Exit
- A fixed route: Kathmandu, Pokhara, Jomsom, Muktinath

**Suggested order for the lesson**
1. Print the title and ask for the name.
2. Store health, energy and money in plain variables. Print the status.
3. Wrap the status in a function.
4. Add the menu loop with `while True`.
5. Add Travel using a list (`ROUTE`) and `index()`.
6. Show the problem of passing many variables around, then introduce `Player`.
7. Add `ask_number()` after someone types `abc`.

**Checkpoint:** a student can walk from Kathmandu to Muktinath.

**Achievement:** "I have a working game!"

---

## Day 2: Create the World

**Folder:** `day2/` (`main.py`, `models.py`, `locations.py`)

**Goal:** turn a straight line into a small world with people in it.

**Concepts:** classes and objects, constructors, dictionaries, inheritance, polymorphism, dunder methods, splitting code into modules.

**What is new compared to Day 1**
- `Location` class with altitude, difficulty, travel cost and a plain list of neighbors
- A small map of 8 places in two routes. Each place lists the places you can reach from it, so not every place connects to every other place.
- Food, Water and Reputation on the `Player`
- `Person` with `Guide`, `Merchant`, `Traveler` and `Local`. Each has its own `interact()`.
- `__str__`, `__repr__`, `__len__` on `Player`, `__eq__` on `Person`

**Good teaching moment:** put four different NPC objects in one list and call `interact()` on each in a loop. The same call gives four different results. That is polymorphism.

**Checkpoint:** a student can travel across the map and talk to different NPCs.

**Achievement:** "I created my own game world!"

---

## Day 3: Make the Game Unpredictable

**Folder:** `day3/` (`main.py`, `game.py`, `models.py`, `events.py`, `locations.py`, `storage.py`, `exceptions.py`, `utils.py`)

**Goal:** every journey is different.

**Concepts:** the `random` module, class inheritance in a second place (events), exceptions, custom exceptions, `try` / `except`, file handling, JSON.

**What is new compared to Day 2**
- A bigger map of 15 places. `Location` now also has temperature, distance and activities. Give students this `locations.py` to read and use, not to type.
- `Weather` (6 kinds) and the altitude rules in `locations.py`
- 15 random events in `events.py`. Each one is a small class that extends `RandomEvent`.
- `Item` and an inventory. Food and Water are now items.
- `exceptions.py` and the `try` / `except` in `GameEngine.play`
- Save and load in `storage.py`
- A `GameEngine` class that holds the game loop

**Good teaching moments**
- Ask the class to type `abc`, `hello`, `-50` and `999999` at every prompt. Show how `prompt_int` handles all four.
- Open `data/savegame.json` and read it together.
- Add one new event live. Copy an existing event class, change the text, add it to `EVENT_CLASSES`.

**Checkpoint:** travel, weather, a random event, a decision, health and energy changes, and an inventory that changes.

**Achievement:** "Every game is different!"

---

## Day 4: Become a Python Developer

**Folder:** `../nepal_adventure/` (the finished game)

**Goal:** use more advanced Python to make the code cleaner, then make the game their own.

Day 3 is the finished Day 4 code with these five things taken out. Students add them back one by one. Each is a short, separate exercise.

| Topic | What students add | Where |
| --- | --- | --- |
| List comprehension | Replace the loops that build lists. Start with the usable items in `use_item`, then the possible events in `get_random_event`. | `game.py`, `events.py` |
| Dictionary comprehension | Replace the loops that build `ITEM_PRICES` and `Merchant.prices`. | `models.py` |
| Lambda | Save scores to `leaderboard.json` and sort them with `sorted(..., key=lambda entry: entry["score"], reverse=True)`. Add "Leaderboard" to the main menu. | `storage.py`, `main.py` |
| Generator | `find_route` and `journey`. `journey` yields each stop and the kilometers to it. Use it for the shortest-route line on the map and for the Guide's next stop. | `locations.py`, `game.py` |
| Decorator | `write_log` and `@log_action`. Put the decorator above `travel`, `rest`, `eat`, `drink`, `explore`, `use_item` and `talk_to_npc`. Read `logs/game.log` afterwards. | `utils.py`, `game.py` |

After these five, add the scoring and endings (`calculate_score`, `complete_journey`, `finish_game` in `game.py`) so a journey ends with a rank and a leaderboard entry.

**Suggested order:** list comprehension, dictionary comprehension, lambda, generator, decorator. Each builds on something students already know from earlier days.

### Final challenge (30 to 60 minutes)

Stop teaching. Let students customize their own game. Ideas:

- 🏴 A secret location (add a `Location` to `build_nepal_map` and add its name to a neighbor's list)
- 💎 Hidden treasure (a new explore outcome in `EXPLORE_OUTCOMES`)
- 🐅 A new wildlife encounter (a new `RandomEvent` class)
- 🏕️ Camping bonuses (change `GameEngine.rest`)
- ❤️ A reputation reward (check `player.reputation` in an event)
- 🗺️ A secret route
- 💀 A new ending
- 👻 A mystery event
- 🏆 Achievements, such as "Never rested" or "Reached Everest in 8 days"

Then everyone runs their game for the class.

---

## Tips for the classroom

- **Run before you teach.** Play each day's finished folder once before class.
- **Keep the same folder names.** Students can switch to the finished folder if they fall behind.
- **Data folders are created automatically.** `data/` and `logs/` appear the first time a game runs. Delete them any time to reset.
- **Slow starters:** after Day 2, give them the `day3/` folder and let them read it instead of typing it.
- **Fast finishers:** ask them to add a new destination, more NPCs or difficulty levels.
