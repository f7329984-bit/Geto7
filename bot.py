import time
import random
import json
import os
import asyncio
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

#=============== CUSTOM LINES (WILL BE LOADED FROM FILE) ================
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

# =============== DUMMY SERVER FOR RENDER ================
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
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

#=============== DATA ================
sudo_users = {OWNER_ID}
raid_active = {}  # chat_id -> True/False (UNLIMITED RAID)
raid_task = None  # single task reference

#=============== FILE PATHS ================
SUDO_FILE = "sudo_users.json"
LINES_FILE = "custom_lines.json"

#=============== DATA PERSISTENCE ================

def load_all_data():
    global sudo_users, CUSTOM_LINES
    print("\n📂 LOADING SAVED DATA...")
    
    if os.path.exists(SUDO_FILE):
        with open(SUDO_FILE, "r") as f:
            loaded_sudo = json.load(f)
            if loaded_sudo:
                sudo_users = set(loaded_sudo)
                print(f"✅ Loaded {len(sudo_users)} sudo users")
    
    if os.path.exists(LINES_FILE):
        with open(LINES_FILE, "r", encoding='utf-8') as f:
            loaded_lines = json.load(f)
            if loaded_lines:
                CUSTOM_LINES = loaded_lines
                print(f"✅ Loaded {len(CUSTOM_LINES)} custom lines")
    
    print("✅ DATA LOADING COMPLETE!\n")

def save_sudo_users():
    with open(SUDO_FILE, "w") as f:
        json.dump(list(sudo_users), f, indent=2)

def save_custom_lines():
    with open(LINES_FILE, "w", encoding='utf-8') as f:
        json.dump(CUSTOM_LINES, f, indent=2, ensure_ascii=False)

def save_all_data():
    save_sudo_users()
    save_custom_lines()
    print("💾 All data saved!")

#=============== BUTTONS ================
def get_main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me Baby", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [InlineKeyboardButton("🏠 My Home", callback_data="home")],
        [InlineKeyboardButton("👑 My Master", url="https://t.me/ll_SUPRRME_XD_ll")],
        [InlineKeyboardButton("❓ Help", callback_data="help")],
        [InlineKeyboardButton("⚡ Get Sudo", url="https://t.me/ll_SUPRRME_XD_ll")]
    ])

#=============== UNLIMITED RAID LOOP (from first code) ================
async def unlimited_raid_loop(client, chat_id, target_user_id):
    """
    UNLIMITED raid - tab tak chalega jab tak raid_active[chat_id] = False na ho jaye.
    Har LINE ko sequentially bhejta hai, phir dobara shuru se.
    """
    global raid_active
    
    try:
        target_user = await client.get_users(target_user_id)
        mention = target_user.mention
    except:
        mention = f"`{target_user_id}`"
    
    if not CUSTOM_LINES:
        await client.send_message(chat_id, f"❌ No custom lines found! Use `!addline` to add lines first.")
        raid_active[chat_id] = False
        return
    
    await client.send_message(
        chat_id,
        f"╔══════════════════════╗\n"
        f"   ⚔️ **UNLIMITED RAID** ⚔️\n"
        f"╚══════════════════════╝\n\n"
        f"🎯 **Target:** {mention}\n"
        f"📜 **Lines:** `{len(CUSTOM_LINES)}`\n"
        f"⚡ **Mode:** UNLIMITED 🔥\n"
        f"🛑 **Stop:** `!stopr`"
    )
    
    raid_active[chat_id] = True
    
    try:
        while raid_active.get(chat_id, False):
            for line in CUSTOM_LINES:
                if not raid_active.get(chat_id, False):
                    break
                
                # Format line with mention
                if "${USER}" in line:
                    final = line.replace("${USER}", mention)
                else:
                    final = f"{mention} {line}"
                
                try:
                    await client.send_message(chat_id, final)
                except Exception as e:
                    error_str = str(e).lower()
                    if "flood" in error_str or "too many" in error_str or "429" in error_str:
                        await asyncio.sleep(2)
                    elif "bot was blocked" in error_str:
                        raid_active[chat_id] = False
                        break
                    continue
                
                # Ultra fast speed - no delay (0s)
                await asyncio.sleep(0)
    except Exception as e:
        print(f"Raid error: {e}")
    finally:
        raid_active[chat_id] = False

