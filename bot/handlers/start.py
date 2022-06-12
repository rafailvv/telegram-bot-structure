from aiogram import Bot, Dispatcher
from aiogram.types import Message

from bot.buttons.buttons import Buttons


class Start:
    def __init__(self, bot : Bot, dp :Dispatcher, buttons : Buttons):
        self.buttons = buttons
        self.dp = dp
        self.bot = bot
        dp.register_message_handler(self.start_handler, commands=['start'])

    async def start_handler(self, message : Message):
        await message.answer(text= f"Привет, {message.from_user.first_name}")
