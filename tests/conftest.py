import pytest


@pytest.fixture
def get_kill_line():
    return "  0:25 Kill: 2 4 6: Oootsimo killed Zeh by MOD_ROCKET"


@pytest.fixture
def get_players():
    return ["player1", "player2"]


@pytest.fixture
def create_game():
    return {
        "game_test": {
            "total_kills": 0,
            "players": [],
            "kills": {},
            "kills_by_means": {}
        }
    }


@pytest.fixture
def get_new_game_line():
    return "0:00 InitGame: \capturelimit\8\g_maxGameClients\0\timelimit\15\fraglimit\20\dmflags\0\sv_allowDownload\0" \
           "\sv_maxclients\16\sv_privateClients\2\g_gametype\0\sv_hostname\Code Miner " \
           "Server\sv_minRate\0\sv_maxRate\10000\sv_minPing\0\sv_maxPing\0\sv_floodProtect\1\version\ioq3 1.36 " \
           "linux-x86_64 Apr 12 2009\protocol\68\mapname\q3dm17\gamename\baseq3\g_needpass\0 "


@pytest.fixture
def get_game_result():
    return {
        'game_1': {
            'total_kills': 29,
            'players': [
                'Oootsimo', 'Zeh', 'Isgalamido', 'UnnamedPlayer', 'Dono da Bola', 'Maluquinho', 'Assasinu Credi', 'Mal'
            ],
            'kills': {
                'Oootsimo': 8, 'Isgalamido': 3, 'Zeh': 7, 'Dono da Bola': 2, 'Maluquinho': 0, 'Assasinu Credi': 1
            },
            'kills_by_means': {
                'MOD_ROCKET': 5, 'MOD_RAILGUN': 2, 'MOD_SHOTGUN': 4, 'MOD_ROCKET_SPLASH': 13, 'MOD_TRIGGER_HURT': 3,
                'MOD_FALLING': 1, 'MOD_MACHINEGUN': 1
            }
        }
    }
