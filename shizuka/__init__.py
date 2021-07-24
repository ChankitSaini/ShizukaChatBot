import os
from pyrogram import Client

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
TOKEN = os.environ.get("TOKEN", None)

SHIZUKA = Client(':memory:', api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
