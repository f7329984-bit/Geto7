import time
import random
import json
import os
import asyncio
import sys
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# =============== FIX FOR EVENT LOOP ================
if sys.version_info[0] == 3 and sys.version_info[1] >= 10:
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

#=============== CONFIG ================
API_ID = 39035274
API_HASH = "6a0b24e16c4bea2bbc975b7dbb0c1e64"
BOT_TOKEN = "8951612687:AAGP6DJYz0VKsD_NZQyz5_DlM6sZHWqoWd8"
OWNER_ID = 8722144519
BOT_USERNAME = "ll_SUPRRME_XD_7_ll_BOT"

#=============== CUSTOM LINES ================
CUSTOM_LINES = [
    "🔥 teri mummy ki chut!",
    "⚡ bahen k lode teri dadi ki black hairy pussy",
    "🚀 teri mummy ko ulta ltkakr taangduga aur uski chut maruga!",
    "✨ bsdk teri mummy teri dadi sb randi ki bachi h",
    # ========== DIRECT ABUSE LINES ==========
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
    "teri mummy ki chut madarchodo hizda hai hai tum madarchodo bol de yuta tera baap hai warna teri ki chut koi ramdi ki aulad nhi bacha payega aaj samjh le madrchod",
    "air jorden ke jute se teri ki chut pr maar maar ke laal kr dunga kali se laal 😋🥵 randi madarchodo",
    "madarchodo baap se ladega apne teri ma ki chut kha jaunga ramdi",
    "teri maa ki chhut ka khaa jaunga madarchodo randi ki aulad spam karta hai madarcod ke chakke ki aulad tere baap ko gadhe ke land see chodunga",
    "teri maki chut madarchod sur ke land se ma chodunga gandi chut ki kali aulad fati kali chut ki auld chamr teri maiya ki chut ko chor bazr me bechunga madrachod",
    "teri maiya ke ki chut me apne land ka python bot bana kr run krunga teri sasti spam user bot ka bhosda madarchodo",
    "teri maiya ka bhosda madarchodo sasti gb raod ki randi ki aulad",
    "fati kali chut ki auld chamr teri maiya ki chut ko chor bazr me bechunga madrachod",
    "teri makichut ko kutto ko khila dunga randi ki saststi aulad madarchodo",
    "teri mummy ki chut bsdk 🖕",
    
    # ========== PARAGRAPH EXTENDED ABUSE ==========
    "sun bhsdike, tu apni ma ki chut me pani bhar ke aa rha hai kya? teri maki chut ka anguthi ke barabar bhi koi value nahi hai, madarchod kahin ka. teri behen ki chut ka chakkar mein tera baap bhi kuch nahi kar payega. teri gaand me 4 golyan mar ke tumhe bhagwa chola pehna dunga. randi ki aulad, teri maiya ne to mujhe bolaya tha ke ${USER} ko rok ke rakh, lekin teri ma ki chut mein to puro poori jeej ka dungi!",
    "madarchod! teri maiya ne to mujhe bataya ki tu abhi tak bachon wali nikkar pehenta hai. teri behen to meri randi hai aur teri maa meri rakhal. tere baap ko malum hai to bhi kuch nahi kar sakta. teri maki chut me mera lund itna deep gaya ki teri dadi ki bhi yaad aa gayi. aag laga dunga teri family me, tere saare khandan ki gaand marunga. tu to bas ek khaali aluminium ka tube hai, jisme kuch nahi bachega!",
    "bahen ke lode! tujhe lagta hai tu bohot bada aaya hai? teri maiya to meri chodi hui malkin hai. teri behen ka muh mera lund se bhara hua tha jab tu tv dekh rha tha. teri maa ki chut me to 5 goliyan, 4 ungliyan aur 2 penetration ho chuki hain. tu kya bosdina kare ga? teri shakal pe thappar marunga to tu ro dega, madarchod.",
    "teri maiya ki chut me mera lund itna zor se ghoosta hai jaise stadium ke flood lights chal rahi ho. teri behen to itni suali hai ki uski chut me dandiyaan daalni padti hain. madarchod kahin ka, tu to bas ek chhotu sa bosdina hai. tera baap bhi meri presence me ghutno ke bal aata hai.",
    "randi ki aulad! teri maiya to meri aafat hai aur tu mera fan. teri maa ki chut me to bohot zyada traffic hai, ek to main aur ek tere baap ka dosra beta. tu kuch bhi nahi hai bosdina. main teri behen ki chut me ek dam paver blocker launch kar dunga aur teri maiya ko tere saamne sabke saamne chodunga.",
    "chutiya tu maa chudane aaya hai? teri maiya to meri randi list me highest rated hai. teri behen to itni raandi hai ki uski chut me paytm se payment karta hu main. tera baap to sirf camera dekhne ka kaam karta hai jab main teri maa chodta hu.",
    "teri maa ki chut me mera lund bsdk 🍆💦",
    "teri gaand phat gayi kya bhag kya rha hai 🏃💨",
    "teri maa ne mujhe bolya ko ghas mat khila 💀",
    "teri maa ki chut ka kera hai tu 🤡",
    
    # ========== BEHEN (SISTER) ABUSE LINES ==========
    "teri behen ko dekh ke mera lund khara ho gya 😏",
    "tu apni maa ka dudh peena band kar de 🍼",
    "teri behen ki chut me 5 bihari ek saath 🥵",
    "teri shakal dekh ke mera lund murjha gya 🥀",
    "teri behen to meri ex hai ab teri maa meri current hai 😎",
    "tera baap bhi randi ki aulad hai sale 🚮",
    "teri maa ki chut me parking lot 🅿️",
    "teri behen ki chut me wifi chalta hai 📶",
    "teri behen to meri favorite randi hai 💋",
    "teri maa ki chut me cloud storage ☁️",
    "teri behen ki chut me bluetooth connect 📱",
    "teri maa ki chut ka subscriber hu mai 🔔",
    "teri maa ko chod ke thak gya hu 💦",
    "teri behen ka onlyfans top donation mai hu 👑",
    "teri behen ko chodta hu to aawaz aati hai oye haye 🎵",
    "teri behen ki chut ka rent 500 hai 💵",
    "teri behen ko dekh ke mera lund bolta hai aaja 🗣️",
    "teri behen ka virginity maine li thi 🏆",
    "teri behen ke muh me mera lund 💯",
    "teri behen ko randi bana ke chodta hu 🎯",
    "teri behen to meri sugarmammy hai 🍭",
    "teri behen ke muh ka swad chang hai 👅",
    "teri behen ko randi banane ka master hu mai 🧠",
    "teri behen ki chut ka toll free number 📞",
    "teri behen ki chut ka pin 7860 📌",
    "teri behen ki chut ka rate list 💲",
    "teri behen ki chut ka catalog 📚",
    "teri behen ki chut ka location 📍",
    "teri behen ki chut ka color black 🖤",
    "teri behen ki chut ka stock available 📦",
    "teri behen ki chut ka offer zone 🏷️",
    "teri behen ki chut ki quality aaa ✅",
    "teri behen ki chut ka track record 🏅",
    "teri maa ki chut teri behen ka bhosda 🖕",
    "madarchod teri aukaat nahi hai bhaag yahan se 🤬",
    "bhadwe teri maa ki chut itna attitude kahan se laata hai 🖕",
    "itni shakal buri ki aaina bhi tod de 🔥",
    "teri photo dekh ke darwaza chod de itna ugly hai tu 🤣",
    "main aag hoon jo jalati hai aur raakh mein bhi chamakti hai 🔥",
    "meri aukaat nahi meri shaan hai 👑",
    "madarchod teri aukaat nahi hai bhaag yahan se 🤬",
    "teri shaadi kab hai? maa ne kaha ghar par rakh legi 😂",
    "tu itna smart hai ki duniya ko laga tera baap ka paisa hai 🤣",
    
    # ========== UNICODE FORMAL LINES (TERI MAA) ==========
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑵𝑭𝑻 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERI BEHEN) ==========
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERE BAAP) ==========
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERI FAMILY) ==========
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERE KUTTE) ==========
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERI AUKAAT) ==========
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERI MUMMY) ==========
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== UNICODE (TERE DADA) ==========
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    
    # ========== PUNISHMENT LINES (UNAUTHORIZED USERS) ==========
    "TERI MAKI CHUT ${USER} RANDI ITACHI PAPA BOL KE THODI AUKAT BANA LE PHIR BOT SE CHUDWANA AAKE 😋🥵",
    "MADARCHOD ${USER} TERI AUKAAT NAHI HAI BOT USE KARNE KI TERI MAIYA KI CHUT ME MERA LUND 🍆💦",
    "${USER} RANDI KI AULAD BOT KA USE KARE GA TERI MAKI CHUT ME TALWAR GHUSAAUNGA 🔥",
    "BHOSDIKE ${USER} TERI BEHEN KI CHUT ME BOT DAAL DUNGA TERI AUKAAT PEHLE BANA 🖕",
    "${USER} CHUTIYE TU KAUN HOTA HAI BOT USE KARNE WALA TERI MAIYA NE BOL DIYA TERA BAAP BHI NAHI HAI 🤡",
    "TERI MAKI CHUT ${USER} MADARCHOD PEHLE SUDO LE PHIR AA NAHI TO TERI GAAND MARUNGA 💀",

]

