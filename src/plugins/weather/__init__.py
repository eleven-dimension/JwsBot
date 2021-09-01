from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json
import urllib3

weather = on_command("weather", aliases={'weather'}, priority=5)

@weather.handle()
async def weather_handle(bot: Bot, event: Event, state: T_State):

    await weather.send(Message("看什么看，人家还没发育好呢~"))