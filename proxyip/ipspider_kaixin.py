# coding:utf-8
'''
   开心代理 大概一个小时可以运行一次，
   每一次会自动过滤掉本地IP池中有的ip
'''
import requests
import re
import time
import threading
import pymongo
import socket
import pybloom


IP = socket.gethostbyname(socket.gethostname())
mongoPORT = 27017


def link_mongo():
    conn = pymongo.Connection(IP, mongoPORT)
    db = conn.ip
    return db


def get_html(url):
    r = requests.get(url)
    return ''.join(r.text.split())


def main():

    db = link_mongo()
    f = pybloom.BloomFilter(capacity=100000, error_rate=0.0001)
    for x in db.bigpool.find():
        f.add(x["ip"])

    for page in xrange(1, 11):
        url = ''.join(["http://www.kxdaili.com/dailiip/1/", str(page), '.html#ip'])
        html = get_html(url)
        ip_list = re.findall('<tr.*?><td>(.*?)</td><td>(.*?)</td>', html)
        for x in ip_list:
            ip = ':'.join(x)
            if ip in f:
                continue
            else:
                print ip
                f.add(ip)
                db.bigpool.insert({"ip": ip})
                db.kaixin.insert({"ip": ip})
        print '----------------------', page
        time.sleep(0.2)


if __name__ == '__main__':
    main()
