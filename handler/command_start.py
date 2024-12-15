from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    keyboard = [[KeyboardButton(text="Share contact", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=True, resize_keyboard=True
    )

    await update.message.reply_text(
        f"Hello {user.first_name}. Please share your contact",
        reply_markup=reply_markup,
    )
