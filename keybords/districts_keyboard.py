# keyboards/districts_keyboard.py - ИСПРАВЛЕННАЯ ВЕРСИЯ
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def get_districts_keyboard(language="ru"):
    """Клавиатура для выбора округа с 10 кнопками"""
    
    # Определяем текст кнопок в зависимости от языка
    if language == "ru":
        # 10 округов Москвы на русском
        districts = [
            ("Центральный (ЦАО)", "Центральный (ЦАО)"),
            ("Северный (САО)", "Северный (САО)"),
            ("Северо-Восточный (СВАО)", "Северо-Восточный (СВАО)"),
            ("Восточный (ВАО)", "Восточный (ВАО)"),
            ("Юго-Восточный (ЮВАО)", "Юго-Восточный (ЮВАО)"),
            ("Южный (ЮАО)", "Южный (ЮАО)"),
            ("Юго-Западный (ЮЗАО)", "Юго-Западный (ЮЗАО)"),
            ("Западный (ЗАО)", "Западный (ЗАО)"),
            ("Северо-Западный (СЗАО)", "Северо-Западный (СЗАО)"),
            ("Новомосковский (НАО)", "Новомосковский (НАО)")
        ]
        back_text = "◀️ Назад"
    else:
        # 10 округов Москвы на английском
        districts = [
            ("Central (CAO)", "Центральный (ЦАО)"),
            ("Northern (SAO)", "Северный (САО)"),
            ("North-Eastern (SVAO)", "Северо-Восточный (СВАО)"),
            ("Eastern (VAO)", "Восточный (ВАО)"),
            ("South-Eastern (YuVAO)", "Юго-Восточный (ЮВАО)"),
            ("Southern (YuAO)", "Южный (ЮАО)"),
            ("South-Western (YuZAO)", "Юго-Западный (ЮЗАО)"),
            ("Western (ZAO)", "Западный (ЗАО)"),
            ("North-Western (SZAO)", "Северо-Западный (СЗАО)"),
            ("Novomoskovsky (NAO)", "Новомосковский (НАО)")
        ]
        back_text = "◀️ Back"
    
    keyboard = []
    
    # Создаем кнопки для каждого округа
    # Разбиваем на 2 колонки для компактности
    for i in range(0, len(districts), 2):
        row = []
        # Первая кнопка в ряду
        if i < len(districts):
            display_name, callback_name = districts[i]
            row.append(InlineKeyboardButton(
                display_name, 
                callback_data=f"district_{callback_name}"
            ))
        
        # Вторая кнопка в ряду (если есть)
        if i + 1 < len(districts):
            display_name, callback_name = districts[i + 1]
            row.append(InlineKeyboardButton(
                display_name, 
                callback_data=f"district_{callback_name}"
            ))
        
        keyboard.append(row)
    
    # Кнопка назад
    keyboard.append([InlineKeyboardButton(back_text, callback_data="back_to_main")])
    
    return InlineKeyboardMarkup(keyboard)

# УДАЛИТЕ функцию get_metro_keyboard из этого файла
# Она будет в отдельном файле metro_keyboard.py