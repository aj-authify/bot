from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
import mongodb
import tpo


async def tpo_website_buttons(
    phone_number, update: Update, context: ContextTypes.DEFAULT_TYPE
):
    tpo_data = await tpo.find_all_tpo(f"{phone_number}")
    if not tpo_data["ok"]:
        await update.message.reply_text(tpo_data["message"])
        return

    tpo_data = tpo_data["documents"]

    keyboard = [[KeyboardButton(text=tpo_item["website"]) for tpo_item in tpo_data]]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    )

    await update.message.reply_text("Choose a website", reply_markup=reply_markup)
