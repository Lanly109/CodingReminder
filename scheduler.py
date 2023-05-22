from datetime import datetime
from .utils import *
from .api import *
from .oldapi import *
from . import sv, files
from . import group_list
from . import bot
from nonebot import on_startup

@sv.scheduled_job('interval', minutes=120)  # 2小时进行1次爬虫
async def loadMsg():
    try:
        await getNiuKe()
    except:
        pass
    try:
        await getContest()
    except:
        pass
    try:
        await getNiuKeSchool()
    except:
        pass
    try:
        await getLeetcodeDaily()
    except:
        pass

@sv.scheduled_job('cron', hour='8', minute='00', jitter=00)
async def leetcodeDaily():
    return
    await getLeetcodeDaily()
    global bot
    global group_list
    global contest_list
    data = load_json("leetcode_daily.json")
    msg = get_problem_remind(data['id'], data['title'], data['date'], data['difficulty'], data['url'], data['content'])
    for gid in group_list['group']:
        await bot.send_group_msg(group_id = gid, message = msg)

@sv.scheduled_job('interval', minutes=1)
async def CodingCheck ():
    global bot
    global group_list

    now = datetime.now()

    for contest_file in files:
        contests = await get_upcoming_contest(contest_file)
        if contests is None:
            continue
        for name, info in contests:
            time = datetime.strptime(info['start_time'],  "%Y-%m-%d %H:%M")
            link = info['link']

            delta = time - now
            if 3540 < delta.total_seconds() <= 3600:
                msg = get_contest_remind(name, time, link)
                for gid in group_list['contest']:
                    try:
                        await bot.send_group_msg(group_id = gid, message = msg)
                    except Exception as e:
                        print(e)
                        pass

@on_startup
async def init():
    await do_flush()

@sv.on_fullmatch('flush', only_to_me = True)
async def flush(bot, ev):
    await do_flush()
    await bot.finish(ev, "ok")

async def do_flush():
    await getContest()
    await getNiuKe()
    await getNiuKeSchool()
    await getLeetcodeDaily()

