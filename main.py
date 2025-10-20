from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
from dotenv import load_dotenv
import os
import json
from datetime import datetime, timedelta


# Load .env varsinto the environment
load_dotenv()
TOKEN = os.getenv("TOKEN")
REMINDERS_FILE = os.getenv("REMINDERS_FILE")


# Validate environment variables
if not TOKEN:
    raise ValueError("No TOKEN provided in .env file")
if not REMINDERS_FILE:
    raise ValueError("No REMINDERS_FILE provided in .env file")


# Load reminders from JSON
def load_reminders():
    """Load reminders from reminders.json. Return empty list if file doesn't exist."""
    try:
        with open(REMINDERS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Save reminders to JSON
def save_reminders(reminders):
    """Save reminders list to reminders.json with indentation."""
    with open(REMINDERS_FILE, 'w') as f:
        json.dump(reminders, f, indent=4)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    print()
    print(update.effective_chat.id)
    print("Text:", update.message.text)
    print("Name:", update.effective_user.first_name)
    print("Chat ID:", update.effective_chat.id)
    await update.message.reply_text("Hi fren 🌼! I'm your reminder bot. Use /remind to get a reminder!")


async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /remind command, store reminder in JSON, and send after delay."""
    try:
        delay = int(context.args[0])  # in minutes
        message = ' '.join(context.args[1:]) or "Hey! This is your reminder ✨"
        # str representation of current time + delay in iso format(YYYY-MM-DDTHH:MM:SS)
        remind_time = (datetime.now() + timedelta(minutes=delay)).isoformat()

        # Load existing reminders
        reminders = load_reminders()

        # Add new reminder
        reminders.append({
            "user_id": update.effective_user.id,
            "chat_id": update.effective_chat.id,
            "message": message,
            "remind_time": remind_time
        })

        # Save to file
        save_reminders(reminders)

        await update.message.reply_text(f"Okay! I'll remind you in {delay} minute(s). 🧠⏳")

        # Schedule reminder
        await asyncio.sleep(delay * 60)  # wait that many seconds
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

        # Remove reminder after sending
        reminders = [r for r in load_reminders() if r["remind_time"] != remind_time]
        save_reminders(reminders)

    except (IndexError, ValueError):
        await update.message.reply_text("Usage: /remind <minutes> <message>")


async def check_reminders(context: ContextTypes.DEFAULT_TYPE):
    """Check for due reminders every minute and send them."""
    while True:
        reminders = load_reminders()
        now = datetime.now()
        for reminder in reminders[:]:  # Copy to avoid modifying while iterating
            remind_time = datetime.fromisoformat(reminder["remind_time"])
            if now >= remind_time:
                await context.bot.send_message(
                    chat_id=reminder["chat_id"],
                    text=reminder["message"]
                )
                reminders.remove(reminder)
        save_reminders(reminders)
        await asyncio.sleep(60)  # Check every minute


if __name__ == '__main__':
    # Initialize bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("remind", remind))

    # Start reminder checker
    app.job_queue.run_repeating(check_reminders, interval=60, first=0)

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

