# coding=utf-8
import requests
import re
import time
from PIL import Image
import pytesseract
import threading
import pymongo
import random


FROMTIME = '2015-01-01'
TOTIME = '2015-02-01'


def proxy():
    global proxylist
    rule = [
        # [[('http://www.xicidaili.com/wn/' + str(x)) for x in range(1, 3)], '<td>((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))</td><td>(.*?)</td>'],
        [['http://www.xicidaili.com/nt'],'<td>((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))</td><td>(.*?)</td>'],
    ]

    for rangeweb in rule:
        thisrule = re.compile(rangeweb[1])
        for rangepage in rangeweb[0]:
            r = requests.get(rangepage, headers = {
                'content-type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
                'Referer': 'http://www.xicidaili.com/wn',
                })
            text = r.text
            text = ''.join(text.split())
            proxy_yuan = thisrule.findall(text)
            for every_ip in proxy_yuan:
                proxylist[every_ip[0] + ':' + every_ip[1]] = ''




class wenshu(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.url = 'http://wenshu.court.gov.cn/List/ListContent'

    def get_html(self, key, page):
        data = {
            'Param': key,
            'Index': page,
            'Page': '20',
            'Order': '审判程序',
            'Direction': 'asc',
        }
        try:
            while 1:
                global proxylist
                while 1:
                    try:

                        proxy = random.choice(proxylist.keys())
                        print proxy
                        r = requests.post(self.url, data=data, proxies={'http': proxy}, timeout=7)
                        break
                    except:
                        try:
                            print proxy, 'is bad'
                            print proxylist
                            proxylist.pop(proxy)
                        except:
                            pass
                html = r.text
                # print html
                # print html
                if len(html) != 8:
                    break
                if len(html) < 100:
                    print html
                    return '"[{\"Count\":\"0\"}]"'
            return html
        except :
            print 'except --0'
            return '"[{\"Count\":\"0\"}]"'

    def get_list(self, key, page='1'):
        print key
        html = self.get_html(key, page)
        if len(html) == 21:
            return [{"Count": "0"}]
        text = html[3:-3]
        dell = [
            'titleu0026amp;',
            '\\',
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
        ]
        for dell_l in dell:
            text = text.replace(dell_l, '')
        # print text
        l = text.split('},{')
        for enu, x in enumerate(l):
            x = "{" + x + "}"
            try:
                l[enu] = dict(eval(x))
            except:
                l.pop(enu)
        return l

    def to_db(self, l):
        global db
        for jilu in l[1:]:
            jilu["_id"] = jilu["文书ID"]
            jilu.pop("文书ID")
            if len(jilu) == 8:
                jilu["裁判要旨段原文"] = ''
            # print len(jilu)
            try:
                db.insert(jilu)
            except:
                pass
            # print "Has sent to mongo"
            # print '\n'.join(jilu.keys())
            # print jilu["文书ID"]
            print "----------->"

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
            global datalist
            try:
                key = datalist.pop()
            except:
                break
                # key = "上传日期:2012-02-01 TO 2012-02-02;法院层级:最高法院;地域:最高人民法院;裁判年份:2001"
                # # key = "法院层级:最高法院"
                # key = "上传日期:2016-02-01 TO 2016-02-02;法院层级:最高法院;审判程序:复核"
            wenshulist = self.get_list(key)
            # print wenshulist
            try:
                tiao = int(wenshulist[0]["Count"])
                print "总条数\t",tiao
            except:
                tiao = 0
            if tiao != 0:
                self.to_db(wenshulist)
                pages = self.count_page(int(wenshulist[0]["Count"]))
                if pages >1:
                    print pages
                    for page in range(2,pages+1):
                        self.to_db(self.get_list(key, str(page)))
                        print '已经好了一个了'
                        # print '已经好了一个了'
                        break


if __name__ == '__main__':
    proxylist = {
        '120.52.73.30:80': '',
    }
    proxy()
    print proxylist

    conn = pymongo.Connection('192.168.0.100', 27017)
    db = conn.wenshu.total

    fromtime = time.mktime(time.strptime(FROMTIME, "%Y-%m-%d"))
    datalist = []
    for x in range(10000):
        tup_birth = time.localtime(fromtime)
        format_birth = time.strftime("%Y-%m-%d", tup_birth)
        if not format_birth == TOTIME:
            fromtime += 86400
            for yiceng in ["最高法院",
                           "高级法院",
                           "中级法院",
                           "基层法院",
                           ""]:
                for eceng in ["最高人民法院",
                              "北京市",
                              "天津市",
                              "河北省",
                              "山西省",
                              "内蒙古自治区",
                              "辽宁省",
                              "吉林省",
                              "黑龙江省",
                              "上海市",
                              "江苏省",
                              "浙江省",
                              "安徽省",
                              "福建省",
                              "江西省",
                              "山东省",
                              "河南省",
                              "湖北省",
                              "湖南省",
                              "广东省",
                              "广西壮族自治区",
                              "海南省",
                              "重庆市",
                              "四川省",
                              "贵州省",
                              "云南省",
                              "西藏自治区",
                              "陕西省",
                              "甘肃省",
                              "青海省",
                              "宁夏回族自治区",
                              "新疆维吾尔自治区",
                              "新疆维吾尔自治区高级人民法院生产建设兵团分院",
                              "",
                              ]:
                    for sanceng in ['',
                                    '2001',
                                    '2002',
                                    '2003',
                                    '2004',
                                    '2005',
                                    '2006',
                                    '2007',
                                    '2008',
                                    '2009',
                                    '2010',
                                    '2012',
                                    '2013',
                                    '2014',
                                    '2015']:
                        for siceng in ["",
                                       "判决书",
                                       "裁定书",
                                       "调解书",
                                       "决定书",
                                       "通知书",
                                       "令",]:
                            if yiceng == '':
                                yicenginfo = ""
                            else:
                                yicenginfo = ",法院层级:"+yiceng
                            if eceng == '':
                                ecenginfo = ""
                            else:
                                ecenginfo = ",地域:"+ eceng
                            if sanceng == '':
                                sancenginfo = ""
                            else:
                                sanceng = ",地域:" + eceng
                            if siceng == '':
                                sicenginfo = ''
                            else:sicenginfo = ',文书类型:' + siceng
                            datalist.append("上传日期:" + format_birth + " TO " + time.strftime("%Y-%m-%d",time.localtime(fromtime)) + yicenginfo + ecenginfo + sancenginfo + sicenginfo)

                            # datalist.append("上传日期:" + format_birth + ";法院层级:"+yiceng + ";地域:"+ eceng + ";裁判年份:"+ str(sanceng))
        else:
            break
    print len(datalist)
    # datalist = ["上传日期:2016-02-01 TO 2016-02-02;法院层级:最高法院;审判程序:复核",
    #             "上传日期:2016-02-02 TO 2016-02-03;法院层级:最高法院;审判程序:复核",
    #             ]
    # datalist = ["上传日期:2015-01-31 TO 2015-02-01,法院层级:",
    #             ]
    for x in range(0, 1):
        a = wenshu()
        a.start()


