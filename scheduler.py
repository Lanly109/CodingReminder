from datetime import datetime
from .utils import *
from .api import *
from . import sv
from . import contest_list
from . import group_list
from . import bot

@sv.scheduled_job('interval', minutes=120)  # 2小时进行1次爬虫
async def loadMsg():
    getNiuKe()
    getCodefores()
    getCodeChef()
    getAtcoder()
    getNiuKeSchool()

@sv.scheduled_job('interval', minutes=1)
async def Coding_check ():
    global bot
    global group_list
    global contest_list

    now = datetime.now()

    for contest_name, contest_file in contest_list.items():
        name, info = getFirstcontest(contest_file)
        if name is None:
            continue
        if 'time' not in info:
            continue 
        time = datetime.strptime(info['time'],  "%Y-%m-%d %H:%M")
        link = info['link']

        delta = time - now
        if 3540 < delta.total_seconds() <= 3600:
            msg = get_contest_remind(contest_name, name, time, link)
            for gid in group_list['group']:
                await bot.send_group_msg(group_id = gid, message = msg)

@sv.on_fullmatch('flush', only_to_me = True)
async def flush(bot, ev):
    getNiuKe()
    getCodefores()
    getCodeChef()
    getAtcoder()
    getNiuKeSchool()
    await bot.finish(ev, "ok")
