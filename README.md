# Telegram Reminder Bot

A lightweight, async Telegram bot that helps users schedule simple reminders via chat.

Built with Python using the python-telegram-bot library and asyncio. Reminders are stored persistently using a JSON file (SQLite support coming soon).

## Features
- Set quick reminders with /remind <minutes> <message>
- Async handling ensures smooth user experience
- Persists reminders even if the bot restarts
- Environment-variable-based configuration (via .env)
- Cron-style reminder checking with job_queue

## Setup Instructions

1. Clone the repo
2. Create a `.env` file:
TOKEN=your_telegram_token_here

3. Install requirements
pip install python-telegram-bot python-dotenv

4. Run the bot
python bot.py

## Demo
TODO: (screenshot placeholder)
```
User: /remind 15 Take a break
Bot: Okay! I'll remind you in 15 minute(s).
```


## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/telegram-reminder-bot.git
cd telegram-reminder-bot
```

### 2. Set Up Environment

Create a `.env` file in the root directory:

```
TOKEN=your_telegram_bot_token
REMINDERS_FILE=reminders.json
```

> 💡 You can get your bot token from [@BotFather](https://t.me/BotFather) on Telegram.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Bot

```bash
python bot.py
```

---

## Usage

- Start the bot:  
    `/start`
    
- Set a reminder:  
    `/remind 10 Stretch your legs!`
    
- Example:
    
    > `/remind 60 Call mom`
    
## Roadmap
- [x] Use environment variables for security
- [x] Store reminders in JSON
- [ ] Improve data persistence: JSON ➝ SQLite ➝ PostgreSQL
- [ ] Add `/listreminders` and `/cancelreminder`
- [ ] Add recurring reminders (`/remind_every`)
- [ ] Add inline buttons for reminder control
- [ ] Deploy to VPS (DigitalOcean)


## License
MIT

