#!/usr/bin/env python
# coding:utf-8

import requests
import warnings
import sys
import json
import pymongo
warnings.filterwarnings("ignore")


for num in range(10):
    print num
    conn = pymongo.Connection("192.168.0.50", 27017)
    db = conn.zhizhiren
    url = ''.join(['https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E6%89%A7%E8%A1%8C%E4%BA%BA&pn=',
                  str(num * 50),
                  '&rn=10&ie=utf-8&oe=utf-8&format=json&t=1476685443770&cb=jQuery110207341718924856264_1476685334189&_=1476685334248'])
    r = requests.get(url=url, verify=False)
    j = json.loads(r.text[46:-2])
    l = []
    exi = False
    for jilu in j["data"][0]["result"]:
        jilu["num"] = num
        if jilu["iname"] in l:
            exi = True
            break
        l.append(jilu["iname"])

    db.zhixinren.insert(j["data"][0]["result"])
    if exi:
        print "wancheng"
        sys.exit()
    break
