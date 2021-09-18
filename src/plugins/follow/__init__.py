from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json
import urllib3
import time

follow = on_command("follow", aliases={'关注', 'follow'}, priority=5)

@follow.handle()
async def follow_handle(bot: Bot, event: Event, state: T_State):
    try:
        url = 'https://api.bilibili.com/x/relation/followings?vmid=19968159&pn=1&ps=20&order=desc&jsonp=jsonp'
        
        r = urllib3.PoolManager().request('GET', url)
        hjson = json.loads(r.data.decode())
        following_list = hjson["data"]["list"]

        for user in following_list:
            await follow.send(Message(
                str(user['mid']) + "\n" + str(user['uname']) + "\n" + str(user['sign']) + "\n" + "https://space.bilibili.com/" + str(user['mid'])
            ))

    except Exception as e:
        print(e)
        await follow.send(Message("人家被泥玩坏了辣！"))