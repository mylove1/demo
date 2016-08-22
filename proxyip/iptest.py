# coding:utf-8
import pymongo
import requests
import pybloom
import threading
import socket


IP = socket.gethostbyname(socket.gethostname())
print IP
mongoPORT = 27017


def link_mongo():
    conn = pymongo.Connection(IP, mongoPORT)
    db = conn.ip
    return db


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

class justtest(threading.Thread):
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
            except:
                try:
                    r = requests.get('http://www.baidu.com', proxies={'http': ip}, timeout=5)
                    usefulip.append(ip)
                except:
                    pass

# def ip():
#
#     ippool = []
#     usefulip = []
#
#     db = link_mongo()
#     for x in db.useful.find():
#         ippool.append(x["ip"])
#     print len(ippool)
#     for x in range(20):
#         thread = iptest()
#         thread.start()
#     return ippool


if __name__ == '__main__':
    usefulip = []
    ippool = []
    db = link_mongo()
    f = pybloom.BloomFilter(10000, 0.001)
    for x in db.useful.find():
        f.add(x["ip"])
    for x in db.kaixin.find():
    # for x in db.bigpool.find():
        if x["ip"] in f:
            continue
        ippool.append(x["ip"])
    db.kaixin.drop()
    print len(ippool)
    for x in range(10):
        thread = iptest()
        thread.start()





    # usefulip = []
    # ippool = []
    # db = link_mongo()
    # for x in db.useful.find():
    #     ippool.append(x["ip"])
    # print len(ippool)
    # for x in range(10):
    #     thread = justtest()
    #     thread.start()
