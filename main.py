import os
from dotenv import load_dotenv
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)
import handler


load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", handler.start))
app.add_handler(MessageHandler(filters.CONTACT, handler.contact))

app.run_polling()
