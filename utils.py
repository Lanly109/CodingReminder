import json
from datetime import datetime, timedelta
import os

def load_json(file_name) -> dict:
    path = os.path.join(os.path.dirname(__file__), file_name)
    if not os.path.exists(path):
        return {}
    with open(path, encoding='utf8') as f:
        data = json.load(f)
        return data

def save_json(file_name, args):
    path = os.path.join(os.path.dirname(__file__), file_name)
    with open(path, 'w', encoding='utf8') as f:
        json.dump(args , f, ensure_ascii=False, indent=2)

async def get_contest(file_name, is_ok):
    data = load_json(file_name)
    result = []
    contests = list(data.items())
    for contest in contests:
        _, info = contest
        start_time = datetime.strptime(info['start_time'],  "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(info['end_time'],  "%Y-%m-%d %H:%M")
        link = info['link']
        if is_ok(start_time, end_time, link):
            result.append(contest)
    return result

async def get_upcoming_contest(file_name):
    now = datetime.now()
    return await get_contest(file_name, lambda start, end, link: now < start)

async def get_now_contest(file_name):
    now = datetime.now()
    return await get_contest(file_name, lambda start, end, link: now >= start and now < end)

async def get_today_contest(file_name):
    now = datetime.now()
    today = now - timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
    tomorrow = now + timedelta(days=1)
    return await get_contest(file_name, lambda start, end, link: start >= today and end > now and start < tomorrow)

async def get_tomorrow_contest(file_name):
    now = datetime.now()
    tomorrow = now + timedelta(days=1) - timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
    ttomorrow = tomorrow + timedelta(days=1) 
    return await get_contest(file_name, lambda start, end, link: start >= tomorrow and start < ttomorrow)

def getText(msg):
    text = ""
    for name, info in msg:
        text += f"比赛名称：{name}"
        text += f"\n开始时间：{info['start_time']}"
        if info['end_time']:
            text += f"\n结束时间：{info['end_time']}"
        text += f"\n比赛链接：{info['link']}\n\n"
    if text == "":
        text = "无"
    return text

def get_contest_remind(name, time, link):
    text = f'''比赛通知！
比赛：{name}
比赛时间：{time}
比赛链接：{link}
'''.strip()

    return text

def get_problem_remind(id, name, date, difficulty, url, content):
    text = f'''Leetcode {date} 每日一题！
题目：{id}.{name}
难度：{difficulty}
'''.strip()

    return text

def get_problem_full(id, name, date, difficulty, url, content):
    text = f'''Leetcode {date} 每日一题！
题目：{id}.{name}
难度：{difficulty}
链接：{url}
内容：{content}
'''.strip()

    return text
