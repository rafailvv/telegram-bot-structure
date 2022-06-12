from aiogram import Bot, Dispatcher

from bot.buttons.buttons import Buttons


class Message:
    def __init__(self, bot: Bot, dp: Dispatcher, buttons: Buttons):
        self.buttons = buttons
        self.dp = dp
        self.bot = bot
        # dp.register_message_handler()