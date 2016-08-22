# coding:utf-8
import requests
import json
import pymongo
import config
import threading





class ShuangGongshi(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.agent = config.agents
        # 行政许可
        # self.url = "http://www.xyhn.gov.cn:8000/cms/xzxklist"
        # 行政处罚
        self.url = "http://www.xyhn.gov.cn:8000/cms/xzcflist"
        self.headers = {
    'Accept': 'application/json, text/javascript, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '18',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.xyhn.gov.cn:8000',
    'Origin': 'http://www.xyhn.gov.cn',
    'Referer': 'http://www.xyhn.gov.cn/ca/20160422000005.htm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}


    def run(self):
        while True:
            try:
                page = pagelist.pop(0)
            except:
                break
            data = {
                'page': str(page),
                'pageSize': '50'
            }

            r = requests.post(self.url, headers=self.headers, data=data)
            text = r.text
            text = json.loads(text)
            print '\\\\\\'
            for x in text["data"]:
                db.xzcf.insert(x)
            print '------------->    ', page

conn = pymongo.Connection(config.master, 27017)
db = conn.xinyonghenan
pagelist = [x for x in xrange(1, 806)]
for thr in xrange(10):
    thread = ShuangGongshi()
    thread.start()