# =============== WEB SERVER FOR RENDER ================
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = "<h1>ULTRA FAST RAID BOT</h1><p>Status: ONLINE</p><p>Speed: 100x</p><p>Multi-Raid Support</p>"
        self.wfile.write(html.encode('utf-8'))
    def log_message(self, format, *args):
        pass

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

app = Client("ultra_fast_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

#=============== DATA ================
sudo_users = set()
raid_active = {}  # chat_id_target_id -> True/False (supports multiple raids per group)
raid_tasks = {}   # track raid tasks
raid_count = {}   # track messages sent

#=============== FILE PATHS ================
SUDO_FILE = "sudo_users.json"
LINES_FILE = "custom_lines.json"

#=============== DATA PERSISTENCE ================
def load_all_data():
    global sudo_users, CUSTOM_LINES
    print("\n📂 LOADING SAVED DATA...")
    
    if os.path.exists(SUDO_FILE):
        try:
            with open(SUDO_FILE, "r") as f:
                loaded_sudo = json.load(f)
                if loaded_sudo and isinstance(loaded_sudo, list):
                    sudo_users = set(loaded_sudo)
                    print(f"✅ Loaded {len(sudo_users)} sudo users")
                else:
                    sudo_users = {OWNER_ID}
        except Exception as e:
            print(f"⚠️ Error loading sudo users: {e}")
            sudo_users = {OWNER_ID}
    else:
        sudo_users = {OWNER_ID}
        save_sudo_users()
    
    if os.path.exists(LINES_FILE):
        try:
            with open(LINES_FILE, "r", encoding='utf-8') as f:
                loaded_lines = json.load(f)
                if loaded_lines and isinstance(loaded_lines, list):
                    CUSTOM_LINES = loaded_lines
                    print(f"✅ Loaded {len(CUSTOM_LINES)} custom lines")
        except Exception as e:
            print(f"⚠️ Error loading lines: {e}")
    
    print(f"👑 Owner ID: {OWNER_ID}")
    print(f"🔑 Sudo Users: {list(sudo_users)}")
    print("✅ DATA LOADING COMPLETE!\n")

def save_sudo_users():
    try:
        with open(SUDO_FILE, "w") as f:
            json.dump(list(sudo_users), f, indent=2)
        print(f"💾 Saved {len(sudo_users)} sudo users")
    except Exception as e:
        print(f"❌ Error saving sudo users: {e}")

def save_custom_lines():
    try:
        with open(LINES_FILE, "w", encoding='utf-8') as f:
            json.dump(CUSTOM_LINES, f, indent=2, ensure_ascii=False)
        print(f"💾 Saved {len(CUSTOM_LINES)} custom lines")
    except Exception as e:
        print(f"❌ Error saving lines: {e}")

def save_all_data():
    save_sudo_users()
    save_custom_lines()

#=============== CHECK SUDO ================
def is_sudo(user_id):
    if user_id == OWNER_ID:
        return True
    return user_id in sudo_users

#=============== BUTTONS ================
def get_main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me Baby", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("🏠 My Home", callback_data="home")],
        [InlineKeyboardButton("👑 My Master", url="https://t.me/ll_SUPRRME_XD_ll")],
        [InlineKeyboardButton("❓ Help", callback_data="help")],
        [InlineKeyboardButton("⚡ Get Sudo", url="https://t.me/ll_SUPRRME_XD_ll")]
    ])

