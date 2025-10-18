from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env vars into the environment

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("No TOKEN provided in .env file")


async def hello_fren(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    print()
    print(update.effective_chat.id)
    print("Text:", update.message.text)
    print("Name:", update.effective_user.first_name)
    print("Chat ID:", update.effective_chat.id)
    await update.message.reply_text("Hi fren 🌼! I'm your reminder bot. Use /remind to get a reminder!")


async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        delay = int(context.args[0])  # in minutes
        message = ' '.join(context.args[1:]) or "Hey! This is your reminder ✨"
        await update.message.reply_text(f"Okay! I'll remind you in {delay} minute(s). 🧠⏳")
        await asyncio.sleep(delay * 60)  # wait that many seconds
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except (IndexError, ValueError):
        await update.message.reply_text("Usage: /remind <minutes> <message>")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", hello_fren))
    app.add_handler(CommandHandler("remind", remind))

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

