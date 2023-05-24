from .utils import *
from .sqlite3 import RecordDAO, sqlite3
from bs4 import BeautifulSoup
import requests
from requests import exceptions
import os
import time

db_path = os.path.join(os.path.dirname(__file__), "cf.db")

db = RecordDAO(db_path, "cfer")

CACHE_TIME = 60 * 60 * 24 * 2 # cache 2 days

def getSorce(name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0)Gecko/20100101 Firefox/66.0"
    }

    url = "https://codeforc.es/profile/%s" % (name)
    html = ""
    try:
        r = requests.get(url, timeout=2, headers=headers)
        r.raise_for_status()
        if r.url != url:
            return [1]
        html = r.text
    except exceptions.Timeout as e:
        print("超时！")
        return [2]
    except requests.HTTPError:
        print('http状态码非200')
        return [3]

    soup = BeautifulSoup(html, "html.parser")
    div = soup.find("div", class_="info")
    ul = div.find("ul")
    li = ul.find('li')
    span = li.find_all("span")
    # print(span)
    sorce = []
    for it in span:
        sorce.append(it.string)
    data = []
    data.append(sorce[0])
    data.append(sorce[-1])
    return data


def getCfSelfMsg(name):
    history = db.get_cfer(name)
    now = time.time() // 1
    if history and now - history[2] < CACHE_TIME:
        return history[1]

    url = "https://codeforc.es/contests/with/%s" % (name)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0)Gecko/20100101 Firefox/66.0"
    }
    html = ""
    print(url)
    try:
        r = requests.get(url, timeout=3, headers=headers)
        r.raise_for_status()
        if r.url != url:
            text = "找不到 " + name + " [CQ:face,id=15][CQ:face,id=15]"
            db.insert_cfer(name, text)
            return text
        html = r.text
    except exceptions.Timeout as e:
        return "超时"

    except requests.HTTPError:
        return "cf官网无法访问"
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find("div", class_="datatable")
    tbody = div.find("tbody")
    div1 = 0
    div2 = 0
    div3 = 0
    other = 0
    contestNum = 0
    div1_ranks = 0
    div2_ranks = 0
    div3_ranks = 0
    other_ranks = 0
    div1_prombles = 0
    div2_prombles = 0
    div3_prombles = 0
    other_prombles = 0
    rating = 0
    max = 1000000
    f = 1

    for it in tbody.find_all("tr"):
        td = it('td')
        contestName = td[1].text.strip()
        if (max > int(td[3].text.strip(), 10)):
            max = int(td[3].text.strip(), 10)

        if ("Div. 2" in contestName):
            div2_ranks += int(td[3].text.strip(), 10)
            div2_prombles += int(td[4].text.strip(), 10)
            div2 += 1
        elif ("Div. 1" in contestName):
            div1_ranks += int(td[3].text.strip(), 10)
            div1_prombles += int(td[4].text.strip(), 10)
            div1 += 1
        elif ("Div. 3" in contestName):
            div3_ranks += int(td[3].text.strip(), 10)
            div3_prombles += int(td[4].text.strip(), 10)
            div3 += 1
        else:
            other_ranks += int(td[3].text.strip(), 10)
            other_prombles += int(td[4].text.strip(), 10)
            other += 1

        rating += int(td[5].text.strip(), 10)
        if f == 1:
            contestNum = int(td[0].string.strip(), 10)
            f = 0

    if contestNum == 0:
        text = name + " 还没有打过比赛呢[CQ:face,id=15][CQ:face,id=15]"
        db.insert_cfer(name, text)
        return text

    sorce = getSorce(name)
    if sorce[0] == 2:
        return "超时"
    elif sorce[0] == 3:
        return "cf官网无法访问"
    text = "cf-ID：%s\n" % (name)
    text += "cf-rating: %s\n" % (sorce[0])
    text += "cf最高rating: %s\n" % (sorce[1])
    text += "cf最高排名：%s\n" % (max)
    text += "比赛总数：%s\n" % (contestNum)
    text += "每场平均加分：%s\n\n" % (round(rating / contestNum, 2))
    # print(text)

    if (div1 == 0):
        pass
        # text = "div1 : 还没有打过哦！\n"
    else:
        text += "div1-参加场数: %s \n" % (div1)
        text += "div1-均场解题数：%s\n" % (round(div1_prombles / div1, 2))
        text += "div1-均场排名：%s\n\n" % (round(div1_ranks / div1, 2))

    if (div2 == 0):
        pass
        # text += "div2: 还没有没打过哦！\n"
    else:
        text += "div2-参加场数: %s \n" % (div2)
        text += "div2-均场解题数：%s\n" % (round(div2_prombles / div2, 2))
        text += "div2-均场排名：%s\n\n" % (round(div2_ranks / div2, 2))
    if (div3 == 0):
        pass
        # text += "div3: 还没有打过哦！"
    else:

        text += "div3-参加场数: %s \n" % (div3)
        text += "div3-均场解题数：%s\n" % (round(div3_prombles / div3, 2))
        text += "div3-均场排名：%s\n\n" % (round(div3_ranks / div3, 2))

    if (other != 0):
        text += "others-参加场数: %s \n" % (other)
        text += "others-均场解题数：%s\n" % (round(other_prombles / other, 2))
        text += "others-均场排名：%s\n\n" % (round(other_ranks / other, 2))

    text += "(div3蓝名以上的时候打的比赛不算在内)"
    # print(text)
    db.insert_cfer(name, text)
    return text

# @nonebot.scheduler.scheduled_job('interval', minutes=1)
# async def cloock():
#     bot = nonebot.get_bot()
#     now = datetime.now()
#
#     if now.hour == 3 and now.minute == 30:
#         updateMsg()
#         await bot.send_private_msg(user_id=1173007724, message="数据爬取成功")
#     elif now.hour == 4 and now.minute == 10:
#         updateMsg()
#         await bot.send_private_msg(user_id=1173007724, message="数据爬取成功")
#     elif now.hour == 5 and now.minute == 10:
#         updateMsg()
#         await bot.send_private_msg(user_id=1173007724, message="数据爬取成功")