#=============== START COMMAND ================
@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    user = message.from_user
    await message.reply_text(
        f"🔥 Welcome {user.first_name}! 🔥\n\n"
        f"💪 **UNLIMITED RAID BOT**\n\n"
        f"⚡ `.r @user` = Unlimited raid (tab tak chalega jab tak stop na karein)\n"
        f"🛑 `.s` = Raid stop\n\n"
        f"**Data Persistence:** ✅ Enabled\n"
        f"**Lines Saved:** `{len(CUSTOM_LINES)}`\n"
        f"**Sudo Users:** `{len(sudo_users)}`\n\n"
        f"Use buttons below!",
        reply_markup=get_main_keyboard()
    )

#=============== UNLIMITED RAID COMMAND ================
@app.on_message(filters.command(["r", "rr", "rrr"], prefixes="!") & filters.group)
async def unlimited_raid_command(client, message: Message):
    global raid_task
    
    if message.from_user.id not in sudo_users:
        await message.reply_text("❌ Not authorized! Only sudo users can use raid.")
        return
    
    chat_id = message.chat.id
    
    # Check if already active
    if raid_active.get(chat_id, False):
        await message.reply_text("❌ Raid already active in this group! Use `!stopr` first.")
        return
    
    # Get target
    target_user = None
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        await message.reply_text("❌ Reply to a user to start raid!\nUsage: `.r @user` (reply karke)")
        return
    
    if target_user.id == OWNER_ID:
        await message.reply_text("🛡️ Cannot raid the owner!")
        return
    if target_user.id in sudo_users:
        await message.reply_text("🛡️ Cannot raid a sudo user!")
        return
    
    # Delete command message
    try:
        await message.delete()
    except:
        pass
    
    # Start unlimited raid as a background task
    raid_task = asyncio.create_task(
        unlimited_raid_loop(client, chat_id, target_user.id)
    )

#=============== STOP RAID ================
@app.on_message(filters.command("stopr", prefixes="!") & filters.group)
async def stop_raid_command(client, message: Message):
    global raid_active, raid_task
    
    if message.from_user.id not in sudo_users:
        await message.reply_text("❌ Not authorized!")
        return
    
    chat_id = message.chat.id
    
    if not raid_active.get(chat_id, False):
        await message.reply_text("❌ No active raid in this group!")
        return
    
    # Stop the raid
    raid_active[chat_id] = False
    
    try:
        await message.delete()
    except:
        pass
    
    try:
        await client.send_message(
            chat_id,
            f"╔══════════════════════╗\n"
            f"   🛑 **RAID STOPPED** 🛑\n"
            f"╚══════════════════════╝\n\n"
            f"✅ Raid stopped successfully!\n"
            f"⚔️ Ready for next raid!"
        )
    except:
        pass

#=============== ADD CUSTOM LINE ================
@app.on_message(filters.command("addline", prefixes="!") & filters.private)
async def add_line_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can add lines!")
        return
    
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply_text("❌ Usage: !addline <your text line>\n💡 Use `${USER}` for target mention")
        return
    
    new_line = parts[1]
    CUSTOM_LINES.append(new_line)
    save_custom_lines()
    
    await message.reply_text(f"✅ **Line Added!**\n📊 Total Lines: `{len(CUSTOM_LINES)}`\n\n📝 `{new_line[:100]}`")

#=============== VIEW LINES ================
@app.on_message(filters.command("lines", prefixes="!") & filters.private)
async def view_lines_command(client, message: Message):
    if message.from_user.id not in sudo_users:
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
        lines_text += f"\n...and `{len(CUSTOM_LINES)-50}` more lines"
    
    await message.reply_text(lines_text)

#=============== SUDO MANAGEMENT ================
@app.on_message(filters.command("add", prefixes="!") & filters.group)
async def add_sudo_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can add sudo users!")
        return

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        try:
            user_id = int(message.command[1])
        except:
            await message.reply_text("❌ Invalid user ID!")
            return
    else:
        await message.reply_text("❌ Reply to user or provide ID!")
        return

    if user_id == OWNER_ID:
        await message.reply_text("❌ Owner is already sudo!")
        return

    sudo_users.add(user_id)
    save_sudo_users()
    try:
        user = await client.get_users(user_id)
        await message.reply_text(f"✅ {user.first_name} added as sudo user!")
    except:
        await message.reply_text(f"✅ User `{user_id}` added as sudo!")
    await message.delete()

