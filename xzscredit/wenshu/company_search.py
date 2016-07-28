# -*- coding: utf-8 -*-
import requests
import random
import MySQLdb
import pymongo
import threading
import sys
import setting
reload(sys)
sys.setdefaultencoding('utf-8')


def get_company_list(start, stop):
    comp_list = []
    conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306, charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select name from company_zong where id between %s and %s  ;" % (start, stop))
    aa = cursor.fetchall()
    for x in aa:
        comp_list.append(x[0])
    conn.close()
    return comp_list


class wenshu(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.url = 'http://wenshu.court.gov.cn/List/ListContent'
        self.header = headers

    def get_html(self, key, page, order='裁判日期', direction='asc'):
        data = {
            'Param': "全文检索:" + key,
            'Index': page,
            'Page': '20',
            'Order': order,
            'Direction': direction,
        }
        try:
            while 1:
                while 1:
                    this_headers = {
                        'User-Agent': random.choice(headers),
                        'Referer': 'http://wenshu.court.gov.cn/List/ListContent',
                        'Connection': 'keep-alive',
                    }
                    # [use proxy]
                    # try:
                    #     proxy = random.choice(proxylist.keys())
                    #     print proxy
                    #     r = requests.post(self.url, headers=this_headers, data=data, proxies={'http': proxy}, timeout=7)
                    #     break
                    # except:
                    #     try:
                    #         print proxy, 'is bad'
                    #         proxylist.pop(proxy)
                    #     except:
                    #         pass

                    # [don't use proxy]
                    try:
                        r = requests.post(self.url, headers=this_headers, data=data, timeout=7)
                        break
                    except:
                        continue
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

    def run(self):
        print 'start run'
        while True:
            print '-  -            -   -   -  -', len(comp_list)
            try:
                key = comp_list.pop()
            except:
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
                db.insert(this_dict)
                print len(this_dict["wenshu"])


if __name__ == '__main__':
    conn = pymongo.Connection('192.168.0.100', 27017)
    db = conn.wenshu.total
    comp_list = [
        '朱浩斌',
        # '华为技术有限公司',
        # '杭州阿里巴巴广告有限公司',
    ]
    comp_list = get_company_list(1, 1000)
    headers = setting.agents
    for x in range(10):
        thread = wenshu()
        thread.start()

