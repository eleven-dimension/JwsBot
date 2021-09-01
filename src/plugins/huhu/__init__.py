from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message

import json
import urllib3
import requests
import re
import random

huhu = on_command("huhu", aliases={'huhu'}, priority=5)

@huhu.handle()
async def huhu_handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()

    home_page_url = 'https://t.me/s/HourlyFops'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

    home_page_html = requests.get(home_page_url, headers=headers)    
    max_huhu_img_index = int(re.findall('<link rel="canonical" href="/s/HourlyFops\?before=(.*?)">', home_page_html.text, re.I|re.S|re.M)[0])

    print(max_huhu_img_index)

    if len(args) == 1 and args == "0":
        await huhu.send(Message("泥到底要不要看狐狐图嘛！"))
        return
    elif (not args.isdigit()) and len(args) > 0:
        await huhu.send(Message("泥发了啥子哦，看不懂qwq"))
        return
    else:
        huhu_num = 1 if len(args) == 0 else int(args)

    try:    
        try:
            if huhu_num >= 5:
                await huhu.send(Message("这么喜欢看狐狐图，等我一张一张发给泥哦"))

            await huhu.send(Message("狐狐图来得不容易，可能会有点慢哦"))
            for i in range(huhu_num):
                cur_img_index = random.randrange(11, max_huhu_img_index)
                cur_img_page_url = 'https://t.me/HourlyFops/' + str(cur_img_index)
                cur_img_page_html = requests.get(cur_img_page_url, headers=headers)
                cur_img_url = re.findall('<meta property="og:image" content="(.*?)">', cur_img_page_html.text, re.I|re.S|re.M)[0]
                
                print(cur_img_url)

                cq = "[CQ:image,file=" + cur_img_url + ",id=40000]"
                await huhu.send(Message(cq))

        except Exception as e:
            print(e)
            await huhu.send(Message("人家被泥玩坏了辣！"))
    except Exception as e:
        print(e)
        await huhu.send(Message("人家被泥玩坏了辣！"))