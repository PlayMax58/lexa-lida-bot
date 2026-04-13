# handlers/language_handler.py
from telegram import Update
from telegram.ext import ContextTypes

async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    lang = "ru" if "lang_ru" in query.data else "en"
    context.user_data["language"] = lang
    
    from handlers.main_menu_handler import send_main_menu
    await send_main_menu(update, context)