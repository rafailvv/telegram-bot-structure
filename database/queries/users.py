from database import models
from database.session import BaseDatabase
from sqlalchemy import (
    select,
    insert,
)


class UserQueries(BaseDatabase):
    async def insert_user(self, tg_id: int, username: str):
        async with self.db() as session:
            await session.execute(
                insert(models.Users).values(id=tg_id, username=username)
            )
            await session.commit()
