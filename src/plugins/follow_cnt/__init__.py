from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json
import urllib3
import time

follow_cnt = on_command("follow_cnt", aliases={'关注数', 'follow_cnt'}, priority=5)

@follow_cnt.handle()
async def follow_cnt_handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args == "jws":
        mid = "19968159"
    elif args == "npy":
        mid = "11243426"
    else:
        await setu.send(Message("泥发了啥子哦，看不懂qwq"))
        return        
    try:
        url = "https://api.bilibili.com/x/relation/stat?vmid=" + mid + "&jsonp=jsonp"
        
        r = urllib3.PoolManager().request('GET', url)
        hjson = json.loads(r.data.decode())
        following_cnt = hjson["data"]["following"]
        follower_cnt = hjson["data"]["follower"]

        await follow_cnt.send(Message("following: " + str(following_cnt) + "\n" + "follower: " + str(follower_cnt)))

    except Exception as e:
        print(e)
        await follow_cnt.send(Message("人家被泥玩坏了辣！"))