import random
from typing import Union

from pyrogram import enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PritiMusic import app

STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER
]

def help_pannel(_, START: Union[bool, int] = None):
    alone_style = random.choice(STYLES)
    remaining_styles = [s for s in STYLES if s != alone_style]
    group_style = random.choice(remaining_styles)
    
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],  # Fixed typo: was H_B_2
                    callback_data="help_callback hb1",
                    style=group_style,
                    icon_custom_emoji_id=5456140674028019486
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                    style=group_style,
                    icon_custom_emoji_id=5463107823946717464
                ),
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="help_callback hb3",
                    style=group_style,
                    icon_custom_emoji_id=5377754411319698237
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="help_callback hb4",
                    style=group_style,
                    icon_custom_emoji_id=5402186569006210455
                ),
                InlineKeyboardButton(
                    text=_["H_B_5"],
                    callback_data="help_callback hb5",
                    style=group_style,
                    icon_custom_emoji_id=5251203410396458957
                ),
                InlineKeyboardButton(
                    text=_["H_B_6"],
                    callback_data="help_callback hb6",
                    style=group_style,
                    icon_custom_emoji_id=5240241223632954241
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_7"],
                    callback_data="help_callback hb7",
                    style=group_style,
                    icon_custom_emoji_id=5260293700088511294
                ),
                InlineKeyboardButton(
                    text=_["H_B_8"],
                    callback_data="help_callback hb8",
                    style=group_style,
                    icon_custom_emoji_id=5424818078833715060
                ),
                InlineKeyboardButton(
                    text=_["H_B_9"],
                    callback_data="help_callback hb9",
                    style=group_style,
                    icon_custom_emoji_id=5282843764451195532
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="settingsback_helper",
                    style=alone_style,
                    icon_custom_emoji_id=6084861780935315826
                ),
            ],
        ]
    )
    return upl


def help_back_markup(_):
    alone_style = random.choice(STYLES)
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"], 
                    callback_data="settings_back_helper", 
                    style=alone_style,
                    icon_custom_emoji_id=6084861780935315826
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    alone_style = random.choice(STYLES)
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"], 
                url=f"https://t.me/{app.username}?start=help", 
                style=alone_style,
                icon_custom_emoji_id=5341715473882955310
            )
        ]
    ]
    return buttons
