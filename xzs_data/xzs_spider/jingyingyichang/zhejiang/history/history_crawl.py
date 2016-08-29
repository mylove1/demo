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
        while True:
            try:
                page = pagelist.pop(0)
                print page
            except:
                break
            urllist = ["http://www.zjcredit.gov.cn/page/sgs/sgsProxy.jsp?startrecord=",
                       str(1 + (1000 * (page - 1))),
                       "&endrecord=",
                       str(page * 1000),
                       "&perpage=8&totalRecord=1155093"]
            url = ''.join(urllist)
            print url
            while 1:
                try:
                    try:
                        proxy = proxypool.pop(0)
                    except:
                        proxypool.extend(requests.get("http://192.168.0.50:8384/ip/100").text.split())
                        continue
                    r = requests.post(url, headers=self.headers, data=self.data, timeout=7, proxies={"http":proxy})
                    list = self.rea.findall(r.text)
                    if len(list) > 500: break
                except:
                    print '---'
                    pass

            for x in list:
                db.chufaideid.insert({"id": x})
            print '------------->    ', page

proxypool = []
conn = pymongo.Connection("192.168.0.50", 27017)
db = conn.xinyongzhejiang
pagelist = [x for x in xrange(1, 1172)]
for thr in xrange(10):
    thread = ShuangGongshi()
    thread.start()
