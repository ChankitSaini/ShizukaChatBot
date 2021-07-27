import asyncio
import re

import aiohttp
import emoji
import requests
from googletrans import Translator as google_translator
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from coffeehouse.exception import CoffeeHouseError as CFError

from shizuka import SHIZUKA

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

translator = google_translator()

BOT_ID = 1699240021


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


# Chatbot Modules By  @InukaAsith

en_chats = []


@SHIZUKA.on_message(
    filters.text & filters.reply & ~filters.bot & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
async def shizuka(client, message):
    if message.reply_to_message.from_user.id != BOT_ID:
        message.continue_propagation()
    msg = message.text
    chat_id = message.chat.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        chankit = msg
        chankit = chankit.replace("shizuka", "Aco")
        chankit = chankit.replace("Shizuka", "Aco")
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
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("Aco", "Shizuka")
        result = result.replace("Eliza", "@ShizukaChatBot")
        result = result.replace("Hi~", "Hello Friend I Am @ShizukaChatBot")
        result = result.replace(
            "My dear great botmaster, Neurotic Association..",
            "Made By @NeuroticAssociation.",
        )
        result = result.replace("Have the control right.",
                                "My creator  is @ChankitSaini ")
        result = result.replace(
            "I was created by @NeuroticAssociation.",
            "I was created by @madepranav Team.",
        )
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace(r"<\/a>", "</a>")
        saini = result
        try:
            await SHIZUKA.send_chat_action(message.chat.id, "typing")
            await message.reply_text(saini)
        except CFError as e:
            print(e)
    else:
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
        else:
            rm = msg
        try:
            lan = translator.detect(rm)
            lan = lan.lang  
            except:
        return
    chankit = rm
    if not "en" in lan and not lan == "":
        try:
            chankit = translator.translate(chankit, dest="en")
            chankit = chankit.text
        except:
            return

        chankit = chankit.replace("shizuka", "Aco")
        chankit = chankit.replace("Shizuka", "Aco")
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
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("Aco", "Shizuka")
        result = result.replace("Eliza", "@ShizukaChatBot")
        result = result.replace("Hi~", "Hello Friend I Am @ShizukaChatBot")
        result = result.replace(
            "My dear great botmaster,  Neurotic Association.",
            "Made By  @NeuroticAssociation",
        )
        result = result.replace("Have the control right.",
                                "My creator is @ChankitSaini")
        result = result.replace("I was created by @NeuroticAssociation.",
                                "I was created by @ChankitSaini.")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace(r"<\/a>", "</a>")
        saini = result
        if not "en" in lan and not lan == "":
            saini = translator.translate(saini, lang_tgt=lan[0])
        try:
            await SHIZUKA.send_chat_action(message.chat.id, "typing")
            await message.reply_text(saini)
        except CFError as e:
            print(e)


@SHIZUKA.on_message(filters.text & filters.private & ~filters.reply
                    & ~filters.bot)
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
    else:
        rm = msg
        lan = translator.detect(rm)
    chankit = rm
    if not "en" in lan and not lan == "":
        chankit = translator.translate(chankit, lang_tgt="en")

    chankit = chankit.replace("shizuka", "Aco")
    chankit = replace("Shizuka", "Aco")
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
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("Aco", "Shizuka")
    result = result.replace("Eliza", "@ShizukaChatBot")
    result = result.replace("Hi~", "Hello Friend I Am @ShizukaChatBot")
    result = result.replace("My dear great botmaster, Neurotic Association.",
                            "Made By @ChankitSaini")
    result = result.replace("Have the control right.",
                            "My creator is @ChankitSaini")
    result = result.replace("I was created by Neurotic Association.",
                            "I was created by @ChankitSaini.")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace(r"<\/a>", "</a>")
    saini = result
    if not "en" in lan and not lan == "":
        saini = translator.translate(saini, lang_tgt=lan[0])
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
    else:
        rm = msg
        lan = translator.detect(rm)
    chankit = rm
    if not "en" in lan and not lan == "":
        chankit = translator.translate(chankit, lang_tgt="en")

    chankit = chankit.replace("shizuka", "Aco")
    chankit = chankit.replace("Shizuka", "Aco")
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
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("Aco", "Shizuka")
    result = result.replace("Eliza", "@ShizukaChatBot")
    result = result.replace("Hi~", "Hello Friend I Am @ShizukaChatBot")
    result = result.replace("My dear great botmaster, Neurotic Association.",
                            "Made By ChankitSaini")
    result = result.replace("Have the control right.",
                            "My creator is @ChankitSaini")
    result = result.replace("I was created by Chankit Saini.",
                            "I was created by @madepranav Team.")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace(r"<\/a>", "</a>")
    saini = result
    if not "en" in lan and not lan == "":
        saini = translator.translate(saini, lang_tgt=lan[0])
    try:
        await SHIZUKA.send_chat_action(message.chat.id, "typing")
        await message.reply_text(saini)
    except CFError as e:
        print(e)
