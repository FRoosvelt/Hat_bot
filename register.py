from aiogram import Dispatcher

from handlers.search import register_search


def register(dp: Dispatcher):
    register_search(dp)