#=============== GET CLICKABLE MENTION ================
async def get_clickable_mention(client, user_input, message):
    if message.reply_to_message:
        target = message.reply_to_message.from_user
        return target.mention, target.id, target.first_name
    
    if user_input and user_input.startswith("@"):
        try:
            target = await client.get_users(user_input)
            return target.mention, target.id, target.first_name
        except:
            return user_input, None, None
    
    if user_input and user_input.isdigit():
        try:
            target = await client.get_users(int(user_input))
            return target.mention, target.id, target.first_name
        except:
            return f"`{user_input}`", None, None
    
    return None, None, None

#=============== RAID LOOP (SUPPORTS LIMITED + UNLIMITED) ================
async def raid_loop(client, chat_id, target_user_id, target_mention, target_name, raid_id, count):
    """
    raid_id: unique identifier for this raid (chat_id_target_id)
    count: -1 = unlimited, >0 = limited messages
    """
    global raid_active, raid_count
    
    raid_active[raid_id] = True
    sent = 0
    
    if not CUSTOM_LINES:
        await client.send_message(chat_id, f"❌ No custom lines found! Use `!addline` to add lines first.")
        raid_active[raid_id] = False
        return
    
    # Determine raid type
    if count == -1:
        raid_type = "UNLIMITED"
        stop_cmd = "!stopr"
    else:
        raid_type = f"LIMITED ({count} messages)"
        stop_cmd = "!stopr"
    
    # Start message
    await client.send_message(
        chat_id,
        f"╔══════════════════════════════════╗\n"
        f"   ⚡ **RAID STARTED** ⚡\n"
        f"╚══════════════════════════════════╝\n\n"
        f"🎯 **Target:** {target_mention}\n"
        f"👤 **Name:** {target_name}\n"
        f"📜 **Lines:** `{len(CUSTOM_LINES)}`\n"
        f"⚡ **Speed:** 100x ULTRA FAST\n"
        f"♾️ **Mode:** {raid_type}\n"
        f"🛑 **Stop:** `{stop_cmd}`\n\n"
        f"✅ **RAID STARTED!**"
    )
    
    try:
        if count == -1:  # UNLIMITED MODE
            while raid_active.get(raid_id, False):
                for line in CUSTOM_LINES:
                    if not raid_active.get(raid_id, False):
                        break
                    
                    if "${USER}" in line:
                        final = line.replace("${USER}", target_mention)
                    else:
                        final = f"{target_mention} {line}"
                    
                    try:
                        await client.send_message(chat_id, final)
                        sent += 1
                        
                        if sent % 200 == 0:
                            await client.send_message(
                                chat_id,
                                f"📊 **Progress**\n📨 Sent: `{sent}`\n🎯 {target_mention}"
                            )
                    except Exception as e:
                        error_str = str(e).lower()
                        if "flood" in error_str or "429" in error_str:
                            await asyncio.sleep(1)
                        elif "bot was blocked" in error_str:
                            raid_active[raid_id] = False
                            break
                        continue
                    
                    await asyncio.sleep(0)
        
        else:  # LIMITED MODE
            status_msg = await client.send_message(
                chat_id,
                f"⏳ **Raiding {target_name}**\n📨 Target: `{count}` messages\n⚡ Speed: 100x"
            )
            
            for i in range(count):
                if not raid_active.get(raid_id, False):
                    break
                
                for line in CUSTOM_LINES:
                    if not raid_active.get(raid_id, False) or sent >= count:
                        break
                    
                    if sent >= count:
                        break
                    
                    if "${USER}" in line:
                        final = line.replace("${USER}", target_mention)
                    else:
                        final = f"{target_mention} {line}"
                    
                    try:
                        await client.send_message(chat_id, final)
                        sent += 1
                    except:
                        pass
                    
                    await asyncio.sleep(0)
            
            await status_msg.edit_text(
                f"✅ **RAID COMPLETE**\n"
                f"📨 Sent: `{sent}/{count}`\n"
                f"🎯 {target_mention}"
            )
            
    except Exception as e:
        print(f"Raid error: {e}")
    finally:
        raid_active[raid_id] = False
        raid_count[raid_id] = sent
        
        # Only send completion message for unlimited raids
        if count == -1:
            await client.send_message(
                chat_id,
                f"🛑 **RAID STOPPED**\n📊 Total: `{sent}` messages\n🎯 {target_mention}"
            )

