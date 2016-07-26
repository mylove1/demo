# coding=utf-8
import requests
import re
import time
from PIL import Image
import pytesseract
import threading

FROMTIME = '2012-02-01'
TOTIME = '2013-01-01'

class wenshu(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.url = 'http://wenshu.court.gov.cn/List/ListContent'

    def get_html(self, key, page):
        data = {
            'Param': key,
            'Index': page,
            'Page': '5',
            'Order': '法院层级',
            'Direction': 'asc',
        }
        try:
            while 1:
                r = requests.post(self.url, data=data)
                html = r.text
                # print html
                if len(r.text) != 8:
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
                pass
        return l
        # # 计算页数
        # jishudict = "{" + l[0] + "}"
        # print jishudict
        # # 尝试转换第一个计数字典
        # countdict = dict(eval(jishudict))
        # totalcount = int(countdict["Count"])
        # pages = totalcount/20
        # if totalcount % 20 > 0:
        #     pages += 1


        # 对一个页面的各个文件迭代
        # for x in l[1:]:
        #     x = "{" + x + "}"
        #     # print x
        #     # 尝试转换每个文件为字典
        #     d = dict(eval(x))
        #     print d.keys()[0]
        #     # 打印在页面上
        #     for key in d.keys():
        #         print key + '\t:\t' + d[key]
        #     # 接下来可以存入数据库
        #     # for key in d.keys():
        #     #     print key + '\t:\t' + d[key]
        #     break
        # return 0
    def to_db(self, l):
        for jilu in l[1:]:
            print jilu["文书ID"]

    def count_page(self, num):
        pages = num /20
        if num % 20 > 0:
            pages += 1
        if pages > 25:
            pages = 25
        return pages

    def run(self):
        key = "上传日期:2012-02-01 TO 2012-02-02;法院层级:最高法院;地域:最高人民法院;裁判年份:2001"
        # key = "法院层级:最高法院"
        key = "上传日期:2016-02-01 TO 2016-02-02;法院层级:最高法院;审判程序:复核"
        wenshulist = self.get_list(key)
        self.to_db(wenshulist)
        pages = self.count_page(int(wenshulist[0]["Count"]))
        if pages >1:
            print pages
            for page in range(2,pages+1):
                self.to_db(self.get_list(key, str(page)))
                print '已经好了一个了，算了吧'
                print '已经好了一个了，接着来'
                # break



if __name__ == '__main__':
    # fromtime = time.mktime(time.strptime(FROMTIME, "%Y-%m-%d"))
    # datalist = []
    # for x in range(10000):
    #     tup_birth = time.localtime(fromtime)
    #     format_birth = time.strftime("%Y-%m-%d", tup_birth)
    #     if not format_birth == TOTIME:
    #         fromtime += 86400
    #         for yiceng in ["最高法院",
    #                        "高级法院",
    #                        "中级法院",
    #                        "基层法院"]:
    #             for eceng in ["最高人民法院",
    #                           "北京市",
    #                           "天津市",
    #                           "河北省",
    #                           "山西省",
    #                           "内蒙古自治区",
    #                           "辽宁省",
    #                           "吉林省",
    #                           "黑龙江省",
    #                           "上海市",
    #                           "江苏省",
    #                           "浙江省",
    #                           "安徽省",
    #                           "福建省",
    #                           "江西省",
    #                           "山东省",
    #                           "河南省",
    #                           "湖北省",
    #                           "湖南省",
    #                           "广东省",
    #                           "广西壮族自治区",
    #                           "海南省",
    #                           "重庆市",
    #                           "四川省",
    #                           "贵州省",
    #                           "云南省",
    #                           "西藏自治区",
    #                           "陕西省",
    #                           "甘肃省",
    #                           "青海省",
    #                           "宁夏回族自治区",
    #                           "新疆维吾尔自治区",
    #                           "新疆维吾尔自治区高级人民法院生产建设兵团分院",
    #                           ]:
    #                 for sanceng in range(2001,2013):
    #                     datalist.append({"Param":"上传日期:" + format_birth + " TO " + time.strftime("%Y-%m-%d",time.localtime(fromtime)) + ";法院层级:"+yiceng + ";地域:"+ eceng + ";裁判年份:"+ str(sanceng)})
    #     else:
    #         break
    # print len(datalist)
    # print datalist[0]["Param"]
    a = wenshu()
    a.start()


