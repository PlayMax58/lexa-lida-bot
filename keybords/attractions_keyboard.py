from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import hashlib

def get_attractions_keyboard(attractions, station_name, language="ru"):
    """Клавиатура для выбора достопримечательности с защитой от длинных имен"""
    
    if language == "ru":
        back_text = "◀️ Назад к станциям"
    else:
        back_text = "◀️ Back to stations"
    
    keyboard = []
    
    for attraction in attractions:
        name = attraction.get("name", "Unknown")
        
        # ТЕКСТ на кнопке может быть длинным (до 128 символов)
        button_text = name
        
        # ДАННЫЕ кнопки (callback_data) — лимит 64 байта.
        # Чтобы избежать ошибки, мы берем только первые 20 символов названия 
        # и заменяем пробелы. Этого достаточно для поиска.
        safe_id = name.replace(" ", "_")[:30]
        
        keyboard.append([
            InlineKeyboardButton(
                text=button_text, 
                callback_data=f"attraction_{safe_id}"
            )
        ])
    
    # Кнопка назад
    keyboard.append([InlineKeyboardButton(back_text, callback_data="back_to_districts")])
    
    return InlineKeyboardMarkup(keyboard)