from telegram import Update
from telegram.ext import ContextTypes
import mongodb
import tpo

mongodb_data = mongodb.setup_mongodb()


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    user_id = contact.user_id
    user = update.effective_user

    if user_id != user.id:
        await update.message.reply_text(
            "You must send your own contact information. Please share your contact again"
        )
        return

    tpo_data = await tpo.send_tpo(
        f"+{contact.phone_number}", mongodb_data["collection"]
    )
    if not tpo_data["ok"]:
        await update.message.reply_text(tpo_data["message"])
        return

    await update.message.reply_text(tpo_data["tpo"])
