import hoshino
from hoshino import Service, priv
from .utils import *

_help ='''- [@bot cf] 获取Codeforces比赛信息
- [@bot 牛客] 获取牛客比赛信息
- [@bot Codechef] 获取codechef比赛信息
- [@bot Atcoder] 获取atcoder比赛信息
- [@bot find tourist] 查找tourist cf信息
- [@bot 启动消息通知] 启动比赛提醒功能，提前一小时将比赛链接发在群上
- [@bot 取消消息通知] 停用比赛提醒功能'''

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

@sv.on_fullmatch('帮助CodingReminder')
async def tenki_help_chat(bot, ev):
    await bot.finish(ev, _help)

contest_list = load_json("contestlist.json")

group_list = load_json("group.json")