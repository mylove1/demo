# coding:utf-8
import time
import urllib
import random
import pymongo
import requests
import threading
import re
import config


class ShangbiaoCrawl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.agent = config.agents
        self.proxypool = proxypool

    def get_html(self, url):
        while 1:
            this_headers = {
                'User-Agent': random.choice(self.agent),
                'Host': 'sbcx.saic.gov.cn:9080',
                'Connection': 'keep-alive',
            }
            try:
                proxy = random.choice(self.proxypool)
                r = requests.get(url, headers=this_headers, proxies={'http': proxy}, timeout=5)
                break
            except:
                print '.'
                pass
        return ''.join(r.text.split())

    def put_mess(self, mess):
        requests.post('http://192.168.100.55:12121/post', data=mess)

    def get_kw(self):
        r = requests.get('http://192.168.100.55:12121/comp')
        return r.text

    def run(self):
        while True:
            key = self.get_kw().encode('utf8')
            # key = '华为技术有限公司'
            print key
            if key == '':
                time.sleep(10)
                continue
            key = urllib.quote(key).replace('%', '%25')
            url = 'http://sbcx.saic.gov.cn:9080/tmois/wszhcx_getLikeCondition.xhtml?appCnName=' + key + '&intCls=&paiType=0'
            html = self.get_html(url)
            # print html
            datas = re.findall(
                '<tr>.*?><ahref.*?>(.*?)</a>.*?<ahref.*?>(.*?)</a>.*?<ahref.*?>(.*?)</a>.*?<ahref.*?>(.*?)</a>', html)
            if datas:
                items = []
                for x in datas:
                    item = {}
                    item["company"] = x[3]
                    item["number"] = x[0]
                    item["type"] = x[1]
                    item["name"] = x[2]
                    items.append(item)
                # print str(items)
                self.put_mess({"comp": str(items)})



def main():
    for x in xrange(5):
        thread = ShangbiaoCrawl()
        thread.start()

if __name__ == '__main__':
    proxypool = []
    conn = pymongo.Connection("192.168.100.55", 27017)
    db = conn.ip
    for x in db.useful.find():
        proxypool.append(x["ip"])
    main()
