# coding:utf-8
import re
import requests
import pymongo
import threading




class ShuangGongshi(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.data = {"id2": ''}
        self.rea = re.compile('id=(.*?)"')
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }

    def run(self):
        urllist = ["http://www.zjcredit.gov.cn/page/sgs/sgsProxy.jsp?startrecord=",
                   "1171388",
                   "&endrecord=",
                   "1172400",
                   "&perpage=8&totalRecord=1172400"]
        url = ''.join(urllist)
        print url


        r = requests.post(url, headers=self.headers, data=self.data, timeout=7)
        list = self.rea.findall(r.text)


        for x in list:
            print x

proxypool = []
conn = pymongo.Connection("192.168.0.50", 27017)
db = conn.xinyongzhejiang
pagelist = [x for x in xrange(1, 1172)]
for thr in xrange(1):
    thread = ShuangGongshi()
    thread.start()
