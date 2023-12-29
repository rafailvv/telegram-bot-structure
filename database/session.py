from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext import asyncio as async_orm


class BaseDatabase:
    def __init__(self, config):
        database_url = f"postgresql+asyncpg://{config.db.user}:{config.db.passwrod}@{config.db.host}/{config.db.database}"
        self.db = SessionManager(database_url).get_session()


class SessionManager:
    def __init__(self, database_url) -> None:
        self.engine = async_orm.create_async_engine(database_url, echo=False)
        self.session_local = sessionmaker(
            self.engine, expire_on_commit=False, class_=async_orm.AsyncSession
        )

    def get_session(self) -> sessionmaker:
        return self.session_local
