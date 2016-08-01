# -*- coding: utf-8 -*-
import requests
import random
import MySQLdb
import pymongo
import threading
import sys
import time
import setting
import re

reload(sys)
sys.setdefaultencoding('utf-8')


# def get_company_list(start, stop):
#     comp_list = []
#     conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306, charset="utf8")
#     cursor = conn.cursor()
#     cursor.execute("select name from company_zong where id between %s and %s  ;" % (start, stop))
#     aa = cursor.fetchall()
#     for x in aa:
#         comp_list.append(x[0])
#     return comp_list


class chinaz(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.url = 'http://whois.chinaz.com/reverse'
        self.header = headers

    def get_html(self, key, page=1):
        data = {
            'ddlSearchMode': '2',
            'host': key,
               }
        if page != 1:
            data["page"] = page

        while 1:
            this_headers = {
                'User-Agent': random.choice(headers),
                'Referer': 'http://whois.chinaz.com',
                'Connection': 'keep-alive',
            }
            # [use proxy]
            # try:
            #     proxy = random.choice(proxy_pool.keys())
            #     print proxy
            #     r = requests.post(self.url, headers=this_headers, data=data, proxies={'http': proxy}, timeout=7)
            #     break
            # except:
            #     try:
            #         print proxy, 'is bad'
            #         proxy_pool.pop(proxy)
            #     except:
            #         pass

            # [don't use proxy]
            try:
                r = requests.post(self.url, headers=this_headers, data=data, timeout=7)
                break
            except:
                continue

        html = r.text
        return html

    def get_list(self, key, page=1):
        html = self.get_html(key, page)
        print html
        reweburl = re.compile('<a href=.*?blank">(.*?)</a></div><div class="w280">(.*?)</div><div class="w280"><a href=.*?>(.*?)</a></div><div class="w100">(.*?)</div><div class="w100">(.*?)</div><div class="w70">')
        weburllist = reweburl.findall(html)
        return weburllist

    def count_page(self, num):
        pages = num / 20
        if num % 20 > 0:
            pages += 1
        if pages > 25:
            pages = 25
        return pages

    def to_db(self, weburllist):
        for x in weburllist:
            try:
                cursor.execute("insert into weburl(weburl_url,weburl_name,weburl_email,weburl_starttime,weburl_endtime)values('%s','%s','%s','%s','%s');" % (x[0], x[1], x[2], x[3], x[4]))
                conn.commit()
            except MySQLdb.Error, e:
                print 'Error %d %s' % (e.args[0], e.args[1])


    def run(self):
        while True:
            print '-  -            -   -   -  -', len(comp_list)
            try:
                key = comp_list.pop(0)
                # key = '华为技术有限公司'
            except:
                break
            html = self.get_html(key)
            if '>暂无相关数据' in html:
                print key, '\t\t\tnot'
            elif '>查询过于频繁。' in html:
                print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
            else:
                print key, '\t\t\thave'
                weburllist = re.findall('<a href=.*?blank">(.*?)</a></div><div class="w280">(.*?)</div><div class="w280"><a href=.*?>(.*?)</a></div><div class="w100">(.*?)</div><div class="w100">(.*?)</div><div class="w70">', html)
                self.to_db(weburllist)
                try:
                    pages = re.findall(u'共(.*?)页，到第', html)[0]
                    pages = int(pages)
                    if pages > 1:
                        for page in range(2, pages + 1):
                            print '---', key, '---', page
                            weburllist = self.get_list(key, page)
                            self.to_db(weburllist)
                except:
                    pass


def get_proxy(proxy_pool, db):
    while True:
        if len(proxy_pool) < 500:
            print len(proxy_pool)
            req = requests.get('http://192.168.0.100:8000/ip.html')
            for x in req.text.split():
                proxy_pool[x] = ''

        break
        time.sleep(20)


def get_proxy(proxy_pool, db):
    while True:
        if len(proxy_pool) < 500:
            print len(proxy_pool)
            req = requests.get('http://qsrdk.daili666api.com/ip/?')

            iplist = req.text.split('\n')
            for x in iplist:
                d = {'ip': x}
                db.insert(d)
                proxy_pool.append(x)
        time.sleep(20)


def proxy():
    global proxy_pool
    rule = [
        ['http://www.youdaili.net/Daili/guonei/4766.html',
         r'<br/>((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))):(.*?)'],
        # ['http://www.xicidaili.com/wn/22', r'<td>((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))</td><td>(.*?)</td>'],
    ]

    for rangeweb in rule:
        thisrule = re.compile(rangeweb[1])
        r = requests.get(rangeweb[0], headers={
            'content-type': 'application/json',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )',
        })
        text = r.text
        text = ''.join(text.split())
        proxy_yuan = thisrule.findall(text)
        for every_ip in proxy_yuan:
            proxy_pool[every_ip[0] + ':' + every_ip[1]] = ''


if __name__ == '__main__':
    start = 1
    stop = 1000
    comp_list = []
    conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306, charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select name from company_zong where id between %s and %s  ;" % (start, stop))
    aa = cursor.fetchall()
    for x in aa:
        comp_list.append(x[0])
    comp_list.append('华为技术有限公司')

    # conn = pymongo.Connection('192.168.0.100', 27017)
    # db = conn.test.total
    # dbip = conn.ip.proxy
    # comp_list = [
    #     '朱浩斌',
    #     '华为技术有限公司',
    #     '杭州阿里巴巴广告有限公司',
    # ]

    # comp_list = get_company_list(1, 2)
    headers = setting.agents
    # proxy_pool = {}

    # proxy()
    # print len(proxy_pool)
    # time.sleep(5)
    # print len(proxy_pool)
    # ipthread = threading.Thread(target=proxy)
    # ipthread.start()

    # print 'hello'

    # ipthread = threading.Thread(target=get_proxy, args=(proxy_pool, dbip))
    # ipthread.start()
    # print 'hello'


    for x in range(1):
        thread = chinaz()
        thread.start()

