import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.buttons.buttons import Buttons
from bot.config import load_config
from bot.handlers.callback import Callback
from bot.handlers.messages import Message
from bot.handlers.start import Start


async def main():
    config = load_config('.env')

    bot = Bot(token =config.token, parse_mode="HTML")
    dp = Dispatcher(bot, storage=MemoryStorage())

    bot['config'] = config

    buttons = Buttons()

    start = Start(bot, dp, buttons)
    Callback(bot, dp, buttons)
    Message(bot, dp, buttons)
    # Каждый класс из hanler

    await dp.start_polling()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)