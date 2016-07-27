# -*- coding: utf-8 -*-

import MySQLdb


comp_list = []

conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306, charset="utf8")
cursor = conn.cursor()
a = 1
b = 10
cursor.execute("select name from company_zong where id between %s and %s  ;" % (a, b))
aa = cursor.fetchall()
for x in aa:
    # comp_list.append(x)
    print x[0]
conn.close()
