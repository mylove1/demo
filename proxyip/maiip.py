# coding:utf-8

import time
import pymongo
import requests
import pybloom


def link_mongo():
    conn = pymongo.Connection('192.168.100.55', 27017)
    db = conn.ip.pool
    return db


def get_proxy(db, f):
    while True:
        req = requests.get('http://dev.kuaidaili.com/api/getproxy/?orderid=927082360301289&num=999&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_an=1&an_ha=1&sp1=1&sp2=1&sp3=1&sep=2')
        iplist = req.text.split('\n')
        for x in iplist:
            if x in f:
                continue
            else:
                f.add(x)
                db.insert({'ip': x})
        time.sleep(10)


def main():
    db = link_mongo()
    f = pybloom.BloomFilter(capacity=500000, error_rate=0.0001)
    get_proxy(db, f)


if __name__ == '__main__':
    main()