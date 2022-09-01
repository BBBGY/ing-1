## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCDMGJkLEVGAEoFz3HZxYvncrLw8m4fu1bEvB3apK66uHjKfcN4XbvoFClAUykh-8a4caFeCdsExZDpaGcX9Wa-Tft7Ie-rbL7VWVHrwCP8SsPM67xjuBkuAMyweYn9g0ecy6ws8LFd5wFLrhdNsB9oUvIu3Sk8ARKkjWAwbrrQdgi3q5-3WCLtYJXIWuxDBEfIthsyvoHqzoW5NpEbinraxsdZ0tM0P26T2ZlFoppGGr4mCdem-XzF_bRE5r_ZgL9vb7yhHArIBqO2_lsje_T1v6Fb5MKNPisj73erjnLm70Rzhiev05V5ZjEYqT38raMeD_wpmat2rflAxBVmYNP2AAAAAUtaURkA")
BOT_TOKEN = getenv("BOT_TOKEN", "5415541897:AAEFptVUtB2lhX3mUVOiAjecukrR4E7EjIo")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Ahmed")
OWNER_USERNAME = getenv("OWNER_USERNAME", "R7ZRR")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "RRR8IBOT")
OWNER_ID = getenv("OWNER_ID", "5284259786")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "QIINT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "L6L6P")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "L6L6P")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/b306e5c7ba357b7faf0d3.mp4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
