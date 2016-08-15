# coding:utf-8
import threading
import MySQLdb
import time

start_num = 8614537
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
                if b >= 27107534:
                    b = 27107534
                try:
                    connect = MySQLdb.connect(host='192.168.100.55', user='root', passwd='dingyu', db='dingyu', port=3306,
                                           charset="utf8")
                    cursor = connect.cursor()
                    cursor.execute("select name from company_zong where id between %s and %s  ;" % (a, b))
                    for x in cursor:
                        kwlist.append(x[0])
                    start_num += 100000
                finally:
                    connect.close()
                if b == 27107534:
                    break
                time.sleep(200)
            else:
                time.sleep(200)

a = compadd()
a.start()
