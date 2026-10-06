# 🏔️ Nepal Adventure & Survival Simulator

## Description

A text adventure you play in the terminal. You are a trekker who starts in Kathmandu and must reach a famous place in Nepal such as Muktinath or Everest Base Camp.

On the way you walk between towns, deal with weather and thin mountain air, meet people, and make choices when things go wrong. Look after your health, energy, food, water and money, or the journey will end early.

It was built as a 4-day classroom project for beginner and intermediate Python students. The code has no comments on purpose. Names of files, classes and functions are chosen so the code explains itself.

---

## Features

- 5 destinations with different difficulty, distance and altitude
- 15 locations connected by a simple map (not every town connects to every other town)
- Altitude system with altitude sickness
- 6 kinds of weather that change from day to day
- 15 random events, most of them with choices that have trade-offs
- 10 items you can find, buy and use
- 4 kinds of NPCs: Guide, Merchant, Traveler and Local
- Daily survival: every night uses 1 Food and 1 Water
- Save and load with JSON, safe against missing or damaged files
- Leaderboard saved to a JSON file
- Action log saved to `logs/game.log`
- Several different endings and a final rank

---

## Requirements

- Python 3.9 or newer
- No extra packages. Only the Python standard library is used.
- A terminal that can show emoji (Windows Terminal, VS Code terminal, macOS Terminal, Linux terminal)

---

## Installation

1. Download or clone the project so you have a folder called `nepal_adventure`.
2. Open a terminal in that folder.
3. Check your Python version:

```bash
python --version
```

4. Start the game:

```bash
python main.py
```

On some systems the command is `python3` instead of `python`.

The folders `data/` and `logs/` are created automatically the first time you run the game.

---

## How to Play

### 1. Create a player

```
Enter your name: Arjun
Enter your age (10-90): 25
```

If you type something invalid (like letters for your age) the game asks again. It never crashes on normal mistakes.

### 2. Choose a destination

```
1. Muktinath              3800m | 400 km | Medium
   Recommended gear: Hiking Shoes, Jacket
2. Langtang Valley        3430m | 160 km | Medium
...
```

Harder destinations are higher and further away, but give more points.

### 3. Take actions each day

Every turn you choose from the action menu (see Controls below).

- **Travel**: walk to a connected location. It costs money, energy and one day.
- **Rest**: gain energy and health, but use a day.
- **Eat / Drink**: use Food (restores Health) or Water (restores Energy).
- **Explore**: search the area. You might find money, food, medicine or a hidden path, or get hurt.
- **Talk to NPC**: meet the people nearby. Merchants sell items.
- **Use Item**: use Medicine, First Aid Kit, Food or Water.

### 4. Handle random events

After travelling, an event can happen:

```
========================================
            🎲 RANDOM EVENT
========================================
** Heavy Rain **

A heavy rain has started. The trail turns to mud.

1. Continue walking
2. Find shelter
3. Turn back to the last teahouse

Choose:
```

There is not always one best answer. Each choice costs or gives something different.

### 5. Save, load, and finish

- Choose `0` in the action menu to save and go back to the main menu.
- Choose `Load Game` in the main menu to continue.
- Reach your destination to see your ending, rank and score.

---

## Game Rules

| Thing | Rule |
| --- | --- |
| Health | Starts at 100. If it reaches 0 you die and the journey fails. |
| Energy | Starts at 100. Travelling and exploring use energy. At 0 you collapse and lose Health. |
| Food and Water | Every night uses 1 Food and 1 Water. No Food: Health -15. No Water: Energy -20. |
| Money | Starts at Rs. 10,000. Travel and shopping cost money. |
| Days | You have 25 days. After that the season ends and you must turn back. |
| Altitude | Below 2500 m: normal. 2500 m and above: travel uses more energy. 3500 m and above: altitude sickness can happen. 4500 m and above: sickness is very likely and hurts more. |
| Weather | Sunny and Cloudy are easy. Rainy, Snowy and Storm cost energy. Fog can make you lose the trail. Storms can injure you. A Jacket halves the energy lost to weather, and a Map stops you getting lost in fog. |
| Gear | Hiking Shoes make travel cheaper. A Tent makes resting better. A Torch keeps animals away at night. A Rope helps in landslides. |

### Ways the journey can end

| Ending | When |
| --- | --- |
| 🏆 Legendary Explorer | You reach your destination in excellent condition. |
| 🥾 Successful Adventurer | You reach your destination. |
| 😰 Barely Survived | You reach your destination with almost no resources. |
| 🚨 Expedition Abandoned | You choose to turn back, you run out of days, or you have no food or water for 3 nights in a row. |
| 💀 Journey Failed | Your health reaches 0. |

### Scoring

Points are added for distance travelled, experience, health, energy, reputation, events survived, items found and days survived. Reaching your destination gives a big bonus, bigger for harder destinations.

Points are taken away for injuries, resting more than 5 times, running out of food or water, and dying.

