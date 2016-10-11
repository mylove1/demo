# coding:utf-8
import threading
import MySQLdb
import time
import pymongo
import pybloom
MASTERIP = '192.168.0.50'
conn_mongo = pymongo.Connection(MASTERIP, 27017)
db_mongo = conn_mongo.tianyan

start = db_mongo.totalcount.find()[0]["count"] + 1
print start
start_num = start
kwlist = []

ff = pybloom.BloomFilter(capacity=40000000, error_rate=0.0001)


class compadd(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while 1:
            if len(kwlist) <= 10000:
                global a, start_num
                a = start_num
                b = a + 99999
                if b >= 27107534:
                    b = 27107534
                try:
                    conn = MySQLdb.connect(host=MASTERIP, user='root', passwd='dingyu', db='dingyu', port=3306,
                                           charset="utf8")
                    cur = conn.cursor()
                    cur.execute("select name from company_zong where id between %s and %s  ;" % (a, b))
                    for y in cur:
                        x = y[0]
                        if len(x) >= 5:
                            for n in range(1, 5):
                                kw = x[:n]
                                if not(kw in ff):
                                    ff.add(kw)
                                    kwlist.append(kw)
                        else:
                            for n in range(1, len(x)):
                                kw = x[:n]
                                if not(kw in ff):
                                    ff.add(kw)
                                    kwlist.append(kw)

                    start_num += 100000
                finally:
                    conn.close()
                if b == 27107534:
                    break
                time.sleep(100)
            else:
                time.sleep(100)



a = compadd()
a.start()
