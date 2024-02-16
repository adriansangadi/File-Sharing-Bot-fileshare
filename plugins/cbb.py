#(©)Codexbotz
#(©)Cold_Onez

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Mᴀsᴛᴇʀ : <a href='https://t.me/knmlpro2'>Kɴᴍʟᴘʀᴏ2</a>\n○ Lᴀɴɢᴜᴀɢᴇ : <code>Python3</code>\n○ Cʜᴀɴɴᴇʟ : @Knmlpro2\n○ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ : @Knmlpro2_group</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
