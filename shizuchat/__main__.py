import sys
import asyncio
import importlib
from pyrogram import idle
from pyrogram.types import BotCommand
from config import OWNER_ID
from shizuchat import LOGGER, shizuchat
from shizuchat.modules import ALL_MODULES


async def anony_boot():
    try:
        await shizuchat.start()
    except Exception as ex:
        LOGGER.error(ex)
        sys.exit(1)

    # Import all modules
    for all_module in ALL_MODULES:
        importlib.import_module(f"shizuchat.modules.{all_module}")
        LOGGER.info(f"Imported: {all_module}")

    # Set bot commands
    try:
        await shizuchat.set_bot_commands([
            BotCommand("start", "Start the bot"),
            BotCommand("help", "Help menu"),
            BotCommand("ping", "Check bot status"),
            BotCommand("shipping", "Couples of the day"),
            BotCommand("rankings", "User leaderboard"),
        ])
        LOGGER.info("Bot commands set.")
    except Exception as ex:
        LOGGER.error(f"Failed to set commands: {ex}")

    LOGGER.info(f"@{shizuchat.username} Started!")

    try:
        await shizuchat.send_message(int(OWNER_ID), f"{shizuchat.mention} is online.")
    except:
        LOGGER.warning("Start bot from owner account first.")

    await idle()


if __name__ == "__main__":
    asyncio.run(anony_boot())
