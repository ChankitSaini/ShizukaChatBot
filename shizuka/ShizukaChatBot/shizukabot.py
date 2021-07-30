import asyncio
import re

import aiohttp
import emoji
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from coffeehouse.exception import CoffeeHouseError as CFError

from shizuka import SHIZUKA

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

BOT_ID = 1699240021


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


en_chats = []


@SHIZUKA.on_message(filters.text & filters.reply & ~filters.bot & ~filters.via_bot & ~filters.forwarded, group=2)
async def shizuka(client, message):
    if message.reply_to_message.from_user.id != BOT_ID:
        message.continue_propagation()
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
        querystring = {
            "bid": "158053",
            "key": "rSXmqf3MCQqrFpQf",
            "uid": "mashape",
            "msg": {chankit},
        }
        headers = {
            "x-rapidapi-key":
            "4340f386fdmsh1d96fdb95a0d4bcp1e7794jsnc18973f05156",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
        
    saini =  response
    try:
        await SHIZUKA.send_chat_action(message.chat.id, "typing")
        await message.reply_text(saini)
    except CFError as e:
        print(e)
@SHIZUKA.on_message(filters.text & filters.private & ~filters.reply & ~filters.bot)
async def neurotic(client, message)
        querystring = {
        "bid": "158053",
        "key": "rSXmqf3MCQqrFpQf",
        "uid": "mashape",
        "msg": {chankit},
    }
        headers = {
        "x-rapidapi-key": "4340f386fdmsh1d96fdb95a0d4bcp1e7794jsnc18973f05156",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
        response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
        saini =  response
    try:
        await SHIZUKA.send_chat_action(message.chat.id, "typing")
        await message.reply_text(saini)
    except CFError as e:
        print(e)


@SHIZUKA.on_message(
    filters.regex("Shizuka|shizuka|SHIZUKA")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel)
async def neurotic(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if ([(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    
    querystring = {
        "bid": "158053",
        "key": "rSXmqf3MCQqrFpQf",
        "uid": "mashape",
        "msg": {chankit},
    }
    headers = {
        "x-rapidapi-key": "4340f386fdmsh1d96fdb95a0d4bcp1e7794jsnc18973f05156",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    saini =  response    
    try:
        await SHIZUKA.send_chat_action(message.chat.id, "typing")
        await message.reply_text(saini)
    except CFError as e:
        print(e)
