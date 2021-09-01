from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json

xyx = on_command("xyx", aliases={'xyx'}, priority=5)

@xyx.handle()
async def xyx_handle(bot: Bot, event: Event, state: T_State):
    await xyx.send(Message("[CQ:face,id=178]"))