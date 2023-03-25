import telebot
import src.messages as ms

# Клавиатура для меню
menu_markup = telebot.types.ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
)
first_button = telebot.types.InlineKeyboardButton(text=ms.FIRST_BUTTON)
second_button = telebot.types.InlineKeyboardButton(text=ms.SECOND_BUTTON)
third_button = telebot.types.InlineKeyboardButton(text=ms.THIRD_BUTTON)
menu_markup.add(first_button, second_button)
menu_markup.add(third_button)


# Inline клавиатура админки
administration_inline_markup = telebot.types.InlineKeyboardMarkup()
statistics_button = telebot.types.InlineKeyboardButton(
    text=ms.STATISTICS_BUTTON, callback_data=ms.ADMIN_STATISTICS
)
ban_user_button = telebot.types.InlineKeyboardButton(
    text=ms.BAN_USER_BUTTON, callback_data=ms.ADMIN_BAN_USER
)
adv_button = telebot.types.InlineKeyboardButton(
    text=ms.ADV_BUTTON, callback_data=ms.ADMIN_ADV
)
administration_inline_markup.add(statistics_button)
administration_inline_markup.add(ban_user_button)
administration_inline_markup.add(adv_button)


# Inline клавиатура для скрытия списка советов
hide_inline_markup = telebot.types.InlineKeyboardMarkup()
hide_button = telebot.types.InlineKeyboardButton(
    text=ms.HIDE_BUTTON, callback_data="hide"
)
hide_inline_markup.add(hide_button)
