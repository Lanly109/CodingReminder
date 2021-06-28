import json
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
        return list(data.items())[0]
    except:
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
'''
    return text
