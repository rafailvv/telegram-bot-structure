from database.session import BaseDatabase
from database.relations.student import StudentDatabase

from dotenv import dotenv_values


class Database(BaseDatabase):
    students = StudentDatabase(config)
