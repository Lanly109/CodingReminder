import hoshino
from hoshino import Service, priv
from .utils import *

_help ='''- 输入以下关键字获得比赛咨询：cf 牛客 atcoder ucup yukicoder leetcode codechef topcoder ctf
- [今日比赛] 获取今日未举行的比赛
- [明日比赛] 获取明日比赛
- [当前比赛] 获取当前进行的比赛
- [find tourist] 查找tourist cf信息
- [@bot 启动比赛通知] 启动比赛提醒功能，提前一小时将比赛链接发在群上
- [@bot 取消比赛通知] 停用比赛提醒功能'''

sv = Service(
    name = '算法竞赛开赛提醒',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #False隐藏
    enable_on_default = True, #是否默认启用
    bundle = '订阅', #属于哪一类
    help_ = _help #帮助文本
    )

bot = hoshino.get_bot()

@sv.on_fullmatch('帮助比赛提醒')
async def tenki_help_chat(bot, ev):
    await bot.finish(ev, _help)

group_list = load_json("group.json")

files = ["contests.json", "niuke.json", "niuke_school.json"]
