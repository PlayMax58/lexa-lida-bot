# handlers/navigation_handler.py
from telegram import Update
from telegram.ext import ContextTypes

async def navigation_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # Возврат в главное меню
    if data == "back_to_main":
        from handlers.main_menu_handler import send_main_menu
        await send_main_menu(update, context)

    # Возврат к списку маршрутов (ВАША ОШИБКА ЗДЕСЬ)
    elif data == "back_to_routes":
        from handlers.routes_handler import send_routes_list
        await send_routes_list(update, context)

    # Возврат к списку ТОП-40
    elif data == "back_to_top40_list":
        from handlers.top40_handler import send_top40_list
        page = context.user_data.get("top40_page", 0)
        await send_top40_list(update, context, start_index=page)

    # Возврат к списку округов
    elif data == "back_to_districts":
        from handlers.attractions_handler import send_districts_menu
        await send_districts_menu(update, context)

    # Добавьте сюда back_to_districts и прочие, если они нужны

    # Вспомогательная функция для очистки
    async def safe_clear():
        try:
            # Если в сообщении есть фото, его ОБЯЗАТЕЛЬНО нужно удалить,
            # так как обычный текст нельзя "впихнуть" в сообщение с картинкой
            if query.message.photo or query.message.caption:
                await query.message.delete()
                return True
        except:
            pass
        return False

    if data == "back_to_main":
        await safe_clear()
        await send_main_menu(update, context)

    elif data == "back_to_top40_list":
        from handlers.top40_handler import send_top40_list
        page = context.user_data.get("top40_page", 0)
        is_deleted = await safe_clear()
        # Если удалили сообщение с фото, вызываем через update, чтобы создалось новое
        await send_top40_list(update, context, start_index=page)

    elif data == "back_to_districts":
        from handlers.attractions_handler import send_districts_menu
        await safe_clear()
        await send_districts_menu(update, context)