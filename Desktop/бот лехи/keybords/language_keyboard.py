from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def get_language_keyboard():
    """Клавиатура для выбора языка"""
    keyboard = [
        [
            InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)