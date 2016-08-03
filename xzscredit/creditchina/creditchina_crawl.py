# coding:utf-8
'''input a comppany keyword,then output a data that json type.'''
import requests
import random
import config
import time
import json
print ''.join(str('%.3f' % time.time()).split('.'))


class CreditChina(object):
    def __init__(self, kw):
        self.kw = kw
        self.data = {
            'keyword': self.kw,
            'searchtype': 0,
            'objectType': 2,
            'areas': '',
            'creditType': '',
            'dataType': 1,
            'areaCode': '',
            'templateId': '',
            'exact': 0,
            'page': 1
        }
        self.headers = {
            'User-Agent': random.choice(config.agents),
            'Referer': 'http://www.creditchina.gov.cn/',
            'Connection': 'keep-alive',
        }
    def posthtml(self):
        url = 'http://www.creditchina.gov.cn/credit_info_search?t=' + ''.join(str('%.3f' % time.time()).split('.'))
        while 1:
            try:
                proxy = requests.get('http://192.168.0.100:8384/ip').text
                print proxy
                r = requests.post(url, data=self.data, headers=self.headers, timeout=5, proxies={'http': proxy},)
                break
            except:
                pass
        html = r.text
        return html

    def search_kw(self):

        a = self.posthtml()
        print a
        try:
            j = json.loads(a)
            encryStr = j["result"]["results"][0]["encryStr"]
            return encryStr
        except:
            return ''

    def gethtml(self, url):
        while 1:
            try:
                proxy = requests.get('http://192.168.0.100:8384/ip').text
                r = requests.get(url, headers=self.headers, timeout=5, proxies={'http': proxy},)
                break
            except:
                pass
        html = r.text
        return html

    def info_page(self):
        encryStr = self.search_kw()
        url = 'http://www.creditchina.gov.cn/credit_info_detail?objectType=2&encryStr=' + encryStr
        if encryStr:
            html = ''.join(self.gethtml(url).split())
            print html

        else:
            return None

    def resolve(self, html):
        pass

k = '江苏华飞建设集团有限公司'
a = CreditChina(k)

a.info_page()


