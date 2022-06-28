import json
import os
import re
import sys

from handlers import handle_results
from constants import (
    KILL_LINE_PATTERN,
    START_GAME_PATTERN,
    WORLD_PLAYER
)

GAMES = {}
CURRENT_GAME_KEY = ""
NUMBER_OF_GAMES = 0


def get_death_data(kill_line):
    half_log = kill_line.split("killed")
    third_log = half_log[1].split("by")

    return half_log[0].split(":")[-1].strip(), third_log[0].strip(), third_log[1].strip()


def increase_total_kills():
    GAMES[CURRENT_GAME_KEY]["total_kills"] += 1


def add_players(players):
    for player in players:
        if player != WORLD_PLAYER and player not in GAMES[CURRENT_GAME_KEY]["players"]:
            GAMES[CURRENT_GAME_KEY]["players"].append(player)


def set_kill(killer, victim):
    game = GAMES[CURRENT_GAME_KEY]
    if killer == WORLD_PLAYER:
        game["kills"][victim] = -1 if victim not in game["kills"] else game["kills"][victim] - 1
    else:
        game["kills"][killer] = 1 if killer not in game["kills"] else game["kills"][killer] + 1


def set_meaning(meaning):
    game = GAMES[CURRENT_GAME_KEY]

    if meaning in game["kills_by_means"]:
        game["kills_by_means"][meaning] += 1
    else:
        game["kills_by_means"][meaning] = 1


def is_new_game(line):
    return bool(re.compile(START_GAME_PATTERN).match(line.strip()))


def is_kill_event(line):
    return bool(re.compile(KILL_LINE_PATTERN).match(line.strip()))


def create_game():
    global CURRENT_GAME_KEY
    CURRENT_GAME_KEY = f"game_{NUMBER_OF_GAMES}"
    GAMES[CURRENT_GAME_KEY] = {
        "total_kills": 0,
        "players": [],
        "kills": {},
        "kills_by_means": {}
    }


def increase_number_of_games():
    global NUMBER_OF_GAMES
    NUMBER_OF_GAMES += 1


@handle_results
def create_games_grouped_information(file_name):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", file_name), "r") as f:
        for line in f.readlines():
            if is_new_game(line):
                increase_number_of_games()
                create_game()
                continue

            if is_kill_event(line):
                increase_total_kills()
                killer, victim, meaning = get_death_data(line)
                add_players([killer, victim])
                set_kill(killer, victim)
                set_meaning(meaning)


def show_result():  # pragma: no cover
    print(GAMES)


def save_result():  # pragma: no cover
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "result.txt"), "w") as f:
        f.write(json.dumps(GAMES, indent=4))


if __name__ == "__main__":  # pragma: no cover
    file = sys.argv[-1]
    create_games_grouped_information(file)
    show_result()
    save_result()
