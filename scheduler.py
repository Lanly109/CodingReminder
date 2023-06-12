from datetime import datetime
from .utils import *
from .api import *
from .oldapi import *
from . import sv_cron as sv, sv_lt, files
from . import bot
from nonebot import on_startup
from hoshino.config import SUPERUSERS
import random

    
async def report_to_su(sess, msg_with_sess, msg_wo_sess):
    if sess:
        await sess.send(msg_with_sess)
    else:
        global bot
        sid = bot.get_self_ids()
        if len(sid) > 0:
            sid = random.choice(sid)
            await bot.send_private_msg(self_id=sid, user_id=SUPERUSERS[0], message=msg_wo_sess)

@sv.scheduled_job('interval', minutes=120)  # 2小时进行1次爬虫
async def loadMsg():
    try:
        await getNiuKe()
    except Exception as e:
        sv.logger.exception(e)
        await report_to_su(None, f'Error: {e}', f'牛客比赛信息定时更新时遇到错误：\n{e}')
    try:
        await getContest()
    except Exception as e:
        sv.logger.exception(e)
        await report_to_su(None, f'Error: {e}', f'比赛信息定时更新时遇到错误：\n{e}')
    try:
        await getNiuKeSchool()
    except Exception as e:
        sv.logger.exception(e)
        await report_to_su(None, f'Error: {e}', f'牛客高校比赛信息定时更新时遇到错误：\n{e}')
    try:
        await getLeetcodeDaily()
    except Exception as e:
        sv.logger.exception(e)
        await report_to_su(None, f'Error: {e}', f'leetcode每日一题定时更新时遇到错误：\n{e}')

@sv_lt.scheduled_job('cron', hour='4', minute='00', jitter=00)
async def luogunews():
    try:
        await getLuoguYuebao()
    except Exception as e:
        sv.logger.exception(e)
        await report_to_su(None, f'Error: {e}', f'洛谷日报定时更新时遇到错误：\n{e}')

@sv_lt.scheduled_job('cron', hour='8', minute='00', jitter=00)
async def leetcodeDaily():
    await getLeetcodeDaily()
    data = load_json("leetcode_daily.json")
    msg = get_problem_remind(data['id'], data['title'], data['date'], data['difficulty'], data['url'], data['content'])
    await sv_lt.broadcast(msg, "leetcode_daily")

@sv.scheduled_job('interval', minutes=1)
async def CodingCheck ():
    global bot
    global group_list

    now = datetime.now()

    for contest_file in files:
        contests = await get_upcoming_contest(contest_file)
        if not contests:
            continue
        for info in contests:
            name = info['name']
            start_time = datetime.strptime(info['start_time'],  "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(info['end_time'],  "%Y-%m-%d %H:%M")
            link = info['link']

            delta = start_time - now
            if 3540 < delta.total_seconds() <= 3600:
                msg = get_contest_remind(name, start_time, end_time, link)
                await sv.broadcast(msg, "contest_remaind")

@on_startup
async def init():
    try:
        await do_flush()
    except Exception as e:
        sv.logger.exception(e)
        await report_to_su(None, f'Error: {e}', f'初始化比赛信息时遇到错误：\n{e}')

@sv.on_fullmatch('flush', only_to_me = True)
async def flush(bot, ev):
    try:
        await do_flush()
    except Exception as e:
        sv.logger.exception(e)
        await bot.finish(ev, f'Error: {e}')
    await bot.finish(ev, "ok")

async def do_flush():
    await getContest()
    await getNiuKe()
    await getNiuKeSchool()
    await getLeetcodeDaily()
    await getLuoguYuebao()

