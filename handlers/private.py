from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAECL0phG6f50Xd7OG\_i8YaNIzz7gh2UbAAC2gEAAuaC4EQGx1I9UzNAziAE")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ  ɢʀᴏᴜᴩ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. 
ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜsɪᴄ ғʀᴇᴇʟʏ 🤗 Developed By [👻👻](https://t.me/dangerpro_bot) !**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner ✨️", url="https://t.me/danger_of_telegram")
                  ],[
                    InlineKeyboardButton(
                        "Support❤", url="https://t.me/danger_bots"
                    ),
                    InlineKeyboardButton(
                        "Group 🌴", url="https://t.me/nammude_keralam"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "Commands👀", url="https://telegra.ph/Dangerbots-12-05"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/danger_of_telegram")
                ]
            ]
        )
   )
