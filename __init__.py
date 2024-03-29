import hoshino
from hoshino import Service, priv
from .utils import *

_help ='''- 输入以下关键字获得比赛咨询：cf 牛客 atcoder ucup yukicoder leetcode codechef topcoder ctf
- [今日比赛] 获取今日未举行的比赛
- [明日比赛] 获取明日比赛
- [当前比赛] 获取当前进行的比赛
- [find tourist] 查找tourist cf信息
- [洛谷月报 xxxx-xx] 获得xxxx年xx月的洛谷月报，省略则获得最新月报
- [随机月报] 随机获得一份洛谷月报
还可以开启开赛提醒+leetcode每日一题服务'''

sv_info = Service(
    name = '比赛查询',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #False隐藏
    enable_on_default = False, #是否默认启用
    bundle = '查询', #属于哪一类
    help_ = _help #帮助文本
    )

sv_cron = Service(
    name = '比赛开赛提醒',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #False隐藏
    enable_on_default = False, #是否默认启用
    bundle = '订阅', #属于哪一类
    help_ = _help #帮助文本
    )

sv_lt = Service(
    name = 'leetcode每日一题',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #False隐藏
    enable_on_default = False, #是否默认启用
    bundle = '订阅', #属于哪一类
    help_ = _help #帮助文本
    )

bot = hoshino.get_bot()

@sv_info.on_fullmatch(('帮助比赛提醒', '算法竞赛开赛提醒'))
async def tenki_help_chat(bot, ev):
    await bot.finish(ev, _help)

files = ["contests.json", "niuke.json", "niuke_school.json"]
