# Telegram Reminder Bot

A small, persistent Telegram bot for setting timed reminders directly in chat.  
Reminders are stored in SQLite and survive bot restarts.

Deployed on a DigitalOcean Ubuntu VPS and managed with `systemd`.

Built with **Python, python-telegram-bot, dateparser** and **SQLite**.

## Features

- `/remind <minutes> [message]` – schedule a reminder with natural language time input
- Examples: `in 10 minutes`, `tomorrow 9am`, `in 30 seconds`
- Fully persistent reminders via SQLite (`reminders.db`)
- Due reminders checked automatically in the background
- Bot token loaded from `.env`
- Runs on a VPS as a `systemd` service
- Automatically starts again after server reboot
- Logs available through `journalctl`
- Error handling and user-friendly replies

## Setup Instructions

1. Get a token from @BotFather
2. Clone the repo
3. Create `.env` file with `TOKEN=your_telegram_token_here`
4. Install requirements: `pip install -r requirements.txt`
5. Run the bot `python bot.py`


## Deployment

The bot is deployed on a DigitalOcean Ubuntu VPS.

Deployment steps included:

- creating a Droplet
- connecting with SSH
- installing Python, Git, and venv tools
- cloning the repo into `/opt/telegram-reminder-bot`
- creating a Python virtual environment
- installing dependencies from `requirements.txt`
- creating a server-side `.env` file
- running the bot manually for testing
- creating a `systemd` service
- enabling the service to start on reboot
- verifying the bot still worked after reboot

Useful service commands:

```
systemctl status reminder-fren
systemctl restart reminder-fren
journalctl -u reminder-fren -n 20
journalctl -u reminder-fren -f
```

## Demo

```
User: /remind in 30 seconds Drink water
Bot: Got it! I'll remind you at 2026-06-26 23:19:15 (⌯'▾'⌯)✨
(10 seconds later)
Bot: Drink Water
```

## Project Evolution

| Version | Change                                                |
|---------|-------------------------------------------------------|
| 0.1     | Basic in-memory reminders                             |
| 0.2     | .env support + proper project layout                  |
| 0.3     | JSON persistence                                      |
| 0.4     | Full SQLite migration + crash-proof polling           |
| 0.5     | Natural language time parsing with dateparser         |
| 0.6     | VPS deployment to DigitalOcean with systemd (current) |

    
## Roadmap

- [x] Deploy to VPS (DigitalOcean)
- [ ] `/list` - show active reminders
- [ ] `/cancel <id>` - delete a reminder
- [ ] `/done <id>` - mark a reminder/task complete
- [ ] Recurring reminders
- [ ] Improve timezone handling
- [ ] Add inline buttons for reminder control
- [ ] Improve data persistence: SQLite ➝ PostgreSQL

## License

This project is licensed under the MIT License. See LICENSE.
