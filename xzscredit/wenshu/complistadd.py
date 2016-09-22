# coding:utf-8
import threading
import MySQLdb
import time
import config

start_num = 27107535
kwlist = []

class compadd(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            if len(kwlist) <= 1000:
                global a, start_num
                a = start_num
                b = a + 99999
                if b >= 39000000:
                    b = 39000000
                try:
                    conn = MySQLdb.connect(host=config.master, user='root', passwd='dingyu', db='xzs', port=3306,
                                           charset="utf8")
                    cur = conn.cursor()
                    cur.execute("select t_gongsi_mingzi from t_gongsi where t_gongsi_id between %s and %s  ;" % (a, b))
                    for x in cur:
                        kwlist.append(x[0])
                    start_num += 100000
                finally:
                    conn.close()
                if b == 27107534:
                    break
                time.sleep(200)
            else:
                time.sleep(200)

a = compadd()
a.start()
