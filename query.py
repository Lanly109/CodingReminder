import hoshino
from hoshino import priv
from .utils import *
from .search import *
from . import sv_info as sv, files
from hoshino.util import FreqLimiter

lmt = FreqLimiter(10)

@sv.on_fullmatch(('当前比赛'))
async def contest_now(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    global files
    title = "当前进行的比赛：\n"
    msg = await get_now_contest(files)
    text = (title + getText(msg)).strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('今日比赛'))
async def contest_today(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    global files
    title = "今日比赛：\n"
    msg = await get_today_contest(files)
    text = (title + getText(msg)).strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('明日比赛'))
async def contest_tomorrow(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    global files
    title = "明日比赛：\n"
    msg = await get_tomorrow_contest(files)
    text = getText(msg)
    text = (title + getText(msg)).strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('opencup'))
async def contest_opencup(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    msg = await get_contest("contests.json", lambda start, end, link: "opencup" in link)
    text = "opencup:\n" + getText(msg).strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('leetcode','lc', '力扣'))
async def contest_leetcode(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    msg = await get_contest("contests.json", lambda start, end, link: "leetcode" in link)
    text = "leetcode:\n" + getText(msg).strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('ctf'))
async def contest_ctf(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    msg = await get_contest("contests.json", lambda start, end, link: any([i in link for i in ["ctftime", "hackerearth", "hackerrank"]]))
    text = "ctf:\n" + getText(msg).strip()
    await bot.finish(ev, text)


@sv.on_fullmatch(('topcoder'))
async def contest_topcoder(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    msg = await get_contest("contests.json", lambda start, end, link: "topcoder" in link)
    text = "topcoder:\n" + getText(msg).strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('atcoder', "atc"))
async def contest_atcode(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    msg = await get_contest("contests.json", lambda start, end, link: "atcoder" in link)
    text = "atcoder:\n" + getText(msg).strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('ucup'))
async def contest_ucup(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    msg = await get_contest("contests.json", lambda start, end, link: "ucup" in link)
    text = "ucup:\n" + getText(msg).strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('yukicoder', 'yuki'))
async def contest_yukicode(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    msg = await get_contest("contests.json", lambda start, end, link: "yukicoder" in link)
    text = "yukicoder:\n" + getText(msg).strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('codechef'))
async def contest_codechef(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    msg = await get_contest("contests.json", lambda start, end, link: "codechef" in link)
    text = "codechef:\n" + getText(msg).strip()
    await bot.finish(ev, message = text)

@sv.on_fullmatch(('cf', 'codeforces'))
async def contest_codeforces(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    msg = await get_contest("contests.json", lambda start, end, link: "codeforces" in link)
    text = "codeforces:\n" + getText(msg).strip()
    await bot.finish(ev, text)

@sv.on_fullmatch(('牛客'))
async def contest_niuke(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    text = "牛客:\n" 
    msg = await get_contest("niuke.json", lambda start, end, link: True)
    msg += await get_contest("niuke_school.json", lambda start, end, link: True)
    text += getText(msg).strip()
    await bot.finish(ev, text)

@sv.on_prefix('find')
async def get_cf_msg(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    name = ev.message.extract_plain_text()
    uid = ev.user_id
    msg = getCfSelfMsg(name) if len(name) < 60 else "不要捣乱哦！  [CQ:face,id=106]"
    if "超时" in msg or "无法访问" in msg:
        msg = "cf访问超时，请稍后查询qwq"
    elif "找不到" in msg:
        msg = "没找到这个人qwq"
    elif not msg.startswith("不要捣乱哦") and not msg.endswith("[CQ:face,id=15][CQ:face,id=15]"):
        msg = render_forward_msg([msg])
        await bot.send_group_forward_msg(group_id=ev.group_id, messages=msg)
        return
    msg = f"[CQ:reply,id={ev.message_id}]" + msg
    await bot.finish(ev, msg)

@sv.on_prefix('洛谷月报')
async def get_luogu_some_news(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    condition = ev.message.extract_plain_text().strip()
    if condition and '-' not in condition:
        bot.finish(ev, "请输入正确的格式:洛谷月报 xxxx-xx")
    now = datetime.now()
    year = now.year
    month = now.month
    try:
        if condition:
            year, month = map(int, condition.split('-'))
    except Exception as e:
        sv.logger.error(f'Error: {e}')
        bot.finish(ev, "不要捣乱哦")
    msg = await get_luogu_news_condition(year, month)
    msg = get_luogu_news_text(msg)
    bot.finish(ev, msg)

@sv.on_fullmatch('随机月报')
async def get_luogu_random_new(bot, ev):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.finish(ev, '您查询得过于频繁，请稍等片刻', at_sender=True)
    lmt.start_cd(uid)

    msg = await get_luogu_random_news()
    msg = get_luogu_news_text(msg)
    bot.finish(ev, msg)



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
