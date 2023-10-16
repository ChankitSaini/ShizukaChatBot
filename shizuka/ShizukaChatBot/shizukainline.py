import os
import random
import re
import sys
import traceback
from datetime import datetime
from urllib.parse import unquote
from urllib.parse import urlparse

import aiohttp
import requests
from pykeyboard import InlineKeyboard
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineQuery
from pyrogram.types import InlineQueryResultAnimation
from pyrogram.types import InlineQueryResultArticle
from pyrogram.types import InlineQueryResultPhoto
from pyrogram.types import InputTextMessageContent

from shizuka import SHIZUKA


async def fetch(url):
    async with aiohttp.ClientSession() as session, session.get(url) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


@SHIZUKA.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.lower()

    answers = []
    if string.split()[0] == "shizuka":
        if len(string.split()) < 2:
            await client.answer_inline_query(
                query.id,
                results=answers,
                switch_pm_text="Shizuka | Chat [text]",
                switch_pm_parameter="shizuka",
            )
            return
        shizuka = string.split(None, 1)[1].strip()
        Shizuka = await shizukachatbot(answers, shizuka)
        await client.answer_inline_query(query.id, results=Shizuka, cache_time=2)


async def shizukachatbot(answers, text):
    URL = f"http://api.brainshop.ai/get?bid=161901&key=Sgv5QAk5wEbhqYn0&uid=chankit&msg={text}"
    result = await fetch(URL)
    buttons = InlineKeyboard(row_width=1)
    buttons.add(
        InlineKeyboardButton(
            "Shizuka",
            switch_inline_query_current_chat="shizuka",
        ),
    )
    caption = f"""
**You:** `{text}`
**Shizuka:** `{result['cnt']}`"""
    answers.append(
        InlineQueryResultPhoto(
            photo_url="https://telegra.ph/file/c8f2e290ba36052058154.jpg",
            title="Shizuka",
            description=result["cnt"],
            caption=caption,
            reply_markup=buttons,
        ),
    )
    return answers
