from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"𝗧𝗵𝗶𝘀 𝗜𝘀 𝗕𝗼𝘁 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝗰𝗲 𝗝𝗼𝗶𝗻 @danger_bots 𝗙𝗼𝗿 𝗛𝗲𝗹𝗽")
  return                        
