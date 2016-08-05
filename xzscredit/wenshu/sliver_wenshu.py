# coding:utf-8
import time
import random
import requests
import threading
import config
import json


class SearchBox(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.agent = config.agents
        self.url = 'http://wenshu.court.gov.cn/List/ListContent'

    def get_html(self, key, page, order='裁判日期', direction='asc'):
        data = {
            'Param': u"全文检索:" + key,
            'Index': page,
            'Page': '20',
            'Order': order,
            'Direction': direction,
        }
        try:
            while 1:
                while 1:
                    this_headers = {
                        'User-Agent': random.choice(self.agent),
                        'Referer': 'http://wenshu.court.gov.cn/List/ListContent',
                        'Connection': 'keep-alive',
                    }
                    # [use proxy]
                    try:
                        # proxy = requests.get('http://192.168.0.100:8384/ip').text
                        r = requests.post(self.url, headers=this_headers, data=data, proxies={'http': '119.6.136.122:83'}, timeout=7)
                        break
                    except:
                        pass


                html = r.text
                # print html
                lonth = len(html)
                if lonth == 8:
                    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                    continue
                elif lonth == 21:
                    return html
                elif lonth < 100:
                    print html
                    return '"[{\"Count\":\"0\"}]"'
                else:
                    break
            return html
        except :
            print 'except --0'
            return '"[{\"Count\":\"0\"}]"'

    def get_list(self, key, page='1'):
        html = self.get_html(key, page)
        if len(html) == 21:
            return [{"Count": "0"}]
        text = html[3:-3]
        # print text
        dell_1 = [
            '\\n',
            '\\',]
        dell_2 = [
            '/u003e',
            'u003cbr',
            '&nbsp;',
            'titleu0026amp;',
            '/',
            '&amp;#xA;',
            'title&amp;',
            'gt;',
            'u0026amp;',
            '#xA;',
            'lt;',
            '&amp;lt;',
            '&amp;',
            'p&amp;',
            'pp',
            'amp;',
            'nbsp;',
            'times;',
            '&',
            'u0026',
            'lang="EN-US"',
            'u003cspan',
            'u003cb',
        ]
        for dell in dell_1:
            text = text.replace(dell, '')
        l = text.split('},{')
        for enu, x in enumerate(l):
            x = "{" + x + "}"
            # 尝试转换为字典形式，如果出错则对文本进行严格的替换，再不行就返回空值
            try:
                l[enu] = dict(eval(x))
            except:
                for dell in dell_2:
                    text = text.replace(dell, '')
                l = text.split('},{')
                for enu, x in enumerate(l):
                    x = "{" + x + "}"
                    # l[enu] = dict(eval(x))
                    try:
                        l[enu] = dict(eval(x))
                    except:
                        l[enu] = {}
        return l

    def insert_dict(self, dict, list):
        for jilu in list[1:]:
            if jilu != {}:
                dict["wenshu"].append(jilu)

    def count_page(self, num):
        pages = num /20
        if num % 20 > 0:
            pages += 1
        if pages > 25:
            pages = 25
        return pages

    def put_mess(self, mess):
        requests.post('http://192.168.0.100:12315/post', data=mess)

    def get_kw(self):
        r = requests.get('http://192.168.0.100:12315/comp')
        return r.text

    def run(self):
        print 'start run'
        while True:
            key = self.get_kw()
            # key = '上海金茂建筑装饰有限公司与孙开华'
            print key
            if key == '':
                print 'Done'
                break
            wenshulist = self.get_list(key)
            try:
                tiao = int(wenshulist[0]["Count"])
                print "total\t", tiao
            except:
                tiao = 0
            if tiao > 0:
                this_dict = {
                    "company": key,
                    "count": tiao,
                    "wenshu": []
                }
                self.insert_dict(this_dict, wenshulist)
                for jilu in wenshulist[1:]:
                    this_dict["wenshu"].append(jilu)
                if tiao > 20:
                    pages = self.count_page(tiao)
                    for page in range(2, pages + 1):
                        print '---', key, '---', page
                        wenshulist = self.get_list(key, page)
                        self.insert_dict(this_dict, wenshulist)
                this_dict = str(this_dict)
                self.put_mess({"comp": this_dict})
def main():
    for x in xrange(10):
        thread = SearchBox()
        thread.start()

if __name__ == '__main__':
    main()
