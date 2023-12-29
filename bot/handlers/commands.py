from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.buttons import start_kb
from bot.message_text.text import START_MESSAGE, ADMIN_START_MESSAGE
from bot.config import config

commands_router = Router()


@commands_router.message(Command("start"))
async def cmd_start(message: Message):
    if message.chat.id in config.tg_bot.admin_ids:
        await message.answer(
            ADMIN_START_MESSAGE.format(message.chat.first_name),
            reply_markup=await start_kb(),
        )
    else:
        await message.answer(
            START_MESSAGE.format(message.chat.first_name), reply_markup=await start_kb()
        )
