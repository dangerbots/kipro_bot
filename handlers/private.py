
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**ℌ𝔢𝔶 𝔡𝔢𝔞𝔯 𝔱𝔥𝔦𝔰 𝔦𝔰 𝔞『𝔗𝔊』☆𝔔𝔲𝔢𝔢𝔫 ☆࿐>ᴰᵃⁿᵍᵉʳ-ᴮᵒᵗ 𝔱𝔥𝔢 𝔣𝔞𝔰𝔱𝔢𝔰𝔱 𝔄𝔫𝔡 𝔫𝔢𝔵𝔱 𝔤𝔢𝔫𝔞𝔯𝔞𝔱𝔦𝔬𝔫 𝔰𝔲𝔭𝔢𝔯 𝔥𝔦𝔤𝔥 𝔮𝔲𝔞𝔩𝔦𝔱𝔶 𝔪𝔲𝔰𝔦𝔠 𝔭𝔩𝔞𝔶𝔢𝔯 𝔴𝔦𝔱𝔥 𝔠𝔬𝔬𝔩 𝔣𝔢𝔞𝔱𝔲𝔯𝔢𝔰 𝔡𝔢𝔰𝔦𝔤𝔫𝔢𝔡 𝔣𝔬𝔱 𝔶𝔬𝔲.....
𝓭𝓮𝓼𝓲𝓰𝓷𝓮𝓭 𝓫𝔂: [𝗔𝗻𝗼𝗻𝘆𝗺𝗼𝘂𝘀么𝗸𝗶𝗱](https://t.me/danger_of_telegram)**
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
