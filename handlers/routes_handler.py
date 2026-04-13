# handlers/routes_handler.py
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from database.routes_data import ROUTES, MAP_URL

async def send_routes_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query: await query.answer()
    
    lang = context.user_data.get("language", "ru")
    
    # Тексты интерфейса
    if lang == "ru":
        text = "🗺 <b>Авторские маршруты</b>\nВыберите маршрут или откройте интерактивную карту:"
        map_btn = "🌐 Интерактивная карта Gid_eon"
        menu_btn = "🏠 Главное меню"
    else:
        text = "🗺 <b>Author's Routes</b>\nSelect a route or open the interactive map:"
        map_btn = "🌐 Gid_eon Interactive Map"
        menu_btn = "🏠 Main Menu"
    
    keyboard = []
    # Кнопка ссылки на карту
    keyboard.append([InlineKeyboardButton(map_btn, url=MAP_URL)])
    
    # Кнопки маршрутов (названия берутся по языку)
    for r_id, data in ROUTES.items():
        name = data[f"name_{lang}"]
        keyboard.append([InlineKeyboardButton(name, callback_data=f"route_{r_id}")])
    
    keyboard.append([InlineKeyboardButton(menu_btn, callback_data="back_to_main")])
    
    if query:
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")
    else:
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")

async def routes_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("language", "ru")
    
    route_id = int(query.data.split("_")[1])
    route = ROUTES.get(route_id)
    
    if route:
        # Названия лейблов
        labels = {
            "ru": {"dist": "Расстояние", "time": "Время", "area": "Район", "theme": "Тема", "map": "🗺 Карта", "back": "◀️ Назад"},
            "en": {"dist": "Distance", "time": "Time", "area": "District", "theme": "Theme", "map": "🗺 Map", "back": "◀️ Back"}
        }[lang]

        text = (
            f"<b>{route[f'name_{lang}']}</b>\n\n"
            f"{route[f'description_{lang}']}\n\n"
            f"🚶‍♂️ <b>{labels['dist']}:</b> {route[f'distance_{lang}']}\n"
            f"⏱️ <b>{labels['time']}:</b> {route[f'time_{lang}']}\n"
            f"📍 <b>{labels['area']}:</b> {route[f'district_{lang}']}\n"
            f"🎨 <b>{labels['theme']}:</b> {route[f'theme_{lang}']}"
        )
        
        kb = [
            [InlineKeyboardButton(labels["map"], url=MAP_URL)],
            [InlineKeyboardButton(labels["back"], callback_data="back_to_routes")]
        ]
        
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")