from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


async def start_kb():
    start_buttons = [[KeyboardButton(text="Что умеет этот бот? 🤔")]]

    start_buttons_markup = ReplyKeyboardMarkup(keyboard=start_buttons)
    return start_buttons_markup
