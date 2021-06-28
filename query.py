import hoshino
from hoshino import priv
from .utils import *
from .search import *
from . import sv

@sv.on_fullmatch(('atcoder','at', 'ac'), only_to_me = True)
async def contestatcode(bot, ev):
    msg = load_json("atcoder.json")
    text = "比赛平台：Atcoder\n"
    text += getText(msg)
    await bot.finish(ev, text)

@sv.on_fullmatch(('codechef','cc', 'chef','Codechef','CODECHEF'), only_to_me = True)
async def contestCodeChef(bot, ev):
    msg = load_json("codechef.json")
    text = "比赛平台：CodeChef\n"
    text += getText(msg)
    await bot.finish(ev, message = text)

@sv.on_fullmatch(('cf', 'CF', 'CODEFORCES','codeforces','CodeForces'), only_to_me = True)
async def contestCF(bot, ev):
    msg = load_json("cf.json")
    text = "比赛平台：Codeforces\n"
    text += getText(msg)
    await bot.finish(ev, text)

@sv.on_fullmatch(('牛客', 'nk', 'Nk', 'NIUKE', 'Nk'), only_to_me = True)
async def contestNIUKE(bot, ev):
    msg = load_json("niuke.json")
    text = "牛客:\n"
    text += getText(msg)
    await bot.send(ev, text)
    msg = load_json("niuke_school.json")
    text = "牛客高校： \n"
    text += getText(msg)
    await bot.finish(ev, text)

@sv.on_fullmatch('启动消息通知', only_to_me = True)
async def notice(bot, ev):
    uid = ev.user_id
    gid = ev.group_id
    if priv.check_priv(ev, priv.ADMIN):
        data = load_json("group.json")
        if gid in data['group']:
            msg = '本群已经启用消息通知啦~'
        else:
            data['group'].append(gid)
            save_json("group.json", data)
            msg = '成功启用消息通知啦！'
    else:
        msg = '你没有权力哦！'
    await bot.finish(ev, msg)


@sv.on_fullmatch('取消消息通知', only_to_me = True)
async def CancelNotice(bot, ev):
    uid = ev.user_id
    gid = ev.group_id
    if priv.check_priv(ev, priv.ADMIN):
        data = load_json("group.json")
        if gid not in data['group']:
            msg = '本群没有启用消息通知啦~'
        else:
            data['group'].remove(gid)
            save_json("group.json", data)
            msg = '成功取消消息通知啦！'
    else:
        msg = '你没有权力哦！'
    await bot.finish(ev, msg)

@sv.on_prefix('find', only_to_me = True)
async def get_cf_msg(bot, ev):
    name = ev.message.extract_plain_text()
    print(name)
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