#=============== UNLIMITED RAID (!r) ================
@app.on_message(filters.command(["r"], prefixes="!") & filters.group)
async def unlimited_raid_command(client, message: Message):
    if not is_sudo(message.from_user.id):
        await message.reply_text(f"❌ Not authorized! Only sudo users can use raid.\n👑 Owner: `{OWNER_ID}`")
        return
    
    target_user = None
    
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        parts = message.text.split()
        for part in parts:
            if part.startswith("@"):
                try:
                    target_user = await client.get_users(part)
                    break
                except:
                    pass
        
        if not target_user and len(parts) > 1:
            try:
                target_user = await client.get_users(parts[1])
            except:
                pass
    
    if not target_user:
        await message.reply_text(
            "❌ **Usage:** `!r @username` (unlimited)\n"
            "• Reply to user → `!r`\n"
            "• Tag user → `!r @username`\n\n"
            "📌 **Limited Raid:** `!tr @username 100`\n"
            "🛑 **Stop:** `!stopr`"
        )
        return
    
    if target_user.id == OWNER_ID:
        await message.reply_text("🛡️ Cannot raid the owner!")
        return
    
    if is_sudo(target_user.id):
        await message.reply_text("🛡️ Cannot raid a sudo user!")
        return
    
    chat_id = message.chat.id
    raid_id = f"{chat_id}_{target_user.id}"
    
    if raid_active.get(raid_id, False):
        await message.reply_text(f"❌ Already raiding {target_user.first_name}!\n📨 Sent: {raid_count.get(raid_id, 0)} messages\n🛑 Use `!stopr` to stop first.")
        return
    
    try:
        await message.delete()
    except:
        pass
    
    mention = target_user.mention
    name = target_user.first_name
    
    task = asyncio.create_task(raid_loop(client, chat_id, target_user.id, mention, name, raid_id, -1))
    raid_tasks[raid_id] = task

