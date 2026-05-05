import random
from pyrogram import enums
from pyrogram.types import InlineKeyboardButton
import config
from PritiMusic import app

STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER
]

def start_panel(_):
    group_style = random.choice(STYLES)
    
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=group_style,
                icon_custom_emoji_id=5445284980978621387
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                style=group_style,
                icon_custom_emoji_id=5395732581780040886
            ),
        ],
    ]
    return buttons

def private_panel(_):
    alone_style = random.choice(STYLES)
    remaining_styles = [s for s in STYLES if s != alone_style]
    group_style = random.choice(remaining_styles)

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=alone_style,
                icon_custom_emoji_id=5445284980978621387
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", 
                user_id=config.OWNER_ID, 
                style=group_style,
                icon_custom_emoji_id=6102845947170005182
            ),
            InlineKeyboardButton(
                text="ɪɴғᴏ",
                callback_data="api_status",
                style=group_style,
                icon_custom_emoji_id=6291913431196902384
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"], 
                callback_data="shiv_Lucky", 
                style=group_style,
                icon_custom_emoji_id=5395732581780040886
            ),
            InlineKeyboardButton(
                text="sᴏᴜʀᴄᴇ", 
                callback_data="gib_source", 
                style=group_style,
                icon_custom_emoji_id=5440621591387980068
            ),
        ],        
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
                style=alone_style,
                icon_custom_emoji_id=5341715473882955310
            ),
        ],
    ]
    return buttons
