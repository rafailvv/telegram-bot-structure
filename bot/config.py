from dataclasses import dataclass
from typing import List

from environs import Env


@dataclass
class TgBot:
    token : str
    admin_ids : List[int]


def load_config(path : str = None):
    env = Env()
    env.read_env (path)

    return TgBot(
        token = env.str("BOT_TOKEN"),
        admin_ids = list(map(int, env.list("ADMINS")))
    )