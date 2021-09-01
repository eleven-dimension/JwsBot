from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json

music = on_command("music", aliases={'music'}, priority=5)

@music.handle()
async def music_handle(bot: Bot, event: Event, state: T_State):
    cq = "[CQ:music,type=163,id=28949129]"
    await music.send(Message(cq))