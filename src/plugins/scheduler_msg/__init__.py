from nonebot import on_command, require, get_driver, get_bot
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message
import nonebot.adapters.cqhttp
import _thread
import random
import time

scheduler = require('nonebot_plugin_apscheduler').scheduler

@scheduler.scheduled_job('cron', hour=23, minute=3, id="coax_jws_sleep")
async def coax_jws_sleep():
    bot = get_bot()
    jws_id = 1015872615

    coax_jws = [
        "有木有好好碎觉觉！\n再熬夜就把你\n杀~死~哦~\n人家会好好疼爱你尸体的啦！",
        "十一点了喽，舒宝舒宝还不赶快睡觉！\n晚睡对皮肤不好哦",
        "你自己看看几点了！！\n不睡等着挨揍？",
        "想我想得睡不着？\n睡觉！！立刻！！",
        "十一点，命令你睡觉",
        "舒宝，我们睡觉好不啦！\n困了啦人家！",
        "睡不着？一起数羊！一只羊、两只羊、三只羊、喜羊羊，美羊羊，懒羊羊，沸羊羊，小肥羊，海底捞，麻酱，小料，金针菇，虾滑，宽粉，海带，豆芽，大海螺，菠菜",
        "啊\n我得了一种不能睡觉的病毒\n怎么办，亲爱的\n并且这种病毒和你相关联\n"\
        "你要是不睡我也睡不着\n具有很强的传染性\n我妈还没抱上孙子呢\n我一定要活下去\n就让我们一起睡觉吧！\n是你睡我？还是我睡你啊？",
        "十一点还不睡觉是想和我做爱？",
        "不睡觉在干嘛呢？谈恋爱？超级吃醋醋！",
        "猫猫不睡觉是想和主人玩冰恋嘛？"
    ]
    random.seed(int(time.time()))
    await bot.send_private_msg(user_id=jws_id, message=random.choice(coax_jws))

@scheduler.scheduled_job('cron', hour=23, minute=13, id="force_jws_sleep")
async def force_jws_sleep():
    bot = get_bot()
    jws_id = 1015872615

    coax_jws = [
        "炒笨猫", "香菇猫块", "大盆猫", "清蒸猫", "红烧猫", "糖醋猫", "葱油猫", "香辣猫", "茄子炖猫", "麻辣猫", "水煮猫", "酸菜猫", 
        "草猫水饺", "辣橘猫", "红烧橘猫", "橘猫转豆腐", "酸菜猫腩", "铁板猫柳", "铁锅碟猫头", "香辣猫肉培根", "香辣猫肉丝", 
        "油爆猫双脆", "蒜苔猫肚", "猫血旺", "炒猫肚", "米粉猫肉", "红烧猫排骨", "冬瓜猫排骨", "蒜香猫排骨", "爆炒猫肚", "醋溜猫肝尖", 
        "红扒猫脸", "爆炒猫大肠", "五香猫", "干煸猫肉", "猫肉圆"
    ]
    random.seed(int(time.time()))
    await bot.send_private_msg(user_id=jws_id, message="要是还没睡，等着变成" + random.choice(coax_jws) + "吧你！")

'''
@scheduler.scheduled_job('cron', hour=7, minute=50, id="coax_jws_work")
async def coax_jws_work():
    bot = get_bot()
    jws_id = 1015872615

    await bot.send_private_msg(user_id=jws_id, message="大笨猫快起来上班！￣︿￣")
'''