#=============== LIMITED RAID (!tr) ================
@app.on_message(filters.command(["tr"], prefixes="!") & filters.group)
async def limited_raid_command(client, message: Message):
    if not is_sudo(message.from_user.id):
        await message.reply_text(f"❌ Not authorized! Only sudo users can use raid.")
        return
    
    parts = message.text.split()
    
    if len(parts) < 2:
        await message.reply_text(
            "❌ **Usage:** `!tr @username count message`\n\n"
            "Examples:\n"
            "• `!tr @user 100`\n"
            "• `!tr @user 500`\n"
            "• Reply to user → `!tr 100`\n\n"
            "📌 **Unlimited:** `!r @username`"
        )
        return
    
    target_user = None
    count = None
    
    # Parse target and count
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
        if len(parts) > 1:
            try:
                count = int(parts[1])
            except:
                await message.reply_text("❌ Invalid count! Example: `!tr 100`")
                return
    else:
        # Find target (@username)
        for part in parts:
            if part.startswith("@"):
                try:
                    target_user = await client.get_users(part)
                    break
                except:
                    pass
        
        if not target_user and len(parts) > 1:
            try:
                target_user = await client.get_users(parts[1])
            except:
                pass
        
        # Find count
        for part in parts:
            if part.isdigit():
                count = int(part)
                break
    
    if not target_user:
        await message.reply_text("❌ No target found! Tag a user or reply to their message.")
        return
    
    if not count:
        await message.reply_text("❌ No count found! Example: `!tr @username 100`")
        return
    
    if count < 1:
        await message.reply_text("❌ Count must be at least 1!")
        return
    
    if count > 10000:
        await message.reply_text("❌ Maximum count is 10000!")
        return
    
    if target_user.id == OWNER_ID:
        await message.reply_text("🛡️ Cannot raid the owner!")
        return
    
    if is_sudo(target_user.id):
        await message.reply_text("🛡️ Cannot raid a sudo user!")
        return
    
    chat_id = message.chat.id
    raid_id = f"{chat_id}_{target_user.id}"
    
    if raid_active.get(raid_id, False):
        await message.reply_text(f"❌ Already raiding {target_user.first_name}!\n🛑 Use `!stopr` first.")
        return
    
    try:
        await message.delete()
    except:
        pass
    
    mention = target_user.mention
    name = target_user.first_name
    
    task = asyncio.create_task(raid_loop(client, chat_id, target_user.id, mention, name, raid_id, count))
    raid_tasks[raid_id] = task

