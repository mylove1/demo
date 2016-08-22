# coding:utf-8
import time
import random
import pymongo
import requests
import threading
import config
from lxml import etree


class SearchBox(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def gethtml(self, url):
        while 1:
            try:
                proxy = proxypool.pop(0)
            except:
                print 'get ip'
                proxypool.extend(requests.get("http://192.168.0.50:8384/ip/100").text.split())
                continue
            try:
                r = requests.get(url, proxies={'http': proxy}, timeout=5)
                if len(r.text) > 1000:
                    break
            except:
                print '.'
                pass
        return r.text




    def put_mess(self, mess):
        requests.post('http://'+config.master+':12111/post', data=mess)



    def get_kw(self):
        r = requests.get('http://'+config.master+':12111/comp')
        return r.text



    def run(self):
        print 'start run'
        while True:
            key = self.get_kw()
            print key
            if key == '000': break
            url = "http://www.zjcredit.gov.cn/sgs/sgsDetail.do?id=%s" % key
            print url
            html = self.gethtml(url)
            print '---', html[:30], '-------'
            print html
            tree = etree.HTML(html)
            li = tree.xpath('//table[@class="listf4"]/tr[2]/td/table/tr/td/text()')
            print len(li)
            # try:
            dic = {"id": "id", "title": li[0], "bookid": li[2], "company": li[4], "bumen": li[7], "data": li[9], "info": li[12]}
            this_dict = str(dic)
            self.put_mess({"comp": this_dict})
            # except:
            #     pass


def main():
    for x in xrange(1):
        thread = SearchBox()
        thread.start()

if __name__ == '__main__':
    proxypool = []
    main()
