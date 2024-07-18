import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ContentType
from aiogram.filters import Command
from handlers.timezone_giver import *
from config import TOKEN
from handlers.states import MainStates


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.message.register(start, Command('start'))
    dp.message.register(help_command, Command('help'))
    dp.callback_query.register(krasnoyarsk_mode_handler, MainStates.mode_choose, F.data.startswith("krs_tz_mode"))
    dp.message.register(krasnoyarks_time_handler, MainStates.input_krs_time, F.content_type == ContentType.TEXT)

    dp.callback_query.register(other_mode_handler, MainStates.mode_choose, F.data.startswith("all_tz_mode"))
    dp.message.register(other_time_handler, MainStates.input_other_time, F.content_type == ContentType.TEXT)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())