#!/usr/bin/env python
# coding:utf-8

import pymongo
import pybloom
from xzs_data.xinyonggongshi.chongqing.chongqing import ChongQingAnalyze
import threading

class id22info(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            key = keylist.pop()
            # print key
            try:
                entid = key["entid"]
                regid = key["regid"]
                a = ChongQingAnalyze(entid=entid, regid=regid)
                db.chongqing_id.update({"entid": entid}, {"$set": {"typeno": a.type}})
                db.chongqing_info.insert(a.get_gongshi_info())
            except:
                print "xxxxxxx"
                print key
                continue


if __name__ == "__main__":
    conn = pymongo.Connection("192.168.0.50", 27017)
    db = conn.gongshi_id
    bf = pybloom.BloomFilter(500000, 0.001)
    for x in db.chongqing_info.find():
        # print x
        try:
            bf.add(x["base"]["pripid"])
        except:
            continue
    keylist = []
    print len(bf)
    for x in db.chongqing_id.find():
        if x["entid"] in bf:
            continue
        keylist.append({"entid": x["entid"],
                        "regid": x["regid"]})
    print len(keylist)
    for thread in range(10):
        thr = id22info()
        thr.start()
        # db.chongqing_id.insert({"entid": x["_pripid"],
        #                         "regid": x["_regCode"],
        #                         "name": x["_name"],
        #                         "typeno": ""})


