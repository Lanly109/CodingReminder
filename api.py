from datetime import datetime, timedelta
import requests
from .utils import save_json

apikey = "&username=xxxx&api_key=xxxx"

url = "https://clist.by:443/api/v3/contest/?upcoming=true&filtered=true&order_by=start&format=json" + apikey

async def getContest():
    resp = requests.get(url, timeout=5)
    data = dict(resp.json())
    contests = {}
    for contest in data['objects']:
        name = contest['event']
        start_time = (datetime.strptime(contest['start'], "%Y-%m-%dT%H:%M:%S") + timedelta(hours = 8)).strftime("%Y-%m-%d %H:%M")
        end_time = (datetime.strptime(contest['end'], "%Y-%m-%dT%H:%M:%S") + timedelta(hours = 8)).strftime("%Y-%m-%d %H:%M")
        contests[name] = {
            "start_time" : start_time,
            "end_time" : end_time,
            "duration" : contest['duration'],
            "link" : contest['href']
        }
    save_json("contests.json", contests)
