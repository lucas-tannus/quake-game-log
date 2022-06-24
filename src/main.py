import os
import re

from constants import (
    KILL_LINE_PATTERN,
    WORLD_PLAYER
)

GAME = {
    "total_kills": 0,
    "players": [],
    "kills": {},
    "kills_by_means": {}
}


def get_all_kill_lines(file):
    regex = re.compile(KILL_LINE_PATTERN)
    with open(os.path.join("..", "data", file), "r") as file:
        return [line for line in file.readlines() if regex.match(line.strip())]


def get_death_data(kill_line):
    half_log = kill_line.split("killed")
    third_log = half_log[1].split("by")

    return half_log[0].split(":")[-1].strip(), third_log[0].strip(), third_log[1].strip()


def increase_total_kills():
    GAME["total_kills"] += 1


def add_players(players):
    for player in players:
        if player != WORLD_PLAYER and player not in GAME["players"]:
            GAME["players"].append(player)


def set_kill(killer, victim):
    if killer == WORLD_PLAYER:
        GAME["kills"][victim] = -1 if victim not in GAME["kills"] else GAME["kills"][victim] - 1
    else:
        GAME["kills"][killer] = 1 if killer not in GAME["kills"] else GAME["kills"][killer] + 1


def set_mean(mean):
    if mean in GAME["kills_by_means"]:
        GAME["kills_by_means"][mean] += 1
    else:
        GAME["kills_by_means"][mean] = 1


def generate_group_information(file):
    kill_lines = get_all_kill_lines(file)

    for kill_line in kill_lines:
        increase_total_kills()
        killer, victim, mean = get_death_data(kill_line)
        add_players([killer, victim])
        set_kill(killer, victim)
        set_mean(mean)
    print(GAME)


generate_group_information("log_1.txt")
