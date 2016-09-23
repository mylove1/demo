# coding:utf-8
import json
import requests
import sys
import time
import warnings
warnings.filterwarnings("ignore")

reload(sys)
try:
    sys.setdefaultencoding("utf-8")
except:
    reload(sys)
    sys.setdefaultencoding("utf-8")

def piao():
    headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'kyfw.12306.cn',
    'If-Modified-Since': '0',
    'Referer': 'https://kyfw.12306.cn/otn/lcxxcx/init',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    }
    url_list = [
        "https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-10-03&from_station=AYF&to_station=GZQ",
        "https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-10-04&from_station=AYF&to_station=GZQ",
        ]

    r = requests.get(url_list[0], headers= headers, verify=False)
    dic3 = json.loads(r.text)
    for x in dic3["data"]["datas"]:
        if x["station_train_code"] == "T253":
            if x["yw_num"] == u'无' and x["rw_num"] == u'无':
                print u"3号   T253 没票"
                pass
            else:
                print time.ctime()
                if x["yw_num"] != u'无':
                    print u"3号   T253 硬卧有票：%s张" % x["yw_num"]
                if x["rw_num"] != u'无':
                    print u"3号   T253 软卧有票：%s张" % x["rw_num"]

    r = requests.get(url_list[1], headers= headers, verify=False)
    dic3 = json.loads(r.text)
    for x in dic3["data"]["datas"]:
        if x["station_train_code"] == "G531":
            if x["ze_num"] != u'无':
                print time.ctime()
                print "4号   G531 二等座有票：%s张" % x["rw_num"]
            else:
                print u"4号   G531 没票"
        if x["station_train_code"] == "G65":
            if x["ze_num"] != u'无':
                print time.ctime()
                print "4号   G65 二等座有票：%s张" % x["rw_num"]
            else:
                print u"4号   G65 没票"



if __name__ == '__main__':
    while 1:

        piao()
        time.sleep(5)