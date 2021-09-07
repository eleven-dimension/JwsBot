from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json
import urllib3
import time

maomao = on_command("maomao", aliases={'maomao'}, priority=5)

@maomao.handle()
async def maomao_handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()

    if len(args) == 1 and args == "0":
        await maomao.send(Message("泥到底要不要看猫猫图嘛！"))
        return
    elif (not args.isdigit()) and len(args) > 0:
        await maomao.send(Message("泥发了啥子哦，看不懂qwq"))
        return
    else:
        maomao_num = 1 if len(args) == 0 else int(args)
        if maomao_num == 0:
            await maomao.send(Message("泥到底要不要看猫猫图嘛！"))
            return           

    print(maomao_num)
    try:
        try:    
            try:
                if maomao_num >= 5:
                    await maomao.send(Message("猫奴，这么多，等我一张一张发给泥哦"))

                url = "https://api.thecatapi.com/v1/images/search"

                for i in range(maomao_num):
                    print(i)
                    r = urllib3.PoolManager().request('GET', url)
                    hjson = json.loads(r.data.decode())
                    img_url = hjson[0]["url"]
                    cq = "[CQ:image,file=" + img_url + ",id=40000]"
                    try:
                        await maomao.send(Message(cq))
                    except Exception as e:
                        print(e)
                        i -= 1
                if maomao_num >= 5:
                    time.sleep(10)
                    await maomao.send(Message("发完了辣！"))
            except Exception as e:
                print(e)
                await maomao.send(Message("人家被泥玩坏了辣！"))
        except Exception as e:
            print(e)
            await maomao.send(Message("人家被泥玩坏了辣！"))
    except Exception as e:
        print(e)
        await maomao.send(Message("人家被泥玩坏了辣！"))