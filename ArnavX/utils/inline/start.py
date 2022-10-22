from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from ArnavX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🙋‍♀️‍️ ʙᴀʙʏ ᴀᴅᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🙋‍♂️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Fᴏᴜɴᴅᴇʀ", user_id=OWNER),
            InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🙋‍♀️‍️ ʙᴀʙʏ ᴀᴅᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🙋",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="Fᴏᴜɴᴅᴇʀ", user_id=OWNER),
            InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=f"{config.UPSTREAM_REPO}"
                )
        ],
     ]
    return buttons
