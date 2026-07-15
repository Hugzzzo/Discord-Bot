# Discord Channel Manager Bot

A lightweight Discord bot built with **discord.py** that helps administrators manage channels directly from Discord commands.

## ✨ Features

- 📄 Create text channels
- 🔊 Create voice channels
- ❌ Delete any channel
- 🧹 Clear all messages from a text channel

---

## Commands

| Command | Description |
|---------|-------------|
| `&canal_texto <name>` | Creates a text channel |
| `&canal_voz <name>` | Creates a voice channel |
| `&eliminar_canal <name>` | Deletes a channel |
| `&vaciar_canal <name>` | Deletes every message inside a text channel |

Example:

```text
&canal_texto general-2
&canal_voz Música
&eliminar_canal pruebas
&vaciar_canal general
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/discord-channel-manager-bot.git
```

Go inside the folder:

```bash
cd discord-channel-manager-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a file called **secret.py**

```python
TOKEN = "YOUR_DISCORD_BOT_TOKEN"
```

Then simply run

```bash
python main.py
```

---

## Requirements

- Python 3.10+
- discord.py
- requests

Install:

```bash
pip install -r requirements.txt
```

---

## Permissions

The bot requires:

- Manage Channels
- Manage Messages
- Read Messages
- Send Messages

Administrator permissions are recommended.

---

## Built With

- Python
- discord.py

---

## License

This project is licensed under the MIT License.
