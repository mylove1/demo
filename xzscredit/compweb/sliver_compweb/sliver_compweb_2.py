# coding:utf-8
import time
import random
import requests
import threading
import pymongo
import re
import config


class CompWebCrawl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.agent = config.agents
        self.proxypool = proxypool

    def get_html(self, key):

        while 1:
            this_url = 'http://whois.aizhan.com/reverse-whois?q=%s&t=registrant' % key
            this_headers = {
                'User-Agent': random.choice(self.agent),
                'Host': 'whois.aizhan.com',
                'Referer': 'http://whois.aizhan.com/reverse-whois',
                'Connection': 'keep-alive',
            }
            # [use proxy]
            try:
                proxy = random.choice(self.proxypool)
                print proxy
                r = requests.post(this_url, headers=this_headers, proxies={'http': proxy}, timeout=5)
                if r.status_code != 200: continue
                break
            except:
                    print '.'
        return r.text


    def put_mess(self, mess):
        requests.post('http://'+config.master+':12222/post', data=mess)



    def get_kw(self):
        r = requests.get('http://'+config.master+':12222/comp')
        return r.text


    def run(self):
        while True:
            key = self.get_kw().encode('utf8')
            key = '华为技术有限公司'
            print key
            if key == '':
                time.sleep(10)
                continue
            html = ''.join(self.get_html(key).split())
            print html
            datas = re.findall(
                '<a href=.*?blank">(.*?)</a></div><div class="w280">(.*?)</div><div class="w280"><a href=.*?>(.*?)</a></div><div class="w100">(.*?)</div><div class="w100">(.*?)</div><div class="w70">',
                html)
            print datas
            # if datas:
            #     items = []
            #     for x in datas:
            #         item = {}
            #         item["url"] = x[0]
            #         item["name"] = x[1]
            #         item["email"] = x[2]
            #         item["starttime"] = x[3]
            #         item["endtime"] = x[4]
            #         items.append(item)
            #     # print str(items)
            #     print '---------', key, '--------------->>>>>>>>>>>>>>>'
            #     self.put_mess({"comp": str(items)})
            break




if __name__ == '__main__':
    # time.sleep(3600)
    proxypool = []
    conn = pymongo.Connection(config.master, 27017)
    db = conn.ip
    for x in db.useful.find():
        proxypool.append(x["ip"])

    for x in xrange(1):
        thread = CompWebCrawl()
        thread.start()
