import logging

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor

from data.config import TOKEN
from db_api.database import create_base
from register import register


async def on_startup(dp: Dispatcher):
    register(dp)
    await create_base()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(bot)
    executor.start_polling(dp, on_startup=on_startup)
