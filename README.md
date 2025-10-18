A simple async Telegram bot that sends scheduled (temporary) reminders.

## Features
- Simple `/remind <minutes> <message>` reminders
- Async handling for responsive reminders
- Secure config via `.env` environment variables

## Setup Instructions

1. Clone the repo
2. Create a `.env` file:
TOKEN=your_telegram_token_here

3. Install requirements
pip install python-telegram-bot python-dotenv

4. Run the bot
python bot.py

## Demo
# TODO: add screenshot later

## Roadmap
- [x] Use environment variables for secret management
- [ ] Add persistent storage (SQLite/JSON)
- [ ] Add `/listreminders` and `/cancelreminder`
- [ ] Add inline buttons
- [ ] Deploy on VPS (DigitalOcean)

## License
MIT
