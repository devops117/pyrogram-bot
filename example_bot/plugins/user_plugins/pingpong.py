import pyrocatto.filters # pyrocatto.filters.wheel_user
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command('ping') & pyrocatto.filters.wheel_user)
async def ping(client: Client, msg: Message):
    await msg.reply_text("PONG")
