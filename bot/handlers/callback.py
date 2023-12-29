from aiogram import Router
from aiogram.types import CallbackQuery

callback_router = Router()


@callback_router.callback_query(lambda q: "button" in q.data)
async def check_query(query: CallbackQuery):
    await query.message.answer(query.data)
