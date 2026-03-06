# Auto VC Bot

A simple, lightweight **"Join to Create"** Discord bot built with Python and `discord.py`.

## Features

- **Zero Lag:** Instantly creates a new voice channel when a user joins the Generator channel.
- **Auto-Cleanup:** Deletes the custom voice channel immediately when the last person leaves.
- **Channel Ownership:** Grants the creator permissions to manage their room.

## Requirements

- Python 3.8+
- `discord.py`
- `python-dotenv`

## Setup Instructions

### 1. Install dependencies

```bash
pip install discord.py python-dotenv
```

### 2. Configure your secrets

Create a file named `.env` in the root directory.

Add your bot token to the file like this:

```env
DISCORD_TOKEN=your_token_here
```

### 3. Configure your server

- Open `bot.py`
- Change the `GENERATOR_CHANNEL_ID` variable to the **ID of the voice channel users should click**

Ensure your bot has the following **Privileged Gateway Intents** enabled in the Discord Developer Portal:

- Server Members Intent
- Message Content Intent
- Presence Intent

### 4. Run the bot

```bash
python3 bot.py
```

For **24/7 hosting on Ubuntu**, using **PM2** is recommended.
