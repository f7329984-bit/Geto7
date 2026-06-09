import asyncio
import time
import random
import json
import os
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

#=============== CONFIG ================
API_ID = 39035274
API_HASH = "6a0b24e16c4bea2bbc975b7dbb0c1e64"
BOT_TOKEN = "8951612687:AAGP6DJYz0VKsD_NZQyz5_DlM6sZHWqoWd8"
OWNER_ID = 8722144519
BOT_USERNAME = "ll_SUPRRME_XD_7_ll_BOT"

#=============== CUSTOM LINES (EMPTY - WILL LOAD FROM FILE) ================
CUSTOM_LINES = [
    "🔥 teri mummy ki chut!",
    "⚡ bahen k lode teri dadi ki black hairy pussy",
    "🚀 teri mummy ko ulta ltkakr taangduga aur uski chut maruga!",
    "✨ bsdk teri mummy teri dadi sb randi ki bachi h",
    "bahenklodo tumhari maa meri setting",
    "bahenklodo tumhari maa meri setting",
    "teri mummy randi h randi bsdk",
    "teri mummy ki pussy m scooter dalduga",
    "teri mummy ki pussy me cum krduga randi maa k bache",
    "tera khandan hi randiyo ka h",
    "teri dadi ki pussy me mera lund",
    "teri mummy ko chodkr ulta ltkakr uske muh me loda deduga",
    "teri mummy ko deepthroat deduga madarchod k bache",
    "✌️✌️tera papa bhi randi ki aulad h bsdk",
    "teri mummy ko yoga sikhaduga aur usko different styles me choduga",
    "tera papa hu mai teri mummy ka bf jis s vo chudkr gyi thi",
    "teri maa ki pussy me scooter dalduga bahen k lode🤣🤣",
    "teri maa ki chut me bihari gutka khakr thuk kr chale gye the🔥🔥",
    "💀💀teri maa ka bosda randi k beej",
    "✌️✌️teri maa ki chut me 2finger dekr uska paani nikalduga0",
    "🔥🔥teri maa k muh me gass pipe dekr uski gaand me fire lgakr tere baap ki gaand jalauga",
    "😂😍😍teri randi maa ko chodkr maine gb road pr beach diya tha",
    "🙌🙌teri mummy k haath divar pr lgvadiye the 10bihariyo ne",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑵𝑭𝑻 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑳𝑨𝑮𝑬 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑳𝑨𝑮𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑳𝑨𝑮𝑬 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰ℙ𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
]

# =============== DUMMY SERVER FOR RENDER ================
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

    def log_message(self, format, *args):
        pass

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

