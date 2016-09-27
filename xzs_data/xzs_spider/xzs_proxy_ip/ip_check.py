# coding:utf-8
import sqlite3
import threading
from itertools import cycle

import config
from tools import ip_test


class justtest(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            ip = wheel.next()
            if ip_test(ip):
                usefulip.append(ip) if (ip not in usefulip)\
                    else usefulip.remove(ip)

ippool = []
usefulip = []

conn = sqlite3.connect(config.DB_FILE)
cursor = conn.cursor()
cursor.execute("select t_ip from alive;")
for x in cursor.fetchall():
    ippool.append(x[0])
cursor.close()
conn.close()

wheel = cycle(ippool)
print len(ippool)
for x in range(5):
    thread = justtest()
    thread.start()