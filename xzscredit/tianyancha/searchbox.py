# coding:utf-8
import requests
import threading
import random
import config
import pybloom

# with open('C:\Users\cooper\Documents\data\comp_name.fil', 'rb') as bf:
#     f = pybloom.BloomFilter.fromfile(bf)


class SearchBox(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.kw = '杭州银行股份有限公司'

    def get_html(self):
        while 1:
            this_headers = {
                'User-Agent': random.choice(config.agents),
                'Referer': 'http://www.tianyancha.com',
                'Connection': 'keep-alive',
            }
            print this_headers
            url = ['http://www.tianyancha.com/suggest/', self.kw, '.json']
            try:
                proxy = requests.get('http://192.168.0.100:8384/ip').text
                r = requests.get(''.join(url), headers=this_headers, proxies={'http': proxy}, timeout=5)
                break
            except:
                pass
        r.encoding = 'utf8'
        return r.text

    def run(self):
        print self.get_html()



if __name__ == '__main__':
    a = SearchBox()
    a.start()
