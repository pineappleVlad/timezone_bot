from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from .tz_functions import convert_to_timezone
from keyboards.inline import mode_keyboards
from .states import MainStates
from .data import timezones_locale


async def start(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Выберите режим перевода времени:", reply_markup=mode_keyboards())
    await state.set_state(MainStates.mode_choose)


async def help_command(message: Message, bot: Bot, state: FSMContext):
    help_info = "Список доступных часовых поясов: \n"
    for city in timezones_locale.keys():
        help_info += f"{city} \n"
    await message.answer(help_info)


async def krasnoyarsk_mode_handler(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Введите дату и время по Красноярску \n \n"
                              "Формат: день-месяц-год часы:минуты \n \n"
                              "Пример: 18-07-2024 14:00")
    await state.set_state(MainStates.input_krs_time)


async def krasnoyarks_time_handler(message: Message, bot: Bot, state: FSMContext):
    input_time = message.text
    try:
        tz_result_dict = convert_to_timezone(input_time)
    except Exception:
        await message.answer("Неверный формат даты, попробуйте еще раз")
        return

    tz_result_str = ""
    for tz_name, converted_time in tz_result_dict.items():
        tz_result_str += f"Время в {tz_name}: {converted_time} \n \n"

    await message.answer(tz_result_str)
    await state.set_state(MainStates.start)
    await start(message, bot, state)


async def other_mode_handler(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.message.delete()
    await call.message.answer(f"Введите дату, время и часовой пояс \n \n"
                              f"Формат: день-месяц-год часы:минуты Часовой пояс \n"
                              f"(список доступных часовых поясов можно посмотреть по \n"
                              f"команде /help) \n \n"
                              f"Пример: 20-01-2024 14:00 Буэнос-Айрес")
    await state.set_state(MainStates.input_other_time)


async def other_time_handler(message: Message, bot: Bot, state: FSMContext):
    input_list = message.text.split()
    time_str = input_list[0] + " " + input_list[1]
    timezone = input_list[-1]
    if timezone not in timezones_locale.keys():
        await message.answer("Неверный часовой пояс, попробуйте еще раз")
        return
    try:
        tz_result_dict = convert_to_timezone(time_str, timezone)
    except Exception:
        await message.answer("Неверный формат даты, попробуйте еще раз")
        return

    tz_result_str = ""
    for tz_name, converted_time in tz_result_dict.items():
        tz_result_str += f"Время в {tz_name}: {converted_time} \n \n"

    await message.answer(tz_result_str)
    await state.set_state(MainStates.start)
    await start(message, bot, state)



