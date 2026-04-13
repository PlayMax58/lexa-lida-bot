from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from database.routes_data import ROUTES, MAP_URL

def get_routes_list_keyboard(language="ru"):
    """Клавиатура со списком маршрутов"""
    if language == "ru":
        back_text = "◀️ Назад в меню"
        map_text = "🗺️ Открыть карту"
    else:
        back_text = "◀️ Back to menu"
        map_text = "🗺️ Open map"
    
    keyboard = []
    
    # Создаем кнопки для каждого маршрута
    for route_id, route_data in ROUTES.items():
        keyboard.append([
            InlineKeyboardButton(
                f"{route_id}. {route_data['name']}", 
                callback_data=f"route_{route_id}"
            )
        ])
    
    # Кнопка открыть карту и назад
    keyboard.append([
        InlineKeyboardButton(map_text, url=MAP_URL)
    ])
    keyboard.append([
        InlineKeyboardButton(back_text, callback_data="back_to_main")
    ])
    
    return InlineKeyboardMarkup(keyboard)

def get_route_detail_keyboard(route_id, language="ru"):
    """Клавиатура для детального просмотра маршрута"""
    if language == "ru":
        back_text = "◀️ Назад к маршрутам"
        map_text = "🗺️ Открыть карту"
    else:
        back_text = "◀️ Back to routes"
        map_text = "🗺️ Open map"
    
    keyboard = [
        [
            InlineKeyboardButton(map_text, url=MAP_URL),
            InlineKeyboardButton(back_text, callback_data="back_to_routes")
        ]
    ]
    
    return InlineKeyboardMarkup(keyboard)