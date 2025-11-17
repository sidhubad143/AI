# client.py
from pyrogram import Client
from pyrogram.enums import ParseMode
import config

class ShizuChat(Client):
    def __init__(self):
        super().__init__(
            name="shizuchat",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.DEFAULT,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = (self.me.first_name or "") + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

    async def stop(self):
        await super().stop()

shizuchat = ShizuChat()
