from telegram import Update
from telegram.ext import ContextTypes
import validator
import tpo


async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if validator.valid_website(text):
        tpo_data = await tpo.find_tpo(text)
        msg_send = (
            tpo_data["document"]["tpo"] if tpo_data["ok"] else tpo_data["message"]
        )

        await update.message.reply_text(msg_send, parse_mode="markdown")
        return
    await update.message.reply_text(
        f"{update.effective_user.first_name} good to know!\n`Trust through verification`",
        parse_mode="markdown",
    )
