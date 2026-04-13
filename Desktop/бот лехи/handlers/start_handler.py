from telegram import Update
from telegram.ext import ContextTypes
from keyboards.language_keyboard import get_language_keyboard

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user = update.effective_user
    
    # Отправляем приветственное сообщение с выбором языка
    welcome_message = (
        f"👋 Добро пожаловать, {user.first_name}!\n"
        f"Welcome, {user.first_name}!\n\n"
        "Выберите язык / Choose language:"
    )
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=get_language_keyboard()
    )

async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик выбора языка"""
    query = update.callback_query
    await query.answer()
    
    # Определяем выбранный язык
    if query.data == "lang_ru":
        language = "ru"
        greeting = "🇷🇺 Язык установлен: Русский"
    else:
        language = "en"
        greeting = "🇬🇧 Language set: English"
    
    # Сохраняем язык в контексте пользователя
    context.user_data["language"] = language
    
    # Отправляем сообщение и переходим к главному меню
    from handlers.main_menu_handler import send_main_menu
    await send_main_menu(update, context, greeting)