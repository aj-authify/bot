from telegram import Update
from telegram.ext import ContextTypes
import validator
import tpo


async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if validator.valid_website(text):
        tpo_data = await tpo.find_tpo(text)
        if not tpo_data["ok"]:
            await update.message.reply_text(tpo_data["message"])
            return

        await update.message.reply_text(
            f"`{tpo_data['document']['tpo']}`", parse_mode="markdown"
        )
    else:
        await update.message.reply_text(
            f"{update.effective_user.first_name} good to know!\n`Trust through verification`",
            parse_mode="markdown",
        )
