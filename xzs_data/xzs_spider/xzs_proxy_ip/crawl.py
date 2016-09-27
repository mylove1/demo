# coding:utf-8

import re
import requests
import sqlite3
import time
import threading

import config
import pybloom

class ProxyCrawl(threading.Thread):
    def __init__(self, ziyuan, f):
        threading.Thread.__init__(self)
        self.ziyuan = ziyuan
        self.SELEEP = 100
        self.f = f

    def get_html(self, url):
        headers = self.headers
        try:
            r = requests.get(url, headers=headers)
            return ''.join(r.text.split())
        except:
            pass

    def to_db(self, ip_list):
        print '----------------',
        conn = sqlite3.connect(config.DB_FILE)
        cursor = conn.cursor()
        for ip in ip_list:
            cursor.execute('INSERT INTO pool (t_ip) VALUES ("%s");'% ip)
        cursor.close()
        conn.commit()
        conn.close()
        print '>>>>>>>>>>>>>>>>>>>>>>'

    def run(self):
        ADD = 0
        while 1:
            ip_list = []
            for everyone in self.ziyuan:
                self.urllist = everyone["urllist"]
                self.name = everyone["name"]
                self.rule = everyone["rule"]
                self.frequency = everyone["frequency"]
                self.headers = everyone["headers"]
                for url in self.urllist:
                    html = self.get_html(url)
                    ip_new_all_list = re.findall(self.rule, html)
                    for x in ip_new_all_list:
                        ip = ':'.join(x)
                        # print ip
                        # 判断IP是否在过滤器中，如果存在就
                        if ip in self.f:
                            continue
                        elif len(ip) > 21:
                            print '          ', ip
                            continue
                        else:
                            print ip
                            self.f.add(ip)
                            ip_list.append(ip)
                            ADD = ADD + 1
                    time.sleep(2)
                print time.ctime(time.time()), "added：", ADD, self.name
                # time.sleep(self.frequency)
            self.to_db(ip_list)
            time.sleep(self.SELEEP)



def crawl():
    ADD = 0

    # 连接数据库，把数据库中已经有的IP放入过滤器
    print u"正在初始化...."
    conn = sqlite3.connect(config.DB_FILE)
    cursor = conn.cursor()
    cursor.execute("select t_ip from pool;")

    f = pybloom.BloomFilter(capacity=200000, error_rate=0.001)
    for x in cursor.fetchall():
        f.add(x[0])
    cursor.close()
    conn.close()
    print u"初始化完成，开始抓取\n"

    a = ProxyCrawl(config.resources, f)
    a.start()


if __name__ == "__main__":
    crawl()