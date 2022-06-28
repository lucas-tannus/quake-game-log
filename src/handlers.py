import functools

from logger import create_log
from constants import LogConstants


def handle_results(func):
    @functools.wraps(func)
    def wrapper_handle_results(*args, **kwargs):  # pragma: no cover
        try:
            func(*args, **kwargs)
        except FileNotFoundError as exc:
            create_log(exc.__str__(), log_type=LogConstants.ERROR)

    return wrapper_handle_results
