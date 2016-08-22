# coding:utf-8
import pymongo
import requests
import pybloom
import threading
import socket
import config





def link_mongo(ip, port):
    conn = pymongo.Connection(ip, port)
    return conn


class iptest(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            print "新增IP：：", len(usefulip)
            print "还需检测：", len(ippool)
            try:
                ip = ippool.pop()
            except:
                break
            try:
                r = requests.get('http://www.baidu.com', proxies={'http': ip}, timeout=5)
                usefulip.append(ip)
                db.useful.insert({"ip": ip})
            except:
                try:
                    r = requests.get('http://www.baidu.com', proxies={'http': ip},  timeout=5)
                    usefulip.append(ip)
                    db.useful.insert({"ip": ip})
                except:
                    pass

if __name__ == '__main__':
    MONGOIP = config.MONGOIP
    MONGOPORT = config.MONGOPORT
    usefulip = []
    ippool = []
    conn = link_mongo(MONGOIP, MONGOPORT)
    db = conn.ip
    f = pybloom.BloomFilter(10000, 0.001)
    for x in db.useful.find():
        f.add(x["ip"])
    for x in db.kaixin.find():
        if x["ip"] in f:
            continue
        ippool.append(x["ip"])
    db.kaixin.drop()
    print len(ippool)
    for x in range(20):
        thread = iptest()
        thread.start()
