import os
from pyrogram import Client
from pyromod import listen

API_ID = int(os.environ.get("API_ID", "17492714"))
API_HASH = os.environ.get("API_HASH", "26b7fd64901c7d3c6276cd06e272ce95")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5015892079:AAEmNjqfIOBI0w6nDjcd3W-Y17dG_OopGhM")


bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
