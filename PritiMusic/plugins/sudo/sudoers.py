from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from PritiMusic import app
from PritiMusic.misc import SUDOERS
from PritiMusic.utils.database import add_sudo, remove_sudo
from PritiMusic.utils.decorators.language import language
from PritiMusic.utils.extraction import extract_user
from PritiMusic.utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID

@app.on_message(filters.command(["addsudo"], prefixes=["/", "!", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text(_["general_1"])

    user = await extract_user(message)

    if user.id in SUDOERS:
        return await message.reply_text(_["sudo_1"].format(user.mention))

    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])

@app.on_message(filters.command(["delsudo", "rmsudo"], prefixes=["/", "!", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text(_["general_1"])

    user = await extract_user(message)

    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))

    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])

@app.on_message(filters.command(["sudolist", "listsudo", "sudoers"]) & ~BANNED_USERS)
async def sudoers_list(client, message: Message):
    keyboard = [
        [InlineKeyboardButton("๏ ᴠɪᴇᴡ sᴜᴅᴏʟɪsᴛ ๏", callback_data="check_sudo_list")]
    ]
    await message.reply_video(
        video="https://envs.sh/5h_.mp4",
        caption="» ᴄʜᴇᴄᴋ sᴜᴅᴏ ʟɪsᴛ ʙʏ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.**\n\n» ɴᴏᴛᴇ: ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ.",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

@app.on_callback_query(filters.regex("^check_sudo_list$"))
async def check_sudo_list(client, callback_query: CallbackQuery):
    if callback_query.from_user.id not in SUDOERS:
        return await callback_query.answer("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴜᴅᴏ 😝\n\nᴛʜɪꜱ ʟɪꜱᴛ ᴏɴʟʏ ꜰᴏʀ ᴏᴡɴᴇʀ & ꜱᴜᴅᴏ 😏", show_alert=True)

    owner = await app.get_users(OWNER_ID)
    owner_mention = owner.mention if owner.mention else owner.first_name
    caption = f"˹ʟɪsᴛ ᴏғ ʙᴏᴛ ᴍᴏᴅᴇʀᴀᴛᴏʀs˼\n\n🌹 Oᴡɴᴇʀ ➥ {owner_mention}\n\n"

    keyboard = [
        [InlineKeyboardButton("๏ ᴠɪᴇᴡ ᴏᴡɴᴇʀ ๏", url=f"tg://openmessage?user_id={OWNER_ID}")]
    ]

    count = 1
    for user_id in SUDOERS:
        if user_id == OWNER_ID:
            continue
        try:
            user = await app.get_users(user_id)
            mention = user.mention if user else f"`{user_id}`"
            caption += f"🎁 Sᴜᴅᴏ {count} » {mention}\n"
            keyboard.append(
                [InlineKeyboardButton(f"๏ ᴠɪᴇᴡ sᴜᴅᴏ {count} ๏", url=f"tg://openmessage?user_id={user_id}")]
            )
            count += 1
        except:
            continue

    keyboard.append([InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="back_to_main_menu")])

    await callback_query.message.edit_caption(
        caption=caption,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

@app.on_callback_query(filters.regex("^back_to_main_menu$"))
async def back_to_main_menu(client, callback_query: CallbackQuery):
    keyboard = [
        [InlineKeyboardButton("๏ ᴠɪᴇᴡ sᴜᴅᴏʟɪsᴛ ๏", callback_data="check_sudo_list")]
    ]
    await callback_query.message.edit_caption(
        caption="» ᴄʜᴇᴄᴋ sᴜᴅᴏ ʟɪsᴛ ʙʏ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.\n\n» ɴᴏᴛᴇ: ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ.",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

@app.on_message(filters.command(["delallsudo"], prefixes=["/", "!", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def del_all_sudo(client, message: Message, _):
    removed_count = 0
    for user_id in list(SUDOERS):
        if user_id == OWNER_ID:
            continue
        removed = await remove_sudo(user_id)
        if removed:
            SUDOERS.remove(user_id)
            removed_count += 1

    await message.reply_text(f"✅ Removed {removed_count} users from sudo list.")
