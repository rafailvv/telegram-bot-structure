from aiogram import Bot, Dispatcher

from bot.buttons.buttons import Buttons


class Start:
    def __init__(self, bot : Bot, dp :Dispatcher, buttons : Buttons):
        self.buttons = buttons
        self.dp = dp
        self.bot = bot
