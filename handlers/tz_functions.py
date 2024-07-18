import pytz
import datetime
from .data import timezones, timezones_locale


def convert_to_timezone(input_time: str, timezone: str = None):
    input_format = '%d-%m-%Y %H:%M'
    input_time = datetime.datetime.strptime(input_time, input_format)

    if timezone is None:
        timezone = "Asia/Krasnoyarsk"
    else:
        reverse_tz_name = timezones_locale[timezone]
        timezone = timezones[reverse_tz_name]

    correct_tz = pytz.timezone(timezone)
    localized_input_time = correct_tz.localize(input_time)

    result = {}
    for tz_name, tz in timezones.items():
        target_tz = pytz.timezone(tz)
        target_time = localized_input_time.astimezone(target_tz)
        result[tz_name] = target_time.strftime("%d-%m-%Y %H:%M")
    return result
