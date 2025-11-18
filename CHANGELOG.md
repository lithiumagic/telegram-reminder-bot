# Changelog

All notable changes to this project will be documented in this file.

## [0.4.0] - 2025-11-19
### Changed
- Replaced JSON-based storage with SQLite database
- All reminders now stored persistently in `reminders.db`
- Scheduled reminders now handled entirely via recurring `check_reminders()`, removing need for `JobQueue` one-off jobs

### Removed
- Removed `send_reminder()` scheduled job (redundant with periodic check)

## [0.3.0] - 2025-10-19
### Added
- Persistence with JSON

## [0.2.0] - 2025-10-18
### Added
- Support for `.env` file using `python-dotenv`.
- Now reads `TOKEN` from environment for better security.
- Added project on github, added LICENSE, README, CHANGELOG and requirements

### Changed
- Refactored to raise an error if no `TOKEN` is found.
- Improved error message handling in `/remind`.

## [0.1.0] - 2025-10-17
### Added
- Basic bot with `/start` and `/remind <minutes> <message>` commands.
- Sends a delayed message using `asyncio.sleep`.
- Replies to user with reminder text after a delay.
