# keyboards/top40_keyboard.py
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from database.top40_data import TOP_40

def get_top40_keyboard(start_index=0, language="ru"):
    """Клавиатура для навигации по топ-40"""
    
    # Проверяем наличие данных
    if not TOP_40 or len(TOP_40) == 0:
        # Если данных нет, возвращаем пустую клавиатуру с кнопкой назад
        if language == "ru":
            back_text = "◀️ Назад в меню"
        else:
            back_text = "◀️ Back to menu"
        
        keyboard = [[InlineKeyboardButton(back_text, callback_data="back_to_main")]]
        return InlineKeyboardMarkup(keyboard)
    
    # Тексты в зависимости от языка
    if language == "ru":
        back_text = "◀️ Назад в меню"
        prev_text = "⬅️ Предыдущие"
        next_text = "➡️ Следующие"
    else:
        back_text = "◀️ Back to menu"
        prev_text = "⬅️ Previous"
        next_text = "➡️ Next"
    
    keyboard = []
    
    # Показываем 5 достопримечательностей за раз
    items_per_page = 5
    total_items = len(TOP_40)
    end_index = min(start_index + items_per_page, total_items)
    
    # Создаем кнопки для текущей страницы
    for i in range(start_index, end_index):
        item_num = i + 1
        attraction = TOP_40.get(item_num)
        
        if attraction:
            # Обрезаем длинные названия
            name = attraction['name']
            if len(name) > 30:
                name = name[:27] + "..."
            
            keyboard.append([
                InlineKeyboardButton(
                    f"{item_num}. {name}", 
                    callback_data=f"top40_{item_num}"
                )
            ])
    
    # Кнопки навигации между страницами
    nav_buttons = []
    
    # Кнопка "Назад" если не на первой странице
    if start_index > 0:
        nav_buttons.append(
            InlineKeyboardButton(
                prev_text, 
                callback_data=f"top40_page_{max(0, start_index - items_per_page)}"
            )
        )
    
    # Кнопка "Вперед" если есть еще элементы
    if end_index < total_items:
        nav_buttons.append(
            InlineKeyboardButton(
                next_text, 
                callback_data=f"top40_page_{end_index}"
            )
        )
    
    if nav_buttons:  # Добавляем навигационные кнопки если они есть
        keyboard.append(nav_buttons)
    
    # Кнопка возврата в главное меню
    keyboard.append([InlineKeyboardButton(back_text, callback_data="back_to_main")])
    
    return InlineKeyboardMarkup(keyboard)

def get_top40_detail_keyboard(attraction_id, language="ru"):
    """Клавиатура для детального просмотра достопримечательности из топ-40"""
    
    if language == "ru":
        back_text = "◀️ Назад к списку"
        prev_text = "⬅️ Предыдущая"
        next_text = "➡️ Следующая"
    else:
        back_text = "◀️ Back to list"
        prev_text = "⬅️ Previous"
        next_text = "➡️ Next"
    
    keyboard = []
    
    total_items = len(TOP_40)
    
    # Кнопки навигации между соседними элементами
    if total_items > 1:
        nav_buttons = []
        
        # Кнопка "Предыдущая" если не первая
        if attraction_id > 1:
            nav_buttons.append(
                InlineKeyboardButton(
                    prev_text, 
                    callback_data=f"top40_{attraction_id - 1}"
                )
            )
        
        # Кнопка "Следующая" если не последняя
        if attraction_id < total_items:
            nav_buttons.append(
                InlineKeyboardButton(
                    next_text, 
                    callback_data=f"top40_{attraction_id + 1}"
                )
            )
        
        if nav_buttons:
            keyboard.append(nav_buttons)
    
    # Кнопка возврата к списку
    keyboard.append([InlineKeyboardButton(back_text, callback_data="back_to_top40_list")])
    
    return InlineKeyboardMarkup(keyboard)