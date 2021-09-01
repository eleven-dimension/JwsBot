from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json

maogou = on_command("maogou", aliases={'maogou'}, priority=5)

@maogou.handle()
async def maogou_handle(bot: Bot, event: Event, state: T_State):
    await maogou.send(Message("猫狗打架！"))