from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.weekdays_callback_data import weekdays_callback

weekdays_odd = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Понедельник",
                callback_data=weekdays_callback.new(weekday="monday_odd")
            ),
         ],
        [
InlineKeyboardButton(
                text="Вторник",
                callback_data=weekdays_callback.new(weekday="tuesday_odd")
            ),
],
        [

InlineKeyboardButton(
                text="Среда",
                callback_data=weekdays_callback.new(weekday="wednesday_odd")
            ),
            ],
        [
InlineKeyboardButton(
                text="Четверг",
                callback_data=weekdays_callback.new(weekday="thursday_odd")
            ),
            ],
        [
InlineKeyboardButton(
                text="Пятница",
                callback_data=weekdays_callback.new(weekday="friday_odd")
            ),

        ],
    ]
)


weekdays_even = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Понедельник",
                callback_data=weekdays_callback.new(weekday="monday_even")
            ),
         ],
        [
InlineKeyboardButton(
                text="Вторник",
                callback_data=weekdays_callback.new(weekday="tuesday_even")
            ),
],
        [

InlineKeyboardButton(
                text="Среда",
                callback_data=weekdays_callback.new(weekday="wednesday_even")
            ),
            ],
        [
InlineKeyboardButton(
                text="Четверг",
                callback_data=weekdays_callback.new(weekday="thursday_even")
            ),
            ],
        [
InlineKeyboardButton(
                text="Пятница",
                callback_data=weekdays_callback.new(weekday="friday_even")
            ),

        ],
    ]
)

returns = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Вернуться в меню",
                callback_data=weekdays_callback.new(weekday="return")
            ),
            ],
        ]
)




