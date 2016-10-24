#!/usr/bin/env python
# coding:utf-8

import re
import requests
import pymongo
import time


def get_url(year, num):
    for n in range(1, num+1):
        if n % 10 == 0:
            print year, n
        yield "%sSR%06d" % (year, n)


def get_html(url):
    while 1:
        try:
            r = requests.get(url)
            return r.text
        except:
            print "----------try"
            continue

if __name__ == "__main__":
    l = [
        # (2010, 75401),
        (2011, 104362),
        (2012, 137726),
        (2013, 163482),
        (2014, 217853),
        (2015, 291531),
        (2016, 294610),
    ]
for YEAR, NUM in l:
    conn = pymongo.Connection("192.168.0.50", 27017)
    db = conn.zhuzuo
    rea = re.compile(u"登记日期</th></tr><tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>")
    for key in get_url(YEAR, NUM):
        url = ("http://www.ccopyright.com.cn/cpcc/RRegisterAction.do?method=list&no=fck&sql_name=&sql_regnum=%s&sql_author=&curPage=1") % key

        text = get_html(url)
        html = ''.join(text.replace('class="datacell"', '').replace('align="center"', '').split())
        # print html
        for x in rea.findall(html):
            # print x
            zhuzuoren = x[5].split(':')[0]
            db.ruanjian.insert({"dengjihao":x[0],
                "fenleihao": x[1],
                "name": x[2],
                "jiancheng": x[3],
                "banbenhao": x[4],
                "zhuzuoren": zhuzuoren,
                "riqi_shoucifabiao": x[6],
                "riqi_dengji": x[7]
            })
        time.sleep(0.2)
# break

