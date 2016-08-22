# coding:utf-8
import pymongo
import requests
import pybloom
import threading
import socket
from itertools import cycle


IP = socket.gethostbyname(socket.gethostname())
print IP
mongoPORT = 27017


def link_mongo():
    conn = pymongo.Connection(IP, mongoPORT)
    db = conn.ip
    return db

class justtest(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            ip = wheel.next()
            try:
                r = requests.get('http://www.baidu.com', proxies={'http': ip}, timeout=5)
                if ip not in usefulip:
                    usefulip.append(ip)
            except:
                try:
                    r = requests.get('http://www.baidu.com', proxies={'http': ip}, timeout=5)
                    if ip not in usefulip:
                        usefulip.append(ip)
                except:
                    try:
                        usefulip.remove(ip)
                    except:
                        pass

ippool = []
usefulip = []

db = link_mongo()
for x in db.useful.find():
    ippool.append(x["ip"])
wheel = cycle(ippool)
print len(ippool)
for x in range(5):
    thread = justtest()
    thread.start()