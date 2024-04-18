from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

def keyboard_sex()->ReplyKeyboardMarkup:
    kb_sex=ReplyKeyboardMarkup(resize_keyboard=True)
    return kb_sex.row(KeyboardButton(text="Я девушка"),KeyboardButton(text="Я парень"))

def keyboard_interest()->ReplyKeyboardMarkup:
    kb_interest=ReplyKeyboardMarkup(resize_keyboard=True)
    return kb_interest.row(KeyboardButton(text="Парни"),KeyboardButton(text="Девушки"),KeyboardButton(text="Всё равно"))

def keyboard_location()->ReplyKeyboardMarkup:
    kb_location=ReplyKeyboardMarkup(resize_keyboard=True)
    return kb_location.row(KeyboardButton(text="Отправить мое местоположение",request_location=True))

def total_profile()->ReplyKeyboardMarkup:
    kb_total=ReplyKeyboardMarkup(resize_keyboard=True)
    return kb_total.add(KeyboardButton(text="Посмотреть мою анкету"))



