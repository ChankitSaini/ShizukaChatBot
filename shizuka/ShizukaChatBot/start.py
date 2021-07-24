from shizuka import ShizukaChatBot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

SHIZUKA_START = """
I am Shizuka 『しずか』, An Intelligent ChatBot.[⠀](https://telegra.ph/file/f3696f6234fce4d4fb85d.jpg)
"""


@Shizuka.on_message(filters.command(["start"], prefixes = ["/" , "!"]) & ~filters.edited)
async def info(client, message):
    buttons = [[InlineKeyboardButton(text="Go inline", switch_inline_query_current_chat="shizuka "),],
                   [InlineKeyboardButton("Github", url="https://github.com/NeuroticCoders/ShizukaChatBot"), InlineKeyboardButton("Maintained by", url = "https://t.me/NeuroticAssociation")]]
    await Shizuka.send_message(chat_id = message.chat.id, text = SHIZUKA_START, reply_markup = InlineKeyboardMarkup(buttons))
