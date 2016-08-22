# coding:utf-8
'''
   开心代理 大概半天可以运行一次，
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
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    r = requests.get(url, headers=headers)
    return ''.join(r.text.split())


def main():


    for page in xrange(1, 2):
        url = 'http://www.httpsdaili.com/index.asp?stype='
        html = get_html(url)
        ip_list = re.findall('<trclass="odd"><tdclass="style1">(.*?)</td><tdclass="style2">(.*?)</td>', html)
        for x in ip_list:
            ip = ':'.join(x)
            print ip
        print '----------------------', page
        time.sleep(0.2)


if __name__ == '__main__':
    main()
