import os
import aiohttp
import aiofiles
from ARNAV.thumbnail import generate_thumb
from ARNAV.thumbnail2 import generate_thumbb
from config import MUSIC_BOT_NAME, YOUTUBE_IMG_URL

async def gen_thumb(videoid):
    return await generate_thumb(videoid,MUSIC_BOT_NAME)

async def gen_thumbb(videoid):
    return await generate_thumbb(videoid,MUSIC_BOT_NAME)
