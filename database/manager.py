from database.queries.users import UserQueries
from bot.config import config


class Database:
    user = UserQueries(config)


db = Database()