Final rank: 🏆 LEGENDARY EXPLORER, 🥇 MASTER ADVENTURER, 🥈 GREAT SURVIVOR, 🥉 SURVIVOR, or 💀 JOURNEY FAILED.

---

## Controls

Everything uses numbers. Type the number and press Enter.

Main menu:

```
1. New Game
2. Load Game
3. Leaderboard
4. Exit
```

Action menu:

```
1. Travel
2. Rest
3. Eat
4. Drink
5. Explore
6. Talk to NPC
7. Use Item
8. View Status
9. View Map
10. View Inventory
11. Abandon Expedition
0. Save and return to main menu
```

---

## Project Structure

```
nepal_adventure/
├── main.py          Start here. Main menu, new player, leaderboard screen.
├── models.py        Item, Player and the NPC classes (Person, Guide, Merchant, Traveler, Local).
├── game.py          GameEngine: the daily loop, travel, rest, explore, scoring and endings.
├── events.py        The 15 random events. Each event is a small class.
├── locations.py     Weather, Location, the map of Nepal, route finding and altitude rules.
├── storage.py       Saving and loading the game and the leaderboard (JSON files).
├── exceptions.py    Custom errors such as InsufficientMoneyError.
├── utils.py         Logging decorator, safe input helpers and screen helpers.
├── README.md        This file.
├── data/            Created automatically. Holds savegame.json and leaderboard.json.
└── logs/            Created automatically. Holds game.log.
```

---

## Python Concepts Demonstrated

| Concept | Where to look |
| --- | --- |
| Variables and data types | everywhere (`int`, `str`, `float`, `bool`) |
| Conditions | `if`, `elif`, `else` in `events.py` and `game.py` |
| Loops | `while` in `main.py` and `GameEngine.play`, `for` in menus |
| Functions | `prompt_int`, `build_nepal_map`, `find_route` |
| Lists | `Player.inventory`, `EVENT_CLASSES` |
| Tuples | `RANKS` in `game.py` and the stops yielded by `journey()` in `locations.py` |
| Sets | `visited` in `find_route`, `REQUIRED_ENTRY_KEYS` in `storage.py` |
| Dictionaries | `ITEM_CATALOG`, `DESTINATIONS`, `Weather.EFFECTS`, and the map (`build_nepal_map`) |
| List comprehension | `get_random_event`, `GameEngine.use_item` |
| Dictionary comprehension | `ITEM_PRICES` in `models.py`, `Merchant.prices` |
| Lambda | leaderboard sorting in `storage.py` |
| Classes and objects | `Player`, `Item`, `Location`, `Weather` |
| Constructors | every `__init__` |
| Encapsulation | `Player` methods like `spend_money` and `change_health` protect the rules |
| Inheritance | `Guide`, `Merchant`, `Traveler`, `Local` extend `Person`; each event extends `RandomEvent` |
| Polymorphism | every NPC has its own `interact()`; every event has its own `resolve()` |
| Dunder methods | `__str__`, `__repr__`, `__eq__`, `__len__` in `models.py` |
| Properties | `Player.food` and `Player.water` |
| Exception handling | `try` / `except` in `game.py`, `storage.py`, `utils.py` |
| Custom exceptions | `exceptions.py` |
| File handling and JSON | `storage.py` |
| Random | `random.choice`, `random.random`, `random.choices` |
| Decorators | `@log_action` in `utils.py` |
| Generators | `journey()` in `locations.py` yields each stop on a route |
| Modules | the project is split into several files |

---

## Example Gameplay

```
========================================
          🏔️ NEPAL ADVENTURE
========================================

1. New Game
2. Load Game
3. Leaderboard
4. Exit

Choose: 1
Enter your name: Arjun
Enter your age (10-90): 25
Choose: 1

--- Kathmandu | Day 1 | Weather: Sunny | ❤️ 100 ⚡ 100 ---
Choose action: 1

Where do you want to go?
1. Pokhara    200 km | 822m | Cost: Rs. 500 | Energy: 20
2. Syabrubesi 120 km | 1550m | Cost: Rs. 600 | Energy: 20
3. Lukla      130 km | 2860m | Cost: Rs. 5,000 | Energy: 25
0. Stay here
Choose: 1

🚶 You travel to Pokhara (822m).
Weather: Sunny - Clear skies. Perfect trekking weather.

🌙 Night falls. Food -1. Water -1.
☀️ Day 2 begins.
...
========================================
           THE JOURNEY ENDS
========================================
Ending  : 🥾 Successful Adventurer
You reached Muktinath.

Rank        : 🥈 GREAT SURVIVOR
Final score : 612
```

---

## Future Improvements

Ideas for students to add:

- Secret locations and hidden treasure
- A reputation system that unlocks special NPCs
- More NPCs and more destinations
- More random events
- Difficulty levels (easy, normal, hard)
- Achievements such as "Never rested" or "Reached Everest in 8 days"
- A shop in more towns with different prices
