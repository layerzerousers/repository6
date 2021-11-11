from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu =  ReplyKeyboardMarkup(
    [




        [
        KeyboardButton(text="Полное расписание",one_time_keyboard=True),
        ],
[
        KeyboardButton(text="Расписание на сегодня",one_time_keyboard=True),
        KeyboardButton(text="Расписание на завтра",one_time_keyboard=True),
        ],
        [
        KeyboardButton(text="Время до конца пары",one_time_keyboard=True),
        ],


    ],
resize_keyboard=True
)