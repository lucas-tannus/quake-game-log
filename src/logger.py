import os

from datetime import datetime
from constants import LogConstants

log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "logs")


def create_log(message, log_type=LogConstants.INFO):  # pragma: no cover
    with open(
            os.path.join(log_dir, datetime.now().strftime("%m%d%Y%H%M%S.txt")), "w"
    ) as file:
        file.write(f"{log_type}: {message}")
