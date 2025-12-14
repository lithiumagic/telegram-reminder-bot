import os
import sqlite3
import dateparser
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from datetime import datetime

# Load .env vars into the environment
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Validate environment variables
if not TOKEN:
    raise ValueError("No TOKEN provided in .env file")


# Initialize the database
def init_db():
    conn = sqlite3.connect("reminders.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS reminders
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  chat_id INTEGER,
                  message TEXT,
                  remind_time TEXT,
                  status TEXT DEFAULT 'pending')""")
    conn.commit()
    conn.close()


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sorry, I don't understand that (´ ∀ ` *). Try /remind or /start.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update)
    print()
    print(update.effective_chat.id)
    print("Text:", update.message.text)
    print("Name:", update.effective_user.first_name)
    print("Chat ID:", update.effective_chat.id)
    await update.message.reply_text("Hi fren ヾ( ˃ᴗ˂ )◞ • *✰! I'm your reminder bot. Use /remind to get a reminder!")


async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        return await update.message.reply_text("Usage: /remind <time> <message>")

    full_text = " ".join(context.args)

    # 1. Parse time ONLY from the *start* of the text
    # Try increasing prefixes until parsing fails
    parts = full_text.split()
    parsed_time = None
    cutoff_index = 0

    for i in range(1, len(parts) + 1):
        candidate = " ".join(parts[:i])
        dt = dateparser.parse(candidate, settings={'PREFER_DATES_FROM': 'future'})
        if dt:
            parsed_time = dt
            cutoff_index = i
        else:
            break

    if not parsed_time:
        return await update.message.reply_text("Sorry, I couldn't understand the time you gave me 😢")

    # 2. Extract message
    message = " ".join(parts[cutoff_index:]).strip()
    if not message:
        message = "Hey! This is your reminder ✩°｡⋆⸜(˙꒳˙)"

    # 3. Validate future time
    if parsed_time <= datetime.now():
        return await update.message.reply_text("Time must be in the future (｡•́︿•̀｡)")

    # 4. Store reminder
    conn = sqlite3.connect("reminders.db")
    c = conn.cursor()
    c.execute("INSERT INTO reminders (user_id, chat_id, message, remind_time, status) VALUES (?, ?, ?, ?, ?)",
              (update.effective_user.id,
               update.effective_chat.id,
               message,
               parsed_time.isoformat(),
               "pending"))
    conn.commit()
    conn.close()

    await update.message.reply_text(
        f"Got it! I'll remind you at {parsed_time.strftime('%Y-%m-%d %H:%M:%S')} (⌯'▾'⌯)✨"
    )


async def check_reminders(context: ContextTypes.DEFAULT_TYPE):
    """Periodic check for any due reminders (e.g., after restarts)."""
    now_iso = datetime.now().isoformat()

    conn = sqlite3.connect("reminders.db")
    c = conn.cursor()
    c.execute("SELECT id, chat_id, message, remind_time FROM reminders WHERE remind_time <= ? AND status = ?",
              (now_iso, "pending"))
    reminders = c.fetchall()

    for r_id, chat_id, message, remind_time in reminders:
        await context.bot.send_message(chat_id=chat_id, text=message)
        c.execute("UPDATE reminders SET status = ? WHERE id = ?",
                  ("sent", r_id))
        print(f"Reminder sent: {message} → chat {chat_id} at {datetime.now()}")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # Initialize database
    init_db()

    # Initialize bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("remind", remind))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Start reminder checker every minute
    app.job_queue.run_repeating(check_reminders, interval=60, first=0, name="reminder_checker")

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()
