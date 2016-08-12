# coding:utf-8
'''
   中国高匿代理 大概一天可以运行一次，
   每一次会自动过滤掉本地IP池中有的ip
'''
import requests
import re
import time
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
    headers = {
    'Host': 'cn - proxy.com',
    'Proxy-Connection': 'keep - alive',
    'Cache-Control': 'max - age = 0',
    'Accept': 'text / html, application / xhtml + xml, application / xml;',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla / 5.0(Windows NT 6.1; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 50.0.2661.102 Safari / 537.36',
    'Referer': 'http://cn-proxy.com',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh - CN, zh;',
    }
    headers = {}
    r = requests.get(url, headers=headers)
    return ''.join(r.text.split())


def main():

    # db = link_mongo()
    # f = pybloom.BloomFilter(capacity=100000, error_rate=0.0001)
    # for x in db.bigpool.find():
    #     f.add(x["ip"])
    url = 'http://cn-proxy.com/'
    html = get_html(url)
    print html
    ip_list = re.findall('<tr><td>(.*?)</td><td>(.*?)</td>', html)
    for x in ip_list:
        # if x[0] == "服务器地址":
        #     continue
        ip = ':'.join(x)
        print ip
        # if ip in f:
        #     continue
        # else:
        #     print ip
        #     f.add(ip)
        #     db.bigpool.insert({"ip": ip})
        #     db.kaixin.insert({"ip": ip})


if __name__ == '__main__':
    main()
