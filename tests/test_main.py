import os

import pytest
import src.main as main
from src.constants import WORLD_PLAYER
from unittest import mock

GAME_TEST = "game_test"


@pytest.fixture(autouse=True)
def run_before_tests():
    main.NUMBER_OF_GAMES = 0
    main.GAMES = {}
    main.CURRENT_GAME_KEY = ""

    yield


def test_get_death_data(get_kill_line):
    killer, victim, meaning = main.get_death_data(get_kill_line)

    assert killer == "Oootsimo"
    assert victim == "Zeh"
    assert meaning == "MOD_ROCKET"


def test_increase_total_kills():
    main.increase_number_of_games()

    assert main.NUMBER_OF_GAMES == 1


def test_add_players(create_game, get_players):
    main.GAMES = create_game
    main.CURRENT_GAME_KEY = GAME_TEST
    main.add_players(get_players)

    assert len(main.GAMES[GAME_TEST]["players"]) == 2


def test_add_game_player(create_game):
    main.GAMES = create_game
    main.CURRENT_GAME_KEY = GAME_TEST
    main.add_players([WORLD_PLAYER])

    assert len(main.GAMES[GAME_TEST]["players"]) == 0


def test_set_world_kill(create_game):
    victim = "player1"
    main.GAMES = create_game
    main.CURRENT_GAME_KEY = GAME_TEST
    main.set_kill(WORLD_PLAYER, victim)

    assert len(main.GAMES[GAME_TEST]["kills"]) == 1
    assert main.GAMES[GAME_TEST]["kills"][victim] == -1


def test_set_player_kill(create_game):
    killer = "player1"
    victim = "player2"
    main.GAMES = create_game
    main.CURRENT_GAME_KEY = GAME_TEST
    main.set_kill(killer, victim)

    assert len(main.GAMES[GAME_TEST]["kills"]) == 1
    assert main.GAMES[GAME_TEST]["kills"][killer] == 1


def test_set_multiple_kills(create_game):
    player1 = "player1"
    player2 = "player2"
    main.GAMES = create_game
    main.CURRENT_GAME_KEY = GAME_TEST
    main.set_kill(player1, player2)
    main.set_kill(player2, player1)

    assert len(main.GAMES[GAME_TEST]["kills"]) == 2
    assert main.GAMES[GAME_TEST]["kills"][player1] == 1
    assert main.GAMES[GAME_TEST]["kills"][player2] == 1
    

def test_set_new_meaning(create_game):
    meaning = "MEANING_TEST"
    main.GAMES = create_game
    main.CURRENT_GAME_KEY = GAME_TEST
    main.set_meaning(meaning)

    assert main.GAMES[GAME_TEST]["kills_by_means"].get(meaning)
    assert main.GAMES[GAME_TEST]["kills_by_means"][meaning] == 1


def test_set_existing_meaning(create_game):
    meaning = "MEANING_TEST"
    main.GAMES = create_game
    main.GAMES[GAME_TEST]["kills_by_means"].update({
        meaning: 2
    })
    main.CURRENT_GAME_KEY = GAME_TEST
    main.set_meaning(meaning)

    assert main.GAMES[GAME_TEST]["kills_by_means"].get(meaning)
    assert main.GAMES[GAME_TEST]["kills_by_means"][meaning] == 3


def test_is_new_game(get_new_game_line):
    assert main.is_new_game(get_new_game_line)


def test_is_not_new_game(get_kill_line):
    assert not main.is_new_game(get_kill_line)


def test_is_kill_event(get_kill_line):
    assert main.is_kill_event(get_kill_line)


def test_is_not_kill_event(get_new_game_line):
    assert not main.is_kill_event(get_new_game_line)


def test_create_game():
    main.NUMBER_OF_GAMES = 1
    main.create_game()

    assert main.GAMES.get("game_1")


def test_increase_number_of_games():
    main.increase_number_of_games()

    assert main.NUMBER_OF_GAMES == 1


@mock.patch("os.path.join", return_value=os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mocks", "test_log_file.txt")))
def test_create_games_grouped_information(mocked_file_path, get_game_result):

    main.create_games_grouped_information("test_log_file.txt")

    assert main.GAMES == get_game_result
