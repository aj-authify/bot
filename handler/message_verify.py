from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
import tg_bot_utils
import user


async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone_number = user.user_data["phone_number"]

    if phone_number:
        await tg_bot_utils.tpo_website_buttons(phone_number, update, context)
    else:
        await ask_for_contact(update, context)


async def ask_for_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton(text="Share contact", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    )

    await update.message.reply_text(
        "Share your contact to verify", reply_markup=reply_markup
    )
