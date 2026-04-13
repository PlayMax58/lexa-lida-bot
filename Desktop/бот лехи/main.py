# main.py
import os
from dotenv import load_dotenv
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from handlers.language_handler import language_callback
from handlers.main_menu_handler import start, main_menu_callback
from handlers.routes_handler import send_routes_list, routes_callback
from handlers.navigation_handler import navigation_callback
from handlers.top40_handler import top40_callback
from handlers.attractions_handler import district_callback, metro_callback, attraction_callback

load_dotenv("doc_2026-04-13_20-50-39.env")
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(language_callback, pattern="^lang_"))
    
    # Сначала детальные маршруты, потом список
    application.add_handler(CallbackQueryHandler(routes_callback, pattern="^route_"))
    application.add_handler(CallbackQueryHandler(send_routes_list, pattern="^routes$"))
    
    # ТОП-40 и Округа
    application.add_handler(CallbackQueryHandler(top40_callback, pattern="^top40_"))
    application.add_handler(CallbackQueryHandler(district_callback, pattern="^distidx_"))
    application.add_handler(CallbackQueryHandler(metro_callback, pattern="^midx_"))
    application.add_handler(CallbackQueryHandler(attraction_callback, pattern="^attrid_"))

    # Главное меню и навигация
    application.add_handler(CallbackQueryHandler(main_menu_callback, pattern="^(top40|districts|settings)$"))
    application.add_handler(CallbackQueryHandler(navigation_callback, pattern="^back_"))

    application.run_polling()

if __name__ == '__main__':
    main()
