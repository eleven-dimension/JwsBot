from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json
import urllib3
import time

following = on_command("following", aliases={'关注', 'following'}, priority=5)

@following.handle()
async def following_handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    
    if args == "jws":
        mid = "19968159"
    elif args == "npy":
        mid = "11243426"
    else:
        await setu.send(Message("泥发了啥子哦，看不懂qwq"))
        return     

    try:
        url = 'https://api.bilibili.com/x/relation/followings?vmid=' + mid + '&pn=1&ps=20&order=desc&jsonp=jsonp'
        
        r = urllib3.PoolManager().request('GET', url)
        hjson = json.loads(r.data.decode())
        following_list = hjson["data"]["list"]

        for user in following_list:
            await following.send(Message(
                str(user['mid']) + "\n" + str(user['uname']) + "\n" + str(user['sign']) + "\n" + "https://space.bilibili.com/" + str(user['mid'])
            ))

    except Exception as e:
        print(e)
        await following.send(Message("人家被泥玩坏了辣！"))