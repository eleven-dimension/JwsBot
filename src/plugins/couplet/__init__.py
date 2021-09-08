from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json
import urllib3
import time

couplet = on_command("couplet", aliases={'duiduilian', 'duiduizi','对对子', '对对联', '对联', 'couplet'}, priority=5)

def is_command_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

@couplet.handle()
async def couplet_handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()

    if not is_command_all_chinese(args):
        await couplet.send(Message("泥呜啦呜啦说了啥？说中文！"))
        return                    
    try:
        url = "https://ai-backend.binwang.me/v0.2/couplet/"

        r = urllib3.PoolManager().request('GET', url + args)
        hjson = json.loads(r.data.decode())
        unicode_couplet = hjson["output"][0]
        print(unicode_couplet)
        try:
            await couplet.send(Message(unicode_couplet))
        except Exception as e:
            print(e)
            await couplet.send(Message("人家被泥玩坏了辣！"))

    except Exception as e:
        print(e)
        await couplet.send(Message("人家被泥玩坏了辣！"))