app = Client(
    "fast_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

#=============== DATA STORAGE ================
sudo_users = {OWNER_ID}
spam_active = False
custom_spam_active = False
custom_spam_task = None

#=============== FILE PATHS ================
SUDO_FILE = "sudo_users.json"
LINES_FILE = "custom_lines.json"

#=============== DATA PERSISTENCE FUNCTIONS ================

def load_all_data():
    global sudo_users, CUSTOM_LINES
    
    print("\n📂 LOADING SAVED DATA...")
    
    try:
        if os.path.exists(SUDO_FILE):
            with open(SUDO_FILE, "r") as f:
                loaded_sudo = json.load(f)
                if loaded_sudo:
                    sudo_users = set(loaded_sudo)
                    print(f"✅ Loaded {len(sudo_users)} sudo users")
    except Exception as e:
        print(f"⚠️ Error loading sudo users: {e}")
    
    try:
        if os.path.exists(LINES_FILE):
            with open(LINES_FILE, "r", encoding='utf-8') as f:
                loaded_lines = json.load(f)
                if loaded_lines:
                    CUSTOM_LINES = loaded_lines
                    print(f"✅ Loaded {len(CUSTOM_LINES)} custom lines")
    except Exception as e:
        print(f"⚠️ Error loading custom lines: {e}")
    
    print("✅ DATA LOADING COMPLETE!\n")

def save_sudo_users():
    try:
        with open(SUDO_FILE, "w") as f:
            json.dump(list(sudo_users), f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving sudo users: {e}")
        return False

def save_custom_lines():
    try:
        with open(LINES_FILE, "w", encoding='utf-8') as f:
            json.dump(CUSTOM_LINES, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving custom lines: {e}")
        return False

def save_all_data():
    save_sudo_users()
    save_custom_lines()
    print("💾 All data saved!")

#=============== BUTTONS ================
def get_main_keyboard():
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me Baby", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("🏠 My Home", callback_data="home")],
        [InlineKeyboardButton("👑 My Master", url="https://t.me/ll_SUPRRME_XD_ll")],
        [InlineKeyboardButton("❓ Help", callback_data="help")],
        [InlineKeyboardButton("⚡ Get Sudo", url="https://t.me/ll_SUPRRME_XD_ll")]
    ])
    return keyboard

#=============== CUSTOM LINES SPAM FUNCTION ================
async def custom_spam_loop(client, chat_id, target_user_id, count):
    global custom_spam_active
    
    target_user = await client.get_users(target_user_id)
    mention = target_user.mention
    
    if not CUSTOM_LINES:
        await client.send_message(chat_id, f"{mention} ⚠️ No custom lines found! Use !addline to add lines.")
        custom_spam_active = False
        return
    
    i = 0
    retry_count = 0
    max_retries = 5
    
    while i < count and custom_spam_active:
        try:
            line = random.choice(CUSTOM_LINES)
            await client.send_message(chat_id, f"{mention} {line}")
            i += 1
            retry_count = 0
            await asyncio.sleep(0)
                
        except Exception as e:
            error_str = str(e).lower()
            
            if "flood" in error_str or "too many" in error_str or "429" in error_str:
                retry_count += 1
                if retry_count > max_retries:
                    await client.send_message(chat_id, f"❌ Rate limited! Stopped at {i}/{count}.")
                    break
                wait = retry_count
                await client.send_message(chat_id, f"⚠️ Flood wait {wait}s... ({i}/{count})")
                await asyncio.sleep(wait)
            elif "bot was blocked" in error_str:
                await client.send_message(chat_id, f"❌ Bot was blocked! Stopping.")
                break
            else:
                print(f"Custom spam error: {e}")
                await asyncio.sleep(1)
    
    if custom_spam_active and i > 0:
        try:
            await client.send_message(chat_id, f"✅ Done! Sent {i} messages.")
        except:
            pass
    
    custom_spam_active = False

#=============== CUSTOM LINES SPAM COMMAND ================
@app.on_message(filters.command("r", prefixes="!") & filters.group)
async def custom_r_command(client, message: Message):
    global custom_spam_active, custom_spam_task
    
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Not authorized!")
        return
    
    if not message.reply_to_message:
        await message.reply_text("❌ Reply to a user first!\nUsage: !r 100")
        return
    
    parts = message.text.split()
    
    if len(parts) != 2:
        await message.reply_text("❌ Usage: !r <count>\nExample: !r 100\n\nMax: 10000")
        return
    
    try:
        count = int(parts[1])
        if count > 10000:
            await message.reply_text("❌ Max limit is 10000!")
            return
        if count < 1:
            await message.reply_text("❌ Count must be at least 1!")
            return
    except ValueError:
        await message.reply_text("❌ Invalid number!")
        return
    
    if not CUSTOM_LINES:
        await message.reply_text("❌ No custom lines! Use !addline to add.")
        return
    
    target_user = message.reply_to_message.from_user
    chat_id = message.chat.id
    
    if custom_spam_active:
        custom_spam_active = False
        if custom_spam_task:
            custom_spam_task.cancel()
        await asyncio.sleep(0.3)
    
    custom_spam_active = True
    
    await message.reply_text(
        f"✅ **RAID STARTED!**\n\n"
        f"🎯 Target: {target_user.first_name}\n"
        f"🔢 Count: {count}\n"
        f"📝 Lines: {len(CUSTOM_LINES)}\n"
        f"⚡ Speed: MAXIMUM\n"
        f"🛑 Stop: !stopr"
    )
    
    await message.delete()
    
    custom_spam_task = asyncio.create_task(
        custom_spam_loop(client, chat_id, target_user.id, count)
    )

#=============== STOP CUSTOM SPAM ================
@app.on_message(filters.command("stopr", prefixes="!") & filters.group)
async def stop_custom_spam(client, message: Message):
    global custom_spam_active, custom_spam_task
    
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Not authorized!")
        return
    
    if custom_spam_active:
        custom_spam_active = False
        if custom_spam_task:
            custom_spam_task.cancel()
        await message.reply_text("🛑 **RAID STOPPED!**")
        await message.delete()
    else:
        await message.reply_text("⚠️ No active raid!")
        await message.delete()

#=============== ADD CUSTOM LINE ================
@app.on_message(filters.command("addline", prefixes="!") & filters.private)
async def add_line_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can add lines!")
        return
    
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply_text("❌ Usage: !addline <your text line>")
        return
    
    new_line = parts[1]
    CUSTOM_LINES.append(new_line)
    save_custom_lines()
    
    await message.reply_text(f"✅ Line added!\nTotal lines: {len(CUSTOM_LINES)}\n\nLine: {new_line[:100]}")

#=============== REMOVE LINE ================
@app.on_message(filters.command("removeline", prefixes="!") & filters.private)
async def remove_line_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can remove lines!")
        return
    
    parts = message.text.split()
    if len(parts) != 2:
        await message.reply_text("❌ Usage: !removeline <line_number>")
        return
    
    try:
        line_num = int(parts[1]) - 1
        if 0 <= line_num < len(CUSTOM_LINES):
            removed = CUSTOM_LINES.pop(line_num)
            save_custom_lines()
            await message.reply_text(f"✅ Removed line {line_num+1}: {removed[:100]}")
        else:
            await message.reply_text(f"❌ Line number out of range! (1-{len(CUSTOM_LINES)})")
    except ValueError:
        await message.reply_text("❌ Invalid line number!")

#=============== VIEW LINES ================
@app.on_message(filters.command("lines", prefixes="!") & filters.private)
async def view_lines_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can view lines!")
        return
    
    if not CUSTOM_LINES:
        await message.reply_text("📝 No custom lines found!\nUse !addline to add.")
        return
    
    lines_text = f"📝 **Custom Lines (Total: {len(CUSTOM_LINES)})**\n\n"
    for i, line in enumerate(CUSTOM_LINES[:50], 1):
        lines_text += f"{i}. {line[:80]}\n"
    
    if len(CUSTOM_LINES) > 50:
        lines_text += f"\n... and {len(CUSTOM_LINES)-50} more"
    
    await message.reply_text(lines_text)

#=============== START COMMAND ================
@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    user = message.from_user
    await message.reply_text(
        f"🔥 Welcome {user.first_name}! 🔥\n\n"
        f"💪 Powerful Raid Bot\n\n"
        f"**Data Persistence:** ✅ Enabled\n"
        f"**Lines Saved:** {len(CUSTOM_LINES)}\n"
        f"**Sudo Users:** {len(sudo_users)}\n\n"
        f"Use buttons below!",
        reply_markup=get_main_keyboard()
    )

#=============== BUTTON CALLBACK ================
@app.on_callback_query()
async def button_callback(client, callback_query):
    data = callback_query.data

    if data == "help":
        help_text = f"""
🤖 **BOT COMMANDS** 🤖

📊 **Utility:**
• !alive - Check bot status
• !ping - Check bot speed

⚡ **Raid Commands (Sudo only):**
• !r <count> - Raid user with custom lines
• !stopr - Stop active raid

👑 **Owner Commands (Private Chat):**
• !addline <text> - Add custom line (SAVED)
• !removeline <num> - Remove line
• !lines - View all lines
• !add - Add sudo user
• !remove - Remove sudo user
• !sudolist - List sudo users

💾 **Data Persistence:**
• All data auto-saves to files
• Survives bot restarts
• Survives Render resets

💫 **Custom Lines:** {len(CUSTOM_LINES)}
"""

        await callback_query.message.edit_text(
            help_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )

    elif data == "back":
        await callback_query.message.edit_text(
            "🔥 Welcome Back! 🔥\n\nData is safely saved!",
            reply_markup=get_main_keyboard()
        )

    elif data == "home":
        await callback_query.message.edit_text(
            f"🏠 **My Home**\n\n"
            f"📊 Bot Stats:\n"
            f"• Sudo Users: {len(sudo_users)}\n"
            f"• Custom Lines: {len(CUSTOM_LINES)}\n"
            f"• Status: Active 🟢\n"
            f"• Data Persistence: ✅ ON\n\n"
            f"👑 Owner: {OWNER_ID}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )

    await callback_query.answer()

#=============== UTILITY COMMANDS ================
@app.on_message(filters.command("alive", prefixes="!") & filters.group)
async def alive_command(client, message: Message):
    await message.reply_text("✅ Bot is Online! 🚀")

@app.on_message(filters.command("ping", prefixes="!") & filters.group)
async def ping_command(client, message: Message):
    start = time.time()
    msg = await message.reply_text("🏓 Pinging...")
    end = time.time()
    ping_time = round((end - start) * 1000)
    await msg.edit_text(f"🏓 Pong!\n⏱️ {ping_time}ms")

#=============== SUDO CHECK ================
def is_sudo(user_id):
    return user_id in sudo_users

#=============== ADD SUDO ================
@app.on_message(filters.command("add", prefixes="!") & filters.group)
async def add_sudo_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can add sudo users!")
        return

    user_id = None
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        try:
            user_id = int(message.command[1])
        except:
            await message.reply_text("❌ Invalid user ID!")
            return

    if user_id:
        sudo_users.add(user_id)
        save_sudo_users()
        user = await client.get_users(user_id)
        await message.reply_text(f"✅ {user.first_name} added as sudo user!")
        await message.delete()

#=============== REMOVE SUDO ================
@app.on_message(filters.command("remove", prefixes="!") & filters.group)
async def remove_sudo_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can remove sudo users!")
        return

    user_id = None
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        try:
            user_id = int(message.command[1])
        except:
            await message.reply_text("❌ Invalid user ID!")
            return

    if user_id and user_id in sudo_users and user_id != OWNER_ID:
        sudo_users.remove(user_id)
        save_sudo_users()
        user = await client.get_users(user_id)
        await message.reply_text(f"✅ {user.first_name} removed from sudo users!")
        await message.delete()

#=============== SUDO LIST ================
@app.on_message(filters.command("sudolist", prefixes="!") & filters.group)
async def sudo_list_command(client, message: Message):
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Only sudo users can use this command!")
        return

    if not sudo_users:
        await message.reply_text("📝 No sudo users found!")
        return

    sudo_list = "👑 **Sudo Users List**\n\n"
    for user_id in sudo_users:
        try:
            user = await client.get_users(user_id)
            sudo_list += f"• {user.first_name}\n ┗ ID: `{user_id}`\n"
        except:
            sudo_list += f"• Unknown User\n ┗ ID: `{user_id}`\n"

    await message.reply_text(sudo_list)

#=============== MESSAGE HANDLER ================
@app.on_message(filters.group)
async def message_handler(client, message: Message):
    try:
        if not message.from_user:
            return

        log_text = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
        log_text += f"User: {message.from_user.first_name} [{message.from_user.id}] | "
        log_text += f"Group: {message.chat.title} | "

        if message.text:
            log_text += f"Text: {message.text[:100]}"
        elif message.sticker:
            log_text += "Sticker sent"

        print(log_text)
    except:
        pass

#=============== SHUTDOWN HANDLER ================
def shutdown_handler():
    print("\n🛑 Shutting down... Saving data...")
    save_all_data()
    print("✅ Data saved! Goodbye!")

#=============== MAIN ================
def main():
    global CUSTOM_LINES
    
    load_all_data()
    
    if OWNER_ID not in sudo_users:
        sudo_users.add(OWNER_ID)
        save_sudo_users()
    
    import atexit
    atexit.register(shutdown_handler)
    
    print("=" * 60)
    print("🚀 BOT STARTED SUCCESSFULLY!")
    print("=" * 60)
    print(f"✅ Data Persistence: ENABLED")
    print(f"👑 Owner ID: {OWNER_ID}")
    print(f"📊 Sudo Users: {len(sudo_users)}")
    print(f"📝 Custom Lines: {len(CUSTOM_LINES)}")
    print(f"⚡ Speed: MAXIMUM")
    print("=" * 60)
    print("💾 All data auto-saves to files!")
    print("🔄 Data survives bot restarts and Render resets!")
    print("=" * 60)

    app.run()

if __name__ == "__main__":
    main()
