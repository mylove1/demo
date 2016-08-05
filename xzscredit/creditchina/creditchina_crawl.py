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
            'searchtype': '0',
            'objectType': '2',
            'areas': '',
            'creditType': '',
            'dataType': '1',
            'areaCode': '',
            'templateId': '',
            'exact': '0',
            'page': '1'
        }
        self.headers = {
            'User-Agent': random.choice(config.agents),
            'Referer': 'http://www.creditchina.gov.cn/',
            'Connection': 'keep-alive',
        }

        self.headers = {
            'Accept': 'text / plain, * / *;
        q = 0.01
        Accept - Encoding:gzip, deflate
        Accept - Language:zh - CN, zh;
        q = 0.8
        Connection:keep - alive
        Content - Length:191
        Content - Type:application / x - www - form - urlencoded;
        charset = UTF - 8
        Cookie:Hm_lvt_0076fef7e919d8d7b24383dc8f1c852a = 1470189660, 1470191545, 1470374349;
        Hm_lpvt_0076fef7e919d8d7b24383dc8f1c852a = 1470374372
        Host:www.creditchina.gov.cn
        Origin:http: // www.creditchina.gov.cn
        Referer:http: // www.creditchina.gov.cn / search_all
        User - Agent:Mozilla / 5.0(Windows
        NT
        6.1;
        WOW64) AppleWebKit / 537.36(KHTML, like
        Gecko) Chrome / 50.0
        .2661
        .102
        Safari / 537.36
        X - Requested - With:XMLHttpRequest
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

k = '平顶山市科远网络'
a = CreditChina(k)
print a.posthtml()
# a.info_page()


