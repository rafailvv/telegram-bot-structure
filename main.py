import asyncio

from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram import Bot, Dispatcher

from bot.config import config
from bot.handlers import *


BOT_TOKEN = config.token

bot = Bot(BOT_TOKEN, parse_mode="HTML")
redis = Redis(host="localhost")
storage = RedisStorage(redis=redis)
dp = Dispatcher(storage=storage)

dp.include_routers(commands_router, menu_router, callback_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
