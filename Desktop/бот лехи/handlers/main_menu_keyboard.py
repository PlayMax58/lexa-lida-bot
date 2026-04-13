from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu_keyboard(language="ru"):
    """Клавиатура главного меню"""
    if language == "ru":
        text = {
            "attractions": "🏛️ Посмотреть достопримечательности",
            "routes": "🗺️ Посмотреть авторские маршруты",
            "top40": "⭐ Посмотреть рекомендации (Топ-40)"
        }
    else:
        text = {
            "attractions": "🏛️ See attractions",
            "routes": "🗺️ See author routes",
            "top40": "⭐ See recommendations (Top-40)"
        }
    
    keyboard = [
        [InlineKeyboardButton(text["attractions"], callback_data="menu_attractions")],
        [InlineKeyboardButton(text["routes"], callback_data="menu_routes")],
        [InlineKeyboardButton(text["top40"], callback_data="menu_top40")]
    ]
    return InlineKeyboardMarkup(keyboard)