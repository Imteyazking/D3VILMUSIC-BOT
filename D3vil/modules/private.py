# D3vil 
# Copyright (C) 2021  D3KRISH

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from D3vil.modules.msg import Messages as tr
from pyrogram import Client, filters
from D3vil.helpers.filters import other_filters2
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from D3vil.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,BOT_USERNAME
logging.basicConfig(level=logging.INFO)

@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAANvYLub26OWjDEbs5Jq--m4-Ja7SM8AAhIEAAKT29hVxAskq65u1b4fBA")
    await message.reply_text(
        f"""**Hey, I'm [MusicBot](https://t.me/D3VIL_SUPPORT) For VC 🎵""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group 🙋‍♀️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "📲 Channel", url=f"https://t.me/D3VIL_SUPPORT"), 
                    InlineKeyboardButton(
                        "💬 Support Chat", url=f"https://t.me/D3VIL_BOT_SUPPORT")
                ],[
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url=f"https://github.com/D3KRISH/D3VILMUSIC-BOT")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**🔴 {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Support Chat", url=f"https://t.me/D3VIL_SUPPORT"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/D3VIL_BOT_SUPPORT"
        button = [
            [InlineKeyboardButton("➕ Add me to your Group 🙋‍♀️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '📲 Channel', url=f"https://t.me/D3VIL_SUPPORT"),
             InlineKeyboardButton(text = '💬 Support', url=f"https://t.me/D3VIL_BOT_SUPPORT")],
            [InlineKeyboardButton(text = '🛠 Source Code 🛠', url=f"https://github.com/D3KRISH/D3VILMUSIC-BOT")],
            [InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**🙋‍♀️ Hello there! I can play music in the voice chats of telegram groups & channels.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🟡 Click here for help 🟡", url=f"https://telegra.ph/%C9%963%E2%B1%B1%E1%B6%96%C8%B4%EA%AC%BA%E1%B6%99%C8%BF%E1%B6%96%C9%95%C9%93%EA%9D%8D%C8%B6-05-27-2"
                    )
                ]
            ]
        ),
    )
