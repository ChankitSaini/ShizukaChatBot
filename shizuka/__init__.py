import os

from pyrogram import Client

API_ID = os.environ.get('API_ID', None)
API_HASH = os.environ.get('API_HASH', None)
TOKEN = os.environ.get('TOKEN', None)
START_IMG = os.environ.get(
    'START_IMG',
    'https://telegra.ph/file/f3696f6234fce4d4fb85d.jpg',
)

SHIZUKA = Client(':memory:', api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
