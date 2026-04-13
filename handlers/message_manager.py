from telegram import Update
from telegram.ext import ContextTypes

async def delete_previous_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Удаление предыдущих сообщений бота для чистоты чата.
    Детальная информация о достопримечательностях не удаляется.
    """
    try:
        # Получаем ID последнего сообщения
        last_message_id = context.user_data.get("last_message_id")
        
        # Получаем ID предыдущего сообщения (если есть)
        previous_message_id = context.user_data.get("previous_message_id")
        
        # Сохраняем текущее сообщение как предыдущее для следующего раза
        if update.callback_query:
            current_message_id = update.callback_query.message.message_id
        else:
            current_message_id = update.message.message_id
        
        # Удаляем предыдущее сообщение, если оно не является детальной информацией
        if previous_message_id and previous_message_id != last_message_id:
            try:
                await context.bot.delete_message(
                    chat_id=update.effective_chat.id,
                    message_id=previous_message_id
                )
            except:
                pass  # Игнорируем ошибки при удалении
        
        # Обновляем ID сообщений
        context.user_data["previous_message_id"] = last_message_id
        context.user_data["last_message_id"] = current_message_id
        
    except Exception as e:
        # В случае ошибки просто продолжаем
        print(f"Error in delete_previous_messages: {e}")
        pass