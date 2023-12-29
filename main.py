import asyncio
import logging

from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram import Bot, Dispatcher

from bot.config import config
from bot.handlers import *

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

BOT_TOKEN = config.tg_bot.token

bot = Bot(BOT_TOKEN, parse_mode="HTML")
redis = Redis(host=config.redis.host)
storage = RedisStorage(redis=redis)
dp = Dispatcher(storage=storage)

dp.include_routers(commands_router, menu_router, callback_router)


async def main():
    logging.info("Starting bot")
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
