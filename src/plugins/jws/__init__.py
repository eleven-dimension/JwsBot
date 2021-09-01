from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json

jws = on_command("jws", aliases={'voice'}, priority=5)

@jws.handle()
async def jws_handle(bot: Bot, event: Event, state: T_State):
    await jws.send(Message("请您聆听姜婉猫bot对于毛泽东思想的历史意义的回答！"))
    cq = "[CQ:record,file=jws.mp3]"
    await jws.send(Message(cq))