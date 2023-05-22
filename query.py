import hoshino
from hoshino import priv
from .utils import *
from .search import *
from . import sv, files, group_list

@sv.on_fullmatch(('当前比赛'))
async def contest_now(bot, ev):
    global files
    title = "当前进行的比赛：\n"
    text = ""
    for file in files:
        msg = await get_now_contest(file)
        text += getText(msg)
    text = title + text
    text = text.strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('今日比赛'))
async def contest_today(bot, ev):
    global files
    title = "今日比赛：\n"
    text = ""
    for file in files:
        msg = await get_today_contest(file)
        text += getText(msg)
    text = title + text
    text = text.strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('明日比赛'))
async def contest_tomorrow(bot, ev):
    global files
    title = "明日比赛：\n"
    text = ""
    for file in files:
        msg = await get_tomorrow_contest(file)
        text += getText(msg)
    text = title + text
    text = text.strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('leetcode','lc', '力扣'))
async def leetcodeDaily(bot, ev):
    msg = await get_contest("contests.json", lambda start, end, link: "leetcode" in link)
    text = "leetcode:\n" + getText(msg)
    text = text.strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('ctf'))
async def contest_ctf(bot, ev):
    msg = await get_contest("contests.json", lambda start, end, link: any([i in link for i in ["ctftime", "hackerearth", "hackerrank"]]))
    text = "ctf:\n" + getText(msg)
    text = text.strip()
    await bot.finish(ev, text)


@sv.on_fullmatch(('topcoder'))
async def contest_topcoder(bot, ev):
    msg = await get_contest("contests.json", lambda start, end, link: "topcoder" in link)
    text = "topcoder:\n" + getText(msg)
    text = text.strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('atcoder', "at"))
async def contest_atcode(bot, ev):
    msg = await get_contest("contests.json", lambda start, end, link: "atcoder" in link)
    text = "atcoder:\n" + getText(msg)
    text = text.strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('ucup'))
async def contest_ucup(bot, ev):
    msg = await get_contest("contests.json", lambda start, end, link: "ucup" in link)
    text = "ucup:\n" + getText(msg)
    text = text.strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('yukicoder', 'yuki'))
async def contest_yukicode(bot, ev):
    msg = await get_contest("contests.json", lambda start, end, link: "yukicoder" in link)
    text = "yukicoder:\n" + getText(msg)
    text = text.strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('codechef'))
async def contest_codechef(bot, ev):
    msg = await get_contest("contests.json", lambda start, end, link: "codechef" in link)
    text = "codechef:\n" + getText(msg)
    text = text.strip()
    await bot.finish(ev, message = text)

@sv.on_fullmatch(('cf', 'codeforces'))
async def contest_codeforces(bot, ev):
    msg = await get_contest("contests.json", lambda start, end, link: "codeforces" in link)
    text = "codeforces:\n" + getText(msg)
    text = text.strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('牛客'))
async def contest_niuke(bot, ev):
    msg = await get_contest("niuke.json", lambda start, end, link: True)
    text = "牛客:\n" + getText(msg)
    await bot.send(ev, text)
    msg = await get_contest("niuke_school.json", lambda start, end, link: True)
    text += getText(msg)
    text = text.strip()
    await bot.finish(ev, text)

@sv.on_fullmatch('启动比赛通知', only_to_me = True)
async def notice(bot, ev):
    global group_list
    uid = ev.user_id
    gid = ev.group_id
    if priv.check_priv(ev, priv.ADMIN):
        if gid in group_list['contest']:
            msg = '本群已经启用比赛通知啦~'
        else:
            group_list['contest'].append(gid)
            save_json("group.json", group_list)
            msg = '成功启用比赛通知啦！'
    else:
        msg = '你没有权力哦！'
    await bot.finish(ev, msg)


@sv.on_fullmatch('取消比赛通知', only_to_me = True)
async def CancelNotice(bot, ev):
    global group_list
    uid = ev.user_id
    gid = ev.group_id
    if priv.check_priv(ev, priv.ADMIN):
        if gid not in group_list['contest']:
            msg = '本群没有启用消息通知啦~'
        else:
            group_list['contest'].remove(gid)
            save_json("group.json", group_list)
            msg = '成功取消消息通知啦！'
    else:
        msg = '你没有权力哦！'
    await bot.finish(ev, msg)

@sv.on_prefix('find')
async def get_cf_msg(bot, ev):
    name = ev.message.extract_plain_text()
    uid = ev.user_id
    msg = getCfSelfMsg(name) if len(name) < 60 else "不要捣乱哦！  [CQ:face,id=106]"
    if "超时" in msg or "无法访问" in msg:
        msg = "cf访问超时，请稍后查询qwq"
    elif "找不到" in msg:
        msg = "没找到这个人qwq"
    await bot.finish(ev, msg)

# @sv.on_fullmatch('通知我', only_to_me = True)
# async def NoticeMe(bot, ev):
#     message_type = session.ctx['message_type']
#     if(message_type == 'private'):
#         self_id = session.ctx['user_id']
#         file = open('id.json', 'r', encoding='utf-8')
#         js = file.read()
#         id = json.loads(js)
#         Id = id['user']
#         ID = []
#         for it in Id:
#             if it == self_id:
#                 await session.bot.send_private_msg(user_id=session.ctx['user_id'], message="您已经被通知无需操作！")
#                 return
#             ID.append(it)
#         ID.append(self_id)
#         id["user"] = ID
#         print(id)
#         fp = open("id.json", 'w', encoding='utf-8')
#         item_json = json.dumps(id, ensure_ascii=False)
#         fp.write(item_json)
#         fp.close()
#         file.close()
#         await session.bot.send_private_msg(user_id=session.ctx['user_id'], message="将在比赛开始前一个小时通知您！")
#     else:
#         await session.bot.send_private_msg(user_id=session.ctx['user_id'], message="加好友才能操作哦！")

# @sv.on_fullmatch('取消通知我', only_to_me = True)
# async def NoticeMe(bot, ev):
#     message_type = session.ctx['message_type']
#     if(message_type == 'private'):
#         self_id = session.ctx['user_id']
#         file = open('id.json', 'r', encoding='utf-8')
#         js = file.read()
#         id = json.loads(js)
#         Id = id['user']
#         ID = []
#         for it in Id:
#             if it == self_id:
#                 continue
#             ID.append(it)
#         id["user"] = ID
#         print(id)
#         fp = open("id.json", 'w', encoding='utf-8')
#         item_json = json.dumps(id, ensure_ascii=False)
#         fp.write(item_json)
#         fp.close()
#         file.close()
#         await session.bot.send_private_msg(user_id=session.ctx['user_id'], message="已经取消！")

# @sv.on_fullmatch('新闻', only_to_me = True)
# async def news(bot, ev):
    # text = getNews()
    # await session.bot.send_private_msg(user_id=1173007724, message=text)
    # await session.bot.send_private_msg(user_id=1206770096, message=text)
    # await session.bot.send_private_msg(user_id=743742996, message=text)
    # await bot.finish(ev, text)
    # message_type = session.ctx['message_type']
    # if (message_type == 'group'):
    #     await session.bot.send_group_msg(group_id=session.ctx['group_id'], message=text)
    # elif (message_type == 'private'):
    #     await session.bot.send_private_msg(user_id=session.ctx['user_id'], message=text)
