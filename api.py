from datetime import datetime, timedelta
import requests
from .utils import save_json

apikey = "&username=xxxx&api_key=xxxx"

url = "https://clist.by:443/api/v3/contest/?upcoming=true&filtered=true&order_by=start&format=json" + apikey

async def getContest():
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = dict(resp.json())
    contests = []
    for contest in data['objects']:
        name = contest['event']
        start_time = (datetime.strptime(contest['start'], "%Y-%m-%dT%H:%M:%S") + timedelta(hours = 8)).strftime("%Y-%m-%d %H:%M")
        end_time = (datetime.strptime(contest['end'], "%Y-%m-%dT%H:%M:%S") + timedelta(hours = 8)).strftime("%Y-%m-%d %H:%M")
        contests.append({
            "name": name,
            "start_time" : start_time,
            "end_time" : end_time,
            "duration" : contest['duration'],
            "link" : contest['href']
        })
    save_json("contests.json", contests)

async def getLuoguYuebao():
    url = "https://www.craft.do/api/share/N0l80k2gv46Psq"
    data = requests.get(url=url, timeout=10)
    data.raise_for_status()
    data = data.json()
    tmp = {block['id']: block for block in data['blocks']}

    top = data['blocks'][0]['id']

    news = {}

    for title_id in tmp[top]['blocks']:
        title = tmp[title_id]
        if '关键词' in title['content']:
            continue
        year = int(title['content'].strip('年').strip())

        id = ""
        url = ""
        pos = 0
        up = len(title['blocks'])
        while pos < up:
            text = tmp[title['blocks'][pos]]['content']

            if '月' in text:
                month = int(text.strip('月').strip(''))
                pos += 1

                text = tmp[title['blocks'][pos]]['content'].replace('\u3000', ' ')

                while text.startswith('#'):
                    name = text
                    id = text.split(' ')[0]
                    pos += 1
                    url = tmp[title['blocks'][pos]]['content']
                    news[id] = {'title': name, 'url': url, 'year': year, 'month': month}
                    pos += 1
                    if pos >= up:
                        break
                    text = tmp[title['blocks'][pos]]['content'].replace('\u3000', ' ')
            else:
                pos += 1


    save_json("luogu_news.json", news)

