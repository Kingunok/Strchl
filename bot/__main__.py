import asyncio
import logging
import sys
import traceback
import logging.handlers as handlers
from bot import TelegramBot
from bot.server import server
from . import initialize_clients

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(stream=sys.stdout),
        handlers.RotatingFileHandler("streambot.log", maxBytes=100000000, backupCount=3, encoding="utf-8"),
    ],
)

async def start_services():
    """Start bot, multi-client support, and web server."""
    print("\n------------------- Starting Services -------------------")

    print("Initializing Telegram Bot...")
    await TelegramBot.start()
    bot_info = await TelegramBot.get_me()
    TelegramBot.id = bot_info.id
    TelegramBot.username = bot_info.username
    TelegramBot.fname = bot_info.first_name
    print(f"✅ Telegram Bot Started: @{bot_info.username}")


    print("\nInitializing Additional Clients...")
    await initialize_clients()
    print("✅ Clients Initialized")

    print("\nStarting Web Server...")
    await server.serve()
    print("✅ Web Server Running")

    print("\n------------------- All Services Started -------------------")
    await asyncio.Event().wait()

async def cleanup():
    """Cleanup before exit."""
    await TelegramBot.stop()
    print("🛑 Stopped Telegram Bot")

if __name__ == '__main__':
    try:
        asyncio.run(start_services())
    except KeyboardInterrupt:
        print("⚠️ Shutdown Requested!")
    except Exception as e:
        logging.error("Error occurred: %s", traceback.format_exc())
    finally:
        asyncio.run(cleanup())
