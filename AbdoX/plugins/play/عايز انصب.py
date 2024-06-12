from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AbdoX import app
import config
from pyrogram.errors import FloodWait




@app.on_message(filters.command(["عاوز انصب","عاوزه انصب"], ""))
async def maker(client: Client, message: Message):
     await message.reply_video(
        video="https://t.me/HQ_BX/5",
        caption="◍     للتنصيب تواصـل مع مطور السورس ❲ [اطغط هنا](https://t.me/CRAZ_UP) ❳ \n\n√",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
