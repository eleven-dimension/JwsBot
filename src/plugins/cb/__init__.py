from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json

cb = on_command("cb", aliases={'cb'}, priority=5)

@cb.handle()
async def cb_handle(bot: Bot, event: Event, state: T_State):
    await cb.send(Message("[CQ:face,id=318]"))