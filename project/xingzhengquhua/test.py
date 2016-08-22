# coding:utf-8
import requests
import time
import re
import pymongo
import random
import json


def url_list(url, rer):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    while 1:
        try:
            r = requests.post(url, headers=headers)
            r.encoding = 'gbk'
            rea = re.compile(rer)
            return rea.findall(r.text)
        except:
            print url
            continue

if __name__ == '__main__':
    total_sheng = 0
    total_shi = 0
    total_xian = 0
    total_zhen = 0
    total_cun = 0

    conn = pymongo.Connection("192.168.0.50", 27017)
    db = conn.xingzheng

    codelist = []
    url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/index.html'

    # link name
    shenglist = url_list(url, "<td><a href='(.*?)'>(.*?)<br/></a></td>")
    for shengji in shenglist:
        total_sheng += 1
        head = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/'
        shengname = shengji[1]
        shengcode = shengji[0][:2]
        db.sheng.insert(
            {"shengname": shengname, "shengcode": shengcode})
        shengurl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/' + shengji[0]
        # link code name
        shilist = url_list(shengurl, "class='citytr'><td><a href='(.*?)'>(.*?)</a></td><td><a href='.*?'>(.*?)</a></td></tr>")
        for shiji in shilist:
            total_shi += 1
            head = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/'

            shiname = shiji[2]
            shicode = shiji[1]

            db.shi.insert(
                {"shengname": shengname, "shengcode": shengcode, "shiname": shiname, "shicode": shicode})

            shiurl = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/' + shiji[0]
            # link code name
            xianlist = url_list(shiurl, "<tr class='countytr'><td><a href='(.*?)'>(.*?)</a></td><td><a href='.*?'>(.*?)</a></td></tr>")
            for xianji in xianlist:
                total_xian += 1
                xianname = xianji[2]
                xiancode = xianji[1]
                db.xian.insert(
                    {"shengname": shengname, "shengcode": shengcode, "shiname": shiname, "shicode": shicode,
                     "xianname": xianname, "xiancode": xiancode})
                head = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/' + shengji[0][:2] + '/'
                xianurl = head + xianji[0]
                zhenlist = url_list(xianurl, "<tr class='towntr'><td><a href='(.*?)'>(.*?)</a></td><td><a href='.*?'>(.*?)</a></td></tr>")
                for zhen in zhenlist:
                    total_zhen += 1


                    zhenname = zhen[2]
                    zhencode = zhen[1]

                    db.zhen.insert(
                        {"shengname": shengname, "shengcode": shengcode, "shiname": shiname, "shicode": shicode,
                         "xianname": xianname, "xiancode": xiancode,
                         "zhenname": zhenname, "zhencode": zhencode})
                    head = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/' + shengji[0][:2] + '/' + xianji[0][:2] + '/'
                    zhenurl = head + zhen[0]
                    cunlist = url_list(zhenurl, "<tr class='villagetr'><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>")

                    for cun in cunlist:
                        total_cun += 1
                        cunname = cun[2]
                        chengxiangtype = cun[1]
                        cuncode = cun[0]
                        db.cun.insert({"shengname": shengname, "shengcode": shengcode, "shiname": shiname, "shicode": shicode, "xianname": xianname, "xiancode": xiancode,
                                         "zhenname": zhenname, "zhencode": zhencode, "cunname": cunname, "cuncode": cuncode, "chengxiangtype": chengxiangtype})
                    time.sleep(1)
                print '-----------------------------', shengname, shiname, xianname
                print "村", total_cun
                print "-----镇", total_zhen
                print "--------县", total_xian
                print "----------市", total_shi
                print "-------------省", total_sheng

    print "总共有村", total_cun
    print "镇", total_zhen
    print "县", total_xian
    print "市", total_shi
    print "省", total_sheng

    # with open("code.json", "w") as f:
    #     f.write(json.dumps(codelist))
    #     f.close()
    #     time.sleep(1)

        # < tr
        #
        #
        # class ='villagetr' > < td > 410581001001 < / td > < td > 111 < / td > < td > 开元居民委员会 < / td > < / tr >
        #
        # < tr
        #
        #
        # class ='villagetr' > < td > 110101001001 < / td > < td > 111 < / td > < td > 多福巷社区居委会 < / td > < / tr >
        #

# r = requests.get(url)
# r.encoding = 'gbk'
# rea = re.compile("<td><a href='(.*?)'>(.*?)<br/></a></td>")
# head = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/'
# for x in rea.findall(r.text):
#     sheng = x[1]
#     print sheng
#     head = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/'
#     for x in x[0]:
#         r = requests.get(head + x)
#         r.encoding = 'gbk'







# head = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2015/'