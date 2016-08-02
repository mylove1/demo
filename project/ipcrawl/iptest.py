# coding:utf-8
import pymongo
import requests
import threading


def linkdb():
    conn = pymongo.Connection('192.168.0.100', 27017)
    db = conn.ip
    return db


class iptest(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global ippool
        while 1:
            ip = ippool.pop()
            try:
                r = requests.get('http://www.baidu.com', proxies={'http': ip}, timeout=5)
                usefulip.append(ip)
            except:
                try:
                    r = requests.get('http://www.baidu.com', proxies={'http': ip},  timeout=5)
                    usefulip.append(ip)
                except:
                    pass
usefulip = []
def ip():
    global ippool
    global usefulip
    ippool = []


    db = linkdb()
    for x in db.proxy.find():
        ippool.append(x["ip"])
    print len(ippool)
    for x in range(20):
        thread = iptest()
        thread.start()
    return ippool