from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from database.districts_data import DISTRICTS
from database.excel_manager import excel_manager

async def send_districts_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query: await query.answer()
    lang = context.user_data.get("language", "ru")
    text = "🏙 Выберите округ:" if lang == "ru" else "🏙 Select a district:"
    
    keyboard = []
    for dist_id, data in DISTRICTS.items():
        display_name = data["name"].get(lang, data["name"]["ru"])
        keyboard.append([InlineKeyboardButton(display_name, callback_data=f"distidx_{dist_id}")])
    
    keyboard.append([InlineKeyboardButton("🏠 Меню", callback_data="back_to_main")])
    
    if query:
        if query.message.photo:
            await query.message.delete()
            await context.bot.send_message(query.message.chat_id, text, reply_markup=InlineKeyboardMarkup(keyboard))
        else:
            await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def district_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("language", "ru")
    dist_id = query.data.split("_")[1]
    dist_data = DISTRICTS.get(dist_id)

    stations = dist_data["stations"][lang]
    keyboard = []
    row = []
    for s_idx, station in enumerate(stations):
        row.append(InlineKeyboardButton(station, callback_data=f"midx_{dist_id}_{s_idx}"))
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row: keyboard.append(row)
    keyboard.append([InlineKeyboardButton("◀️ Назад", callback_data="back_to_districts")])
    
    await query.edit_message_text(f"🚇 {dist_data['name'][lang]}:", reply_markup=InlineKeyboardMarkup(keyboard))

async def metro_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("language", "ru")
    parts = query.data.split("_")
    dist_id, s_idx = parts[1], int(parts[2])
    
    station_name_ru = DISTRICTS[dist_id]["stations"]["ru"][s_idx]
    attractions = excel_manager.get_attractions_by_station(station_name_ru, lang)
    
    keyboard = []
    for attr in attractions:
        keyboard.append([InlineKeyboardButton(attr["name"], callback_data=f"attrid_{attr['id']}")])
    
    keyboard.append([InlineKeyboardButton("◀️ Назад", callback_data=f"distidx_{dist_id}")])
    await query.edit_message_text(f"📍 {DISTRICTS[dist_id]['stations'][lang][s_idx]}:", reply_markup=InlineKeyboardMarkup(keyboard))

async def attraction_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("language", "ru")
    attr_id = query.data.split("_")[1]
    details = excel_manager.get_details_by_id(attr_id, lang)
    
    if details:
        caption = f"<b>{details['name']}</b>\n\n{details['description']}\n\n📍 {details['address']}"
        kb = [[InlineKeyboardButton("◀️ Назад", callback_data="back_to_districts")]]
        await query.message.delete()
        try:
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=details['photo'], caption=caption, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(kb))
        except:
            await context.bot.send_message(chat_id=query.message.chat_id, text=caption, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(kb))