# coding:utf-8
import MySQLdb

import MySQLdb

try:
    conn = MySQLdb.connect(host='192.168.0.100',
                           user='root',
                           passwd='dingyu',
                           db='dingyu',
                           port=3306,
                           charset="utf8")
    cur = conn.cursor()
    aa = cur.execute('select name from company where id = 14;')
    comany_name = cur.fetchone()

    bb = cur.execute('select name from shunco where id = 1847;')
    shunco_name = cur.fetchone()

    a = 1
    b = 1000000
    cur.execute("select name from company_zong where \
                 id between %s and %s;" % (a, b))
    aa = cur.fetchall()# 返回((,,),(,,),)格式数据

    cur.close()
    conn.close()

except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])