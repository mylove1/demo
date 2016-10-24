#!/usr/bin/env python
# coding:utf-8

import pymongo
import requests
import json
import time


def get_html(url):
    headers = {
        "Referer": "http://gsxt.cqgs.gov.cn/search_tonotejyyc",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    r = requests.get(url, headers=headers)
    return r.text


def url_dict(url):
    while 1:
        try:
            j = json.loads(get_html(url))
            return j
        except:
            continue

if __name__ == "__main__":

    conn = pymongo.Connection("192.168.0.50", 27017)
    db = conn.gongshi_id

    # itemsperpage 每页的数据量
    itemsperpage = 100
    # pagenum 当前页码

    # 经营异常
    # for pagenum in range(5823, 8715):
    #     url = "http://gsxt.cqgs.gov.cn/search_searchjyyc.action?currentpage=%s&itemsperpage=%s" %(pagenum, itemsperpage)
    #     d = url_dict(url)
    #     for x in d["jyyclist"]:
    #         db.chongqing.insert(x)
    #     print pagenum
    #     time.sleep(0.2)
    #     # break

    # 经营异常状态
    for pagenum in range(2020, 2117):
        url = "http://gsxt.cqgs.gov.cn/search_searchjyyczt.action?currentpage=%s&itemsperpage=%s" %(pagenum, itemsperpage)
        d = url_dict(url)
        for x in d["jyyclist"]:
            db.chongqing.insert(x)
        print pagenum
        # time.sleep(0.1)
    #     # break

    # 检查——内资
    # for pagenum in range(1, 2161):
    #     url = "http://gsxt.cqgs.gov.cn/search_searchccjc.action?ccjctype=1&currentpage=%s&enttypeno=0&itemsperpage=%s" %(pagenum, itemsperpage)
    #     d = url_dict(url)
    #     for x in d["ccjclist"]:
    #         db.chongqing.insert({"_date": x["INSDATE"],
    #                              "_entType": x["ENTTYPENO"],
    #                              "_name": x["ENTNAME"],
    #                              "_pripid": x["PRIPID"],
    #                              "_regCode": x["REGNO"]})
    #     print pagenum
    #     time.sleep(0.1)
    #     break

    # 检查——外资
    # for pagenum in range(8800, 13785):
    #     url = "http://gsxt.cqgs.gov.cn/search_searchqyfczc.action?currentpage=%s&itemsperpage=%s" % (pagenum, itemsperpage)
    #     d = url_dict(url)
    #     for x in d["qyfczclist"]:
    #         db.chongqing.insert(x)
    #     print pagenum
    #     time.sleep(0.1)
    #     break