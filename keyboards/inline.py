from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def mode_keyboards() -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Время по Красноярску -> Все пояса", callback_data="krs_tz_mode")
    keyboard_builder.button(text="Время по другому поясу -> Все пояса", callback_data="all_tz_mode")
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup()
