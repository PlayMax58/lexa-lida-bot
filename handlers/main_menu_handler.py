# handlers/main_menu_handler.py
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Русский 🇷🇺", callback_data="lang_ru"),
            InlineKeyboardButton("English 🇬🇧", callback_data="lang_en"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "Привет! Выберите язык / Hello! Choose your language:"
    
    if update.callback_query:
        await update.callback_query.message.reply_text(text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(text, reply_markup=reply_markup)

async def send_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query: await query.answer()
    lang = context.user_data.get("language", "ru")
    
    texts = {
        "ru": ("📍 Главное меню:", [("⭐ ТОП-40", "top40"), ("🏙 Выбрать достопримечательность", "districts"), ("🗺 Авторские маршруты", "routes"), ("⚙️ Настройки", "settings")]),
        "en": ("📍 Main Menu:", [("⭐ TOP-40", "top40"), ("🏙 Choose a place of interest", "districts"), ("🗺 Author's routes", "routes"), ("⚙️ Settings", "settings")])
    }
    
    current_text, buttons = texts.get(lang, texts["ru"])
    keyboard = [[InlineKeyboardButton(name, callback_data=data)] for name, data in buttons]
    
    if query:
        await query.edit_message_text(current_text, reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.message.reply_text(current_text, reply_markup=InlineKeyboardMarkup(keyboard))

async def main_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "top40":
        from handlers.top40_handler import send_top40_list
        await send_top40_list(update, context)
    elif data == "districts":
        from handlers.attractions_handler import send_districts_menu
        await send_districts_menu(update, context)
    elif data == "routes":
        from handlers.routes_handler import send_routes_list
        await send_routes_list(update, context)
    elif data == "settings":
        await query.message.delete()
        await start(update, context)