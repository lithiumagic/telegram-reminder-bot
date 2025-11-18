# Telegram Reminder Bot

A small, persistent Telegram bot for setting timed reminders directly in chat.  
Reminders are stored in SQLite and survive bot restarts.

Built with **python-telegram-bot v20+** and **SQLite**.

## Features

- `/remind <minutes> [message]` – schedule a reminder
- Fully persistent reminders via SQLite (`reminders.db`)
- Due reminders checked every 60 seconds
- Bot token loaded from `.env`
- Error handling and user-friendly replies

## Setup Instructions

1. Get a token from @BotFather
2. Clone the repo
3. Create `.env` file with `TOKEN=your_telegram_token_here`
4. Install requirements: `pip install -r requirements.txt`
5. Run the bot `python bot.py`

## Demo

```
User: /remind 30 Drink water
Bot: Okay! I'll remind you in 30 minute(s).
User: /remind 1
Bot: (uses default message) Hey! This is your reminder ✩°｡⋆⸜(˙꒳˙)
```

## Project Evolution

|Version|Change|
|---|---|
|0.1|Basic in-memory reminders|
|0.2|.env support + proper project layout|
|0.3|JSON persistence|
|0.4|Full SQLite migration + crash-proof polling (current)|

    
## Roadmap

- [ ] `/list` - show active reminders
- [ ] `/cancel <id>` - delete a reminder
- [ ] Recurring reminders
- [ ] Add inline buttons for reminder control
- [ ] Deploy to VPS (DigitalOcean)
- [ ] Improve data persistence: SQLite ➝ PostgreSQL

## License

This project is licensed under the MIT License. See LICENSE.
