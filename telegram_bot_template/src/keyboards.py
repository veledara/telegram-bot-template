import telebot
import messages as ms

# Клавиатура для меню
menu_markup = telebot.types.ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
)
first_button = telebot.types.InlineKeyboardButton(text=ms.FIRST_BUTTON)
second_button = telebot.types.InlineKeyboardButton(text=ms.SECOND_BUTTON)
third_button = telebot.types.InlineKeyboardButton(text=ms.THIRD_BUTTON)
menu_markup.add(first_button, second_button)
menu_markup.add(third_button)
