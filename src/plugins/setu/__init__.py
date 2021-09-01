from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json
import urllib3
import time

setu = on_command("setu", aliases={'色图', '涩图', '瑟图', 'setu'}, priority=5)

@setu.handle()
async def setu_handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()

    if len(args) == 1 and args == "0":
        await setu.send(Message("泥到底要不要看涩图嘛！"))
        return
    elif (not args.isdigit()) and len(args) > 0:
        await setu.send(Message("泥发了啥子哦，看不懂qwq"))
        return
    else:
        setu_num = 1 if len(args) == 0 else int(args)
    
    try:
        if setu_num >= 5:
            await setu.send(Message("lsp，这么多，等我一张一张发给泥哦"))

        url = "https://api.lolicon.app/setu/v2"

        for i in range(setu_num):
            r = urllib3.PoolManager().request('GET', url)
            hjson = json.loads(r.data.decode())
            img_url = hjson["data"][0]["urls"]["original"]
            cq = "[CQ:image,file=" + img_url + ",id=40000]"
            print(cq)
            try:
                await setu.send(Message(cq))
            except Exception as e:
                print(e)
                i -= 1
        if setu_num >= 5:
            time.sleep(10)
            await setu.send(Message("发完了辣！"))
    except Exception as e:
        print(e)
        await setu.send(Message("人家被泥玩坏了辣！"))