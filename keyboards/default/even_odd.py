from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

even_odd =  ReplyKeyboardMarkup(
    [




        [
        KeyboardButton(text="Нечетная",one_time_keyboard=True),
        KeyboardButton(text="Четная",one_time_keyboard=True),
        ],



    ],
resize_keyboard=True
)