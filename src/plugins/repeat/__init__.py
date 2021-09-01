from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json

repeat = on_command("repeat", aliases={'复读'}, priority=5)

@repeat.handle()
async def repeat_handle(bot: Bot, event: Event, state: T_State):
    print(event.get_session_id())
    print(event.get_event_name())
    args = str(event.get_message()).strip()
    await repeat.send(Message(str(args)))