from aiogram import Router, F
from aiogram.types import Message

from bot.message_text.text import WHAT_CAN_BOT_DO

menu_router = Router()


@menu_router.message(F.text == "Что умеет этот бот? 🤔")
async def menu_handler(message: Message):
    await message.answer(
        WHAT_CAN_BOT_DO,
    )
