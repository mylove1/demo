# coding:utf-8
import requests
import threading
import re
import pybloom
import time
import random
import pymongo
import config



# headers = {
#     "Host": "gsxt.zjaic.gov.cn",
#     "Referer": "http://gsxt.zjaic.gov.cn/unusualcatalog/doReadUnusualCatalogList.do",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
# }
#
# url = "http://gsxt.zjaic.gov.cn/unusualcatalog/doReadUnusualCatalogListJSON.do?_id=doReadCatalogList1471058567706"
# data = {
#     "qryParam": "",
#     "pagination.currentPage": "1",
#     "pagination.pageSize": "10",
# }
# r = requests.post(url, data, headers=headers)
# print r.text
# text = r.text
# li = re.findall('''{"catRegNo":"(.*?)","corpid":"(.*?)","catRemark":".*?","catNo":"(.*?)","canOutReaCodeName":".*?","catState":".*?","catEntName":"(.*?)","catOrgName''', text)
# for x in li:
#     pagedict = {}
#     pagedict["catRegNo"] = x[0]
#     pagedict["corpid"] = x[1]
#     pagedict["catNo"] = x[2]
#     pagedict["catEntName"] = x[3]
#     db.yichanglist.insert(pagedict)


class YichangCrawl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.agent = config.agents
        self.url = "http://gsxt.zjaic.gov.cn/unusualcatalog/doReadUnusualCatalogListJSON.do?_id=doReadCatalogList"
        self.useragent = config.agents
        self.proxypool = proxypool

    def get_html(self, key):
        data = {
            "qryParam": "",
            "pagination.currentPage": key,
            "pagination.pageSize": "10",
        }

        headers = {
            "Host": "gsxt.zjaic.gov.cn",
            "Referer": "http://gsxt.zjaic.gov.cn/unusualcatalog/doReadUnusualCatalogList.do",
            "User-Agent": random.choice(self.useragent)
        }


        while 1:
            # [use proxy]
            try:
                url = ''.join([self.url, ''.join(str('%.3f' % time.time()).split('.'))])
                proxy = random.choice(self.proxypool)
                r = requests.post(url, headers=headers, data=data, proxies={'http': proxy}, timeout=5)
                html = r.text

                if html[:2] != '{"': continue
                break
            except:
                print '...'
        return html

    def run(self):
        while True:
            try:
                key = pagelist.pop(0)
            except:
                break
            print key

            html = self.get_html(key)
            li = re.findall('''{"catRegNo":"(.*?)","corpid":"(.*?)","catRemark":".*?","catNo":"(.*?)","canOutReaCodeName":".*?","catState":".*?","catEntName":"(.*?)","catOrgName''',html)
            for x in li:
                pagedict = {}
                pagedict["catRegNo"] = x[0]
                pagedict["corpid"] = x[1]
                pagedict["catNo"] = x[2]
                pagedict["catEntName"] = x[3]
                db.yichanglist.insert(pagedict)
            print '-------------->', key
            db.listhaved.insert({"page": key})


if __name__ == '__main__':

    proxypool = []
    conn = pymongo.Connection(config.master, 27017)
    db = conn.ip
    for x in db.useful.find():
        proxypool.append(x["ip"])

    db = conn.zhejiang
    pagelist = [x for x in xrange(1, 18732)]
    for x in db.listhaved.find():
        pagelist.remove(x["page"])
    print 'total',len(pagelist), 'pages'
    for x in range(20):
        thread = YichangCrawl()
        thread.start()
