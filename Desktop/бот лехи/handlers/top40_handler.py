from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from database.top40_data import TOP_40

def get_top40_keyboard(start_index, lang):
    keyboard = []
    items = list(TOP_40.items())[start_index:start_index + 5]
    
    for idx, item in items:
        name = item.get(f"name_{lang}", item.get("name_ru"))
        keyboard.append([InlineKeyboardButton(name, callback_data=f"top40_id_{idx}")])
    
    nav_buttons = []
    if start_index > 0:
        nav_buttons.append(InlineKeyboardButton("⬅️", callback_data=f"top40_page_{start_index-5}"))
    if start_index + 5 < len(TOP_40):
        nav_buttons.append(InlineKeyboardButton("➡️", callback_data=f"top40_page_{start_index+5}"))
    if nav_buttons:
        keyboard.append(nav_buttons)

    keyboard.append([InlineKeyboardButton("🏠 Меню" if lang == "ru" else "🏠 Menu", callback_data="back_to_main")])
    return InlineKeyboardMarkup(keyboard)

async def send_top40_list(update: Update, context: ContextTypes.DEFAULT_TYPE, start_index=0):
    query = update.callback_query
    if query: await query.answer()
    
    lang = context.user_data.get("language", "ru")
    context.user_data["top40_page"] = start_index
    reply_markup = get_top40_keyboard(start_index, lang)
    text = "⭐ ТОП-40 достопримечательностей:" if lang == "ru" else "⭐ TOP-40 Attractions:"

    if query:
        if query.message.photo:
            await query.message.delete()
            await context.bot.send_message(query.message.chat_id, text, reply_markup=reply_markup)
        else:
            await query.edit_message_text(text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(text, reply_markup=reply_markup)

async def top40_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    lang = context.user_data.get("language", "ru")

    if data.startswith("top40_page_"):
        page = int(data.split("_")[2])
        await send_top40_list(update, context, page)
        return

    if data.startswith("top40_id_"):
        idx = int(data.split("_")[2])
        item = TOP_40.get(idx)
        if item:
            name = item.get(f"name_{lang}")
            desc = item.get(f"description_{lang}")
            addr = item.get(f"address_{lang}")
            caption = f"<b>{name}</b>\n\n{desc}\n\n📍 Адрес: {addr}"
            kb = [[InlineKeyboardButton("◀️ Назад", callback_data="back_to_top40_list")]]
            
            await query.message.delete()
            try:
                await context.bot.send_photo(chat_id=query.message.chat_id, photo=item['photo'], caption=caption, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(kb))
            except:
                await context.bot.send_message(chat_id=query.message.chat_id, text=caption, parse_mode="HTML", reply_markup=InlineKeyboardMarkup(kb))