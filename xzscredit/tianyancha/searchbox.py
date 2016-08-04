# coding:utf-8
import requests
import threading
import random
import MySQLdb
import config
import pybloom




class SearchBox(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def get_html(self, kw):
        while 1:
            this_headers = {
                'User-Agent': random.choice(config.agents),
                'Referer': 'http://www.tianyancha.com',
                'Connection': 'keep-alive',
            }
            url = ['http://www.tianyancha.com/suggest/', kw, '.json']
            try:
                proxy = requests.get('http://192.168.0.100:8384/ip').text
                r = requests.get(''.join(url), headers=this_headers, proxies={'http': proxy}, timeout=5)
                html = r.text
                if html[0:5] != '{"sta':
                    continue
                break
            except:
                pass
        r.encoding = 'utf8'
        return r.text

    def run(self):
        while 1:
            try:
                kw = kwlist.pop(0)
            except:
                break
            print self.get_html()



if __name__ == '__main__':
    # kwlist = []
    # conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306, charset="utf8")
    # cursor = conn.cursor()
    # a = 1
    # b = 1000000
    # cursor.execute("select name from company_zong where id between %s and %s  ;" % (a, b))
    # aa = cursor.fetchall()
    # for x in aa:
    #     kwlist.append(x)


    # with open('C:\Users\cooper\Documents\data\comp_name.fil', 'rb') as bf:
    #     f = pybloom.BloomFilter.fromfile(bf)
    kwlist = ["杭州银行股份有限公司"]
    a = SearchBox()
    a.start()
