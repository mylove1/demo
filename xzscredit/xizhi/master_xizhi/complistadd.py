# coding:utf-8
import threading
import MySQLdb
import time
import pymongo
MASTERIP = '192.168.0.50'
conn = pymongo.Connection(MASTERIP, 27017)
db = conn.xizhi
start = db.totalcount.find()[0]["count"] + 1
print start
start_num = start
kwlist = []

class compadd(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            if len(kwlist) <= 1000:
                global a, start_num
                a = start_num
                b = a + 9999
                if b >= 27107534:
                    b = 27107534
                try:
                    conn = MySQLdb.connect(host=MASTERIP, user='root', passwd='dingyu', db='dingyu', port=3306,
                                           charset="utf8")
                    cur = conn.cursor()
                    cur.execute("select name from company_zong where id between %s and %s  ;" % (a, b))
                    for x in cur:
                        kwlist.append(x[0])
                    start_num += 10000
                finally:
                    conn.close()
                if b == 27107534:
                    break
                time.sleep(200)
            else:
                time.sleep(200)



a = compadd()
a.start()
