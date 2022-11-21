import json
from datetime import datetime
import os

def load_json(file_name):
    path = os.path.join(os.path.dirname(__file__), file_name)
    if not os.path.exists(path):
        return
    with open(path, encoding='utf8') as f:
        data = json.load(f)
        return data

def save_json(file_name, args):
    path = os.path.join(os.path.dirname(__file__), file_name)
    with open(path, 'w', encoding='utf8') as f:
        json.dump(args , f, ensure_ascii=False, indent=2)

def getFirstcontest(file_name):
    data = load_json(file_name)
    try:
        contests = list(data.items())
        now = datetime.now()
        for contest in contests:
            name, info = contest
            time = datetime.strptime(info['time'],  "%Y-%m-%d %H:%M")
            if now <= time:
                return name, info
        return None, None
    except Exception as e:
        print(e)
        return None, None

def getText(msg):
    text = ""
    for name, info in msg.items():
        text += f"\n比赛名称：{name}"
        text += f"\n比赛时间：{info['time']}"
        text += f"\n比赛链接：{info['link']}\n"
    return text

def get_contest_remind(contest_name, name, time, link):
    text = f'''比赛通知！
比赛平台：{contest_name}
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
