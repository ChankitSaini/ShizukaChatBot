from pyrogram import filters
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

from shizuka import SHIZUKA
from shizuka import START_IMG

SHIZUKA_START = f'I am Shizuka 『しずか』, An Intelligent ChatBot.[⠀]({START_IMG})'


@SHIZUKA.on_message(filters.command(['start'], prefixes=['/', '!']) & ~filters.edited)
async def info(client, message):
    buttons = [
        [
            InlineKeyboardButton(
                text='Go inline',
                switch_inline_query_current_chat='shizuka ',
            ),
        ],
        [
            InlineKeyboardButton(
                'Github',
                url='https://github.com/ChankitSaini/ShizukaChatBot',
            ),
            InlineKeyboardButton(
                'Maintained by',
                url='https://t.me/NeuroticAssociation',
            ),
        ],
    ]
    await SHIZUKA.send_message(
        chat_id=message.chat.id,
        text=SHIZUKA_START,
        reply_markup=InlineKeyboardMarkup(buttons),
    )
