from aiogram.fsm.state import StatesGroup, State


class MainStates(StatesGroup):
    start = State()
    mode_choose = State()
    input_krs_time = State()
    input_other_time = State()
