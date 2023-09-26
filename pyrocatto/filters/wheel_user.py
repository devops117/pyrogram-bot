import pyrogram # pyrogram.Client
from pyrogram.types import Message


def user_in_wheel(_, client: pyrogram.Client, msg: Message):
    return msg.from_user.id in client.addons.wheel_userids


wheel_user = pyrogram.filters.create(user_in_wheel)

__all__ = ["wheel_user"]
