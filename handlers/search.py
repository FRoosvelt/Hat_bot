from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import Message

from db_api.commands.table import select_id
from db_api.tables.table import Table


async def start(message: Message):
    return await message.answer("Напиши /search любую цифру\n"
                                "/search 1")


async def search(message: Message):
    args = message.get_args()
    if not args:
        await message.reply(
            '<b> Отсутствуют аргументы к команде!</b>'
        )
    else:
        try:
            table: Table = await select_id(int(args))
            search = message.text.startswith("/search")
            if search and not table:
                return await message.answer(
                    '<b> Такого номера не существует!</b>'
                )
            await message.reply(f"/search <b>{args}</b>\n"
                                f"<b>{table.first_column}</b>\n"
                                f"<b>{table.second_column}</b>")
        except ValueError:
            return await message.reply(
                '<b> Значение должно быть числом!</b>'
            )


def register_search(dp: Dispatcher):
    dp.register_message_handler(
        start,
        CommandStart()
    )
    dp.register_message_handler(
        search,
        Text(startswith="/search")
    )
