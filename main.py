import os
from flask import Flask, request
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)
import handler
from webhook.setup import set_webhook

load_dotenv()
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

bot.add_handler(CommandHandler("start", handler.start))
bot.add_handler(CommandHandler("verify", handler.verify))
bot.add_handler(MessageHandler(filters.TEXT, handler.website))
bot.add_handler(MessageHandler(filters.CONTACT, handler.contact))

flask_app = Flask(__name__)


@flask_app.route("/webhook", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(), bot.bot)
    await bot.process_update(update)
    return "ok"


if __name__ == "__main__":
    set_webhook()
    bot.run_webhook(
        listen="0.0.0.0",
        port=8000,
        url_path="webhook",
        webhook_url=f"{WEBHOOK_URL}/webhook",
    )
