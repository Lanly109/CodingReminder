# 算法竞赛开赛提醒

支持[Codeforces](https://codeforces.com/),[Atcode](https://atcoder.jp),[牛客](https://ac.nowcoder.com/acm/home)平台的赛前提醒~~Codechef可能由于页面结构更改导致原来的爬虫代码解析不到信息先咕了~~

会在比赛开始前一小时将比赛信息和链接推送到群上。

代码来源于[QQ小明机器人插件](https://github.com/bobby285271/xiaoming-bot)

对服务端代码重构，适配[Hoshinobot](https://github.com/Ice-Cirno/HoshinoBot).

## 安装方法

在```HoshinoBot\hoshino\modules```目录下使用以下命令拉取本项目

```
git clone https://github.com/Lanly109/CodingReminder.git
```

进入该目录后使用如下命令安装依赖

```
cd CodingReminder
pip install -r requirements.txt
```

然后在```HoshinoBot\hoshino\config\__bot__.py```文件的```MODULES_ON```加入```CodingReminder```


## 使用方法

- @bot cf （获取Codeforces比赛信息）
- @bot 牛客 （获取牛客比赛信息）
- @bot Codechef (获取codechef比赛信息)
- @bot Atcoder(获取atcoder比赛信息)
- @bot find tourist (查找tourist cf信息) 
- @bot 启动消息通知
- @bot 取消消息通知