#=============== STOP RAID ================
@app.on_message(filters.command("stopr", prefixes="!") & filters.group)
async def stop_raid_command(client, message: Message):
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Not authorized!")
        return
    
    chat_id = message.chat.id
    
    # Find all active raids in this group
    stopped_raids = []
    for raid_id, active in raid_active.items():
        if raid_id.startswith(f"{chat_id}_") and active:
            raid_active[raid_id] = False
            target_id = raid_id.split("_")[1]
            stopped_raids.append(target_id)
    
    if not stopped_raids:
        await message.reply_text("❌ No active raid in this group!")
        return
    
    try:
        await message.delete()
    except:
        pass
    
    await client.send_message(
        chat_id,
        f"🛑 **RAID STOPPED**\n"
        f"📊 Stopped: `{len(stopped_raids)}` raid(s)"
    )

#=============== STOP ALL RAIDS (Owner only) ================
@app.on_message(filters.command("stopall", prefixes="!") & filters.private)
async def stop_all_raids(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner!")
        return
    
    count = 0
    for raid_id in list(raid_active.keys()):
        if raid_active.get(raid_id, False):
            raid_active[raid_id] = False
            count += 1
    
    await message.reply_text(f"🛑 **Stopped {count} raid(s) globally**")

#=============== RAID STATUS ================
@app.on_message(filters.command("raidstatus", prefixes="!") & filters.group)
async def raid_status_command(client, message: Message):
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Not authorized!")
        return
    
    chat_id = message.chat.id
    active_raids = []
    
    for raid_id, active in raid_active.items():
        if raid_id.startswith(f"{chat_id}_") and active:
            target_id = raid_id.split("_")[1]
            sent = raid_count.get(raid_id, 0)
            try:
                user = await client.get_users(int(target_id))
                active_raids.append(f"• {user.mention} - {sent} msgs")
            except:
                active_raids.append(f"• `{target_id}` - {sent} msgs")
    
    if not active_raids:
        await message.reply_text("📊 **No active raids in this group**")
    else:
        status_text = f"📊 **ACTIVE RAIDS**\n\n" + "\n".join(active_raids)
        await message.reply_text(status_text)

#=============== ADD LINE ================
@app.on_message(filters.command("addline", prefixes="!") & filters.private)
async def add_line_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can add lines!")
        return
    
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply_text("❌ Usage: `!addline <text>`\n💡 Use `${USER}` for target mention")
        return
    
    new_line = parts[1]
    CUSTOM_LINES.append(new_line)
    save_custom_lines()
    
    await message.reply_text(f"✅ **Line Added!**\n📊 Total: `{len(CUSTOM_LINES)}`\n\n📝 `{new_line[:100]}`")

#=============== VIEW LINES ================
@app.on_message(filters.command("lines", prefixes="!") & filters.private)
async def view_lines_command(client, message: Message):
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Not authorized!")
        return
    
    if not CUSTOM_LINES:
        await message.reply_text("📝 No custom lines found!\nUse `!addline` to add.")
        return
    
    lines_text = f"📝 **Custom Lines (Total: {len(CUSTOM_LINES)})**\n\n"
    for i, line in enumerate(CUSTOM_LINES[:50], 1):
        display = line[:80] + "..." if len(line) > 80 else line
        lines_text += f"`{i}.` {display}\n"
    
    if len(CUSTOM_LINES) > 50:
        lines_text += f"\n...and `{len(CUSTOM_LINES)-50}` more"
    
    await message.reply_text(lines_text)

#=============== DELETE LINES ================
@app.on_message(filters.command("dellines", prefixes="!") & filters.private)
async def delete_lines_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner!")
        return
    
    count = len(CUSTOM_LINES)
    CUSTOM_LINES.clear()
    save_custom_lines()
    await message.reply_text(f"🗑️ Deleted all `{count}` lines!")

#=============== SUDO MANAGEMENT ================
@app.on_message(filters.command("add", prefixes="!") & filters.group)
async def add_sudo_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text(f"❌ Only owner can add sudo users!")
        return

    target_user = None
    
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        parts = message.text.split()
        for part in parts:
            if part.startswith("@"):
                try:
                    target_user = await client.get_users(part)
                    break
                except:
                    pass
        
        if not target_user and len(parts) > 1:
            try:
                user_id = int(parts[1])
                target_user = await client.get_users(user_id)
            except:
                pass
    
    if not target_user:
        await message.reply_text("❌ Reply to user or tag them!\nUsage: `!add @username`")
        return

    user_id = target_user.id
    user_name = target_user.first_name

    if user_id == OWNER_ID:
        await message.reply_text("❌ Owner is already sudo!")
        return

    if user_id in sudo_users:
        await message.reply_text(f"❌ {user_name} is already sudo!")
        return

    sudo_users.add(user_id)
    save_sudo_users()
    
    await message.reply_text(f"✅ **{user_name} added as sudo user!**")
    
    try:
        await message.delete()
    except:
        pass

@app.on_message(filters.command("remove", prefixes="!") & filters.group)
async def remove_sudo_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can remove sudo users!")
        return

    target_user = None
    
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        parts = message.text.split()
        for part in parts:
            if part.startswith("@"):
                try:
                    target_user = await client.get_users(part)
                    break
                except:
                    pass
        
        if not target_user and len(parts) > 1:
            try:
                user_id = int(parts[1])
                target_user = await client.get_users(user_id)
            except:
                pass
    
    if not target_user:
        await message.reply_text("❌ Reply to user or tag them!\nUsage: `!remove @username`")
        return

    user_id = target_user.id
    user_name = target_user.first_name

    if user_id == OWNER_ID:
        await message.reply_text("❌ Cannot remove owner!")
        return

    if user_id not in sudo_users:
        await message.reply_text(f"❌ {user_name} is not sudo!")
        return

    sudo_users.remove(user_id)
    save_sudo_users()
    
    await message.reply_text(f"✅ **{user_name} removed from sudo!**")
    
    try:
        await message.delete()
    except:
        pass

@app.on_message(filters.command("sudolist", prefixes="!") & filters.group)
async def sudo_list_command(client, message: Message):
    if not is_sudo(message.from_user.id):
        await message.reply_text("❌ Not authorized!")
        return

    if not sudo_users:
        await message.reply_text("📝 No sudo users found!")
        return

    sudo_list = "👑 **SUDO USERS**\n\n"
    for uid in list(sudo_users):
        try:
            user = await client.get_users(uid)
            sudo_list += f"• {user.mention}\n  ┗ ID: `{uid}`\n"
        except:
            sudo_list += f"• Unknown\n  ┗ ID: `{uid}`\n"
    
    sudo_list += f"\n👑 Owner: `{OWNER_ID}`"
    
    await message.reply_text(sudo_list)

#=============== ALIVE ================
@app.on_message(filters.command("alive", prefixes="!") & filters.group)
async def alive_command(client, message: Message):
    chat_id = message.chat.id
    active_count = 0
    for raid_id, active in raid_active.items():
        if raid_id.startswith(f"{chat_id}_") and active:
            active_count += 1
    
    await message.reply_text(
        f"╔══════════════════════╗\n"
        f"   🔥 **BOT ONLINE** 🔥\n"
        f"╚══════════════════════╝\n\n"
        f"⚡ **Speed:** 100x ULTRA FAST\n"
        f"📜 **Lines:** `{len(CUSTOM_LINES)}`\n"
        f"🔑 **Sudo:** `{len(sudo_users)}`\n"
        f"🎯 **Active Raids:** `{active_count}`\n"
        f"👑 **Owner:** `{OWNER_ID}`"
    )

#=============== PING ================
@app.on_message(filters.command("ping", prefixes="!") & filters.group)
async def ping_command(client, message: Message):
    start = time.time()
    msg = await message.reply_text("📡 Pinging...")
    end = time.time()
    ping_time = round((end - start) * 1000)
    await msg.edit_text(f"⚡ **PONG!** `{ping_time}ms`\n🚀 **100x ULTRA FAST**")

#=============== HELP ================
@app.on_message(filters.command("help", prefixes="!"))
async def help_command(client, message: Message):
    await message.reply_text(
        f"🤖 **RAID BOT COMMANDS**\n\n"
        f"⚔️ **RAID:**\n"
        f"• `!r @user` - Unlimited raid\n"
        f"• `!tr @user 100` - Limited raid (100 times)\n"
        f"• `!stopr` - Stop raid\n"
        f"• `!raidstatus` - Check active raids\n\n"
        f"👑 **OWNER:**\n"
        f"• `!addline text` - Add line\n"
        f"• `!lines` - View lines\n"
        f"• `!dellines` - Delete lines\n\n"
        f"🔐 **SUDO:**\n"
        f"• `!add @user` - Add sudo\n"
        f"• `!remove @user` - Remove sudo\n"
        f"• `!sudolist` - List sudo\n\n"
        f"📊 **INFO:**\n"
        f"• `!alive` - Status\n"
        f"• `!ping` - Speed"
    )

#=============== CALLBACK ================
@app.on_callback_query()
async def button_callback(client, callback_query):
    data = callback_query.data

    if data == "help":
        await callback_query.message.edit_text(
            f"🤖 **ULTRA FAST RAID BOT**\n\n"
            f"⚔️ `!r @user` - Unlimited\n"
            f"⚔️ `!tr @user 100` - Limited\n"
            f"🛑 `!stopr` - Stop\n"
            f"📊 `!raidstatus` - Status\n\n"
            f"Speed: 100x ULTRA FAST\n"
            f"Multi-Raid: YES",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )
    elif data == "back":
        await callback_query.message.edit_text(
            "🔥 **ULTRA FAST RAID BOT** 🔥\n\n100x Speed | Multi-Raid | Unlimited",
            reply_markup=get_main_keyboard()
        )
    elif data == "home":
        await callback_query.message.edit_text(
            f"🏠 **Bot Stats**\n\n"
            f"• Sudo: `{len(sudo_users)}`\n"
            f"• Lines: `{len(CUSTOM_LINES)}`\n"
            f"• Speed: 100x\n"
            f"• Multi-Raid: ✅\n\n"
            f"👑 Owner: `{OWNER_ID}`",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )
    await callback_query.answer()

#=============== SHUTDOWN ================
import atexit
atexit.register(save_all_data)

#=============== MAIN ================
if __name__ == "__main__":
    load_all_data()
    
    print("=" * 60)
    print("⚡ **ULTRA FAST RAID BOT (100x SPEED)** ⚡")
    print("=" * 60)
    print(f"👑 Owner ID: {OWNER_ID}")
    print(f"🔑 Sudo Users: {len(sudo_users)}")
    print(f"📝 Custom Lines: {len(CUSTOM_LINES)}")
    print(f"⚡ Speed: 100x ULTRA FAST")
    print(f"🔄 Multi-Raid: ✅ Supported")
    print("=" * 60)
    print("✅ Commands: !r | !tr | !stopr | !raidstatus")
    print("=" * 60)

    app.run()
