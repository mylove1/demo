# coding:utf-8
'''input a comppany keyword,then output a data that json type.'''
import requests
import threading
import random
import pymongo
import time
import json
import infocrawl



class CreditChina(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


        self.headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '173',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.creditchina.gov.cn',
    'Origin': 'http://www.creditchina.gov.cn',
    'Referer': 'http://www.creditchina.gov.cn/search_all',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
    def posthtml(self, kw, page=1):
        url = 'http://www.creditchina.gov.cn/credit_info_search?t=' + ''.join(str('%.3f' % time.time()).split('.'))
        data = {
            'keyword': kw,
            'searchtype': '0',
            'objectType': '2',
            'areas': '',
            'creditType': '',
            'dataType': '1',
            'areaCode': '',
            'templateId': '',
            'exact': '0',
            'page': page,
        }
        while 1:
            try:
                proxy = proxypool.pop(0)
            except:
                proxypool.extend(requests.get("http://" + MASTERIP +":8384/ip/100").text.split())
                continue
            try:
                r = requests.post(url, data=data, headers=self.headers, timeout=5, proxies={'http': proxy},)
                if r.text[:9] == '{"result"': break
            except:
                print '_'
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
                try:
                    proxy = proxypool.pop(0)
                except:
                    proxypool.extend(requests.get("http://' + MASTERIP +':8384/ip/100").text.split())
                    continue
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

    def put_mess(self, dict):
        this_html = self.gethtml("http://www.creditchina.gov.cn/credit_info_detail?objectType=%s&encryStr=%s" %(dict["objectType"],dict["encryStr"][:-1]))
        a = infocrawl.CreditChinaInfo(this_html)
        info = a.info()
        mess = {"comp": json.dumps({"name": dict["name"], "area": dict["area"], "encryStr": dict["encryStr"][:-1], "objectType": dict["objectType"], "info": info})}
        # mess = json.loads(mess)
        requests.post('http://' + MASTERIP + ':12333/post', data=mess)
        print '--------------------------------------->>>'


        # requests.post('http://' + MASTERIP +':12333/post', data=mess)



    def get_kw(self):
        r = requests.get('http://' + MASTERIP +':12333/comp')
        return r.text

    def resolve(self, dic):
        if dic:
            for j in dic:
                self.put_mess(j)
        else:
            print 'o'

    def run(self):
        while 1:
            # kw = '平煤神马建工集团'
            # kw = '平顶山市科远网络技术有限公司'
            kw = self.get_kw()
            try:
                print kw
            except: pass

            jlist = json.loads(self.posthtml(kw))
            self.resolve(jlist["result"]["results"])
            for page in range(2, (jlist["result"]["totalPageCount"]) + 1):
                print '-------------------------------page-----', page
                jlist = json.loads(self.posthtml(kw, page))
                self.resolve(jlist["result"]["results"])

if __name__ == '__main__':
    MASTERIP = '192.168.0.50'
    proxypool = []
    conn = pymongo.Connection(MASTERIP, 27017)
    db = conn.creditchina
    for thread in range(5):
        a = CreditChina()
        a.start()
    # a.info_page()