@app.on_message(filters.command("remove", prefixes="!") & filters.group)
async def remove_sudo_command(client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text("❌ Only owner can remove sudo users!")
        return

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        try:
            user_id = int(message.command[1])
        except:
            await message.reply_text("❌ Invalid user ID!")
            return
    else:
        await message.reply_text("❌ Reply to user or provide ID!")
        return

    if user_id in sudo_users and user_id != OWNER_ID:
        sudo_users.remove(user_id)
        save_sudo_users()
        try:
            user = await client.get_users(user_id)
            await message.reply_text(f"✅ {user.first_name} removed from sudo!")
        except:
            await message.reply_text(f"✅ User `{user_id}` removed from sudo!")
        await message.delete()
    else:
        await message.reply_text("❌ User is not a sudo user!")

@app.on_message(filters.command("sudolist", prefixes="!") & filters.group)
async def sudo_list_command(client, message: Message):
    if message.from_user.id not in sudo_users:
        await message.reply_text("❌ Not authorized!")
        return

    if not sudo_users:
        await message.reply_text("📝 No sudo users found!")
        return

    sudo_list = "👑 **Sudo Users List**\n\n"
    for uid in sudo_users:
        try:
            user = await client.get_users(uid)
            sudo_list += f"• {user.first_name}\n ┗ ID: `{uid}`\n"
        except:
            sudo_list += f"• Unknown User\n ┗ ID: `{uid}`\n"

    await message.reply_text(sudo_list)

#=============== ALIVE / PING ================
@app.on_message(filters.command("alive", prefixes="!") & filters.group)
async def alive_command(client, message: Message):
    await message.reply_text(
        f"╔══════════════════════╗\n"
        f"   🔥 **BOT ONLINE** 🔥\n"
        f"╚══════════════════════╝\n\n"
        f"⚡ **Mode:** UNLIMITED RAID\n"
        f"📜 **Lines:** `{len(CUSTOM_LINES)}`\n"
        f"🔑 **Sudo:** `{len(sudo_users)}`\n"
        f"✅ Ready for action!"
    )

@app.on_message(filters.command("ping", prefixes="!") & filters.group)
async def ping_command(client, message: Message):
    start = time.time()
    msg = await message.reply_text("📡 Pinging...")
    end = time.time()
    ping_time = round((end - start) * 1000)
    await msg.edit_text(f"⚡ **PONG!** `{ping_time}ms`\n🚀 **Ultra Fast Mode**")

#=============== CALLBACK HANDLER ================
@app.on_callback_query()
async def button_callback(client, callback_query):
    data = callback_query.data

    if data == "help":
        help_text = f"""
🤖 **BOT COMMANDS** 🤖

⚔️ **RAID (Unlimited):**
• `!r` (reply karein) - Unlimited raid start
• `!stopr` - Raid stop

👑 **Owner (Private):**
• `!addline <text>` - Add raid line
• `!lines` - View all lines

🔐 **Sudo (Owner only):**
• `!add @user` - Add sudo
• `!remove @user` - Remove sudo
• `!sudolist` - List sudo

📊 **Utility:**
• `!alive` - Bot status
• `!ping` - Ping check

📊 **Stats:**
• Lines: {len(CUSTOM_LINES)}
• Sudo: {len(sudo_users)}
"""
        await callback_query.message.edit_text(
            help_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="back")]
            ])
        )

    elif data == "back":
        await callback_query.message.edit_text(
            "🔥 **Welcome Back!** 🔥\n\nData is safely saved!",
            reply_markup=get_main_keyboard()
        )

    elif data == "home":
        await callback_query.message.edit_text(
            f"🏠 **Bot Stats**\n\n"
            f"• Sudo Users: `{len(sudo_users)}`\n"
            f"• Custom Lines: `{len(CUSTOM_LINES)}`\n"
            f"• Status: Active 🟢\n"
            f"• Raid Mode: UNLIMITED 🔥\n\n"
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
    
    if OWNER_ID not in sudo_users:
        sudo_users.add(OWNER_ID)
        save_sudo_users()
    
    print("=" * 60)
    print("🚀 **UNLIMITED RAID BOT STARTED!**")
    print("=" * 60)
    print(f"👑 Owner ID: {OWNER_ID}")
    print(f"📊 Sudo Users: {len(sudo_users)}")
    print(f"📝 Custom Lines: {len(CUSTOM_LINES)}")
    print(f"⚡ Raid Mode: UNLIMITED (stop with !stopr)")
    print("=" * 60)
    print("💾 Data auto-saves on exit!")
    print("=" * 60)

    app.run()
