# Changelog

All notable changes to this project will be documented in this file.

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
