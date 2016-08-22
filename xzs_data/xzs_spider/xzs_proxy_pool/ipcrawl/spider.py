# coding:utf-8
'''
   代理ip收割机
'''
import requests
import re
import time
import threading
import pymongo
import socket
import pybloom
import config
import resource





class ProxyCrawl(threading.Thread):
    def __init__(self, ziyuan):
        threading.Thread.__init__(self)
        self.urllist = ziyuan["urllist"]
        self.name = ziyuan["name"]
        self.rule = ziyuan["rule"]
        self.frequency = ziyuan["frequency"]
        self.headers = ziyuan["headers"]

    def get_html(self, url):
        headers = self.headers
        try:
            r = requests.get(url, headers=headers)
            return ''.join(r.text.split())
        except:
            pass

    def run(self):
        global ADD
        while 1:
            for url in self.urllist:
                html = self.get_html(url)
                ip_list = re.findall(self.rule, html)
                for x in ip_list:
                    print self.name, '---->'
                    ip = ':'.join(x)
                    # print ip
                    # 判断IP是否在过滤器中，如果存在就
                    if ip in f:
                        continue
                    else:
                        print ip
                        f.add(ip)
                        db.bigpool.insert({"ip": ip})
                        db.kaixin.insert({"ip": ip})
                        ADD = ADD + 1
                time.sleep(2)
            print time.ctime(time.time()), "新增：", ADD, self.name
            time.sleep(self.frequency)


def link_mongo():
    conn = pymongo.Connection(IP, mongoPORT)
    db = conn.ip
    return db


def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    r = requests.get(url, headers=headers)
    return ''.join(r.text.split())


# def main():
#
#     db = link_mongo()
#     f = pybloom.BloomFilter(capacity=100000, error_rate=0.0001)
#     for x in db.bigpool.find():
#         f.add(x["ip"])
#
#     for page in xrange(1, 11):
#         url = ''.join(["http://www.kuaidaili.com/proxylist/", str(page), '/'])
#         html = get_html(url)
#         ip_list = re.findall('<tr><tddata-title="IP">(.*?)</td><tddata-title="PORT">(.*?)</td>', html)
#         for x in ip_list:
#             ip = ':'.join(x)
#             if ip in f:
#                 continue
#             else:
#                 print ip
#                 f.add(ip)
#                 db.bigpool.insert({"ip": ip})
#                 db.kaixin.insert({"ip": ip})
#         print '----------------------', page
#         time.sleep(0.2)


if __name__ == '__main__':
    ADD = 0
    IP = config.MONGOIP
    mongoPORT = config.MONGOPORT
    # 连接mongo数据库，把数据库中已经有的IP放入过滤器
    db = link_mongo()
    f = pybloom.BloomFilter(capacity=100000, error_rate=0.0001)
    for x in db.bigpool.find():
        f.add(x["ip"])

    for thread in resource.resources:
        a = ProxyCrawl(thread)
        a.start()
