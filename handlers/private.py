from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**𝗛𝗲𝘆 𝗕𝗮𝗯𝘆 𝘁𝗵𝗶𝘀 𝗶𝘀 𝗮 𝗲𝗦𝗽𝗼𝗿𝘁 𝗠𝘂𝘀𝗶𝗰𝗫 𝗧𝗵𝗲 𝗙𝗮𝘀𝘁𝗲𝘀𝘁 𝗮𝗻𝗱 𝗡𝗲𝘅𝘁 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗼𝗻 𝗦𝘂𝗽𝗲𝗿 𝗛𝗶𝗴𝗵 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝗠𝘂𝘀𝗶𝗰 𝗣𝗹𝗮𝘆𝗲𝗿 𝘄𝗶𝘁𝗵 𝗖𝗼𝗼𝗹 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 𝗗𝗲𝘀𝗶𝗴𝗻𝗲𝗱 𝗙𝗼𝗿 𝗬𝗼𝘂.....
𝗗𝗲𝘀𝗶𝗴𝗻𝗲𝗱 𝗕𝘆: [𝗔𝗻𝗼𝗻𝘆𝗺𝗼𝘂𝘀么𝗸𝗶𝗱](https://t.me/danger_of_telegram)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner ✨️", url="https://t.me/danger_of_telegram")
                  ],[
                    InlineKeyboardButton(
                        "support 💞", url="https://t.me/danger_bots"
                    ),
                    InlineKeyboardButton(
                        "Group 🌴", url="https://t.me/nammude_Keralam"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Commands👀", url="https://telegra.ph/Dangerbots-12-05"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲..😎**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/danger_bots")
                ]
            ]
        )
   )
