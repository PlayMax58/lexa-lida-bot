from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def get_back_keyboard(callback_data="back_to_main", language="ru"):
    """Универсальная кнопка 'Назад'"""
    if language == "ru":
        back_text = "◀️ Назад"
    else:
        back_text = "◀️ Back"
    
    keyboard = [[InlineKeyboardButton(back_text, callback_data=callback_data)]]
    return InlineKeyboardMarkup(keyboard)