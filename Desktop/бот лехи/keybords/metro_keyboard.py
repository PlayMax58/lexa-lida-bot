#metro_keyboard.py
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from database.districts_data import DISTRICTS

def get_metro_keyboard(district_index, language="ru"):
    # district_index приходит как число (индекс в списке ключей)
    dist_keys = list(DISTRICTS.keys())
    dist_name = dist_keys[int(district_index)]
    stations = DISTRICTS[dist_name]
    
    keyboard = []
    for i in range(0, len(stations), 2):
        row = []
        # Данные кнопки: m_ИНДЕКС-ОКРУГА_ИНДЕКС-СТАНЦИИ
        row.append(InlineKeyboardButton(stations[i], callback_data=f"m_{district_index}_{i}"))
        if i + 1 < len(stations):
            row.append(InlineKeyboardButton(stations[i+1], callback_data=f"m_{district_index}_{i+1}"))
        keyboard.append(row)

    back_text = "◀️ Назад" if language == "ru" else "◀️ Back"
    keyboard.append([InlineKeyboardButton(back_text, callback_data="back_to_districts")])
    return InlineKeyboardMarkup(keyboard)