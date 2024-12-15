from telegram import Update
from telegram.ext import ContextTypes
import tg_bot_utils
import user


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact_user = update.effective_user
    contact = update.message.contact

    if contact.user_id != contact_user.id:
        await update.message.reply_text(
            "Share your **own** contact!", parse_mode="markdown"
        )
        return

    user.user_data["phone_number"] = contact.phone_number
    await tg_bot_utils.tpo_website_buttons(contact.phone_number, update, context)
