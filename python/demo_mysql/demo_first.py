# coding:utf-8
import MySQLdb

import MySQLdb

# try:
#     conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306,  charset="utf8")
#     cur = conn.cursor()
#     cur.execute('select name from company where id < 22;')
#     for x in cur.fetchall():
#         print x[0]
#     cur.close()
#     conn.close()
# except MySQLdb.Error, e:
#     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

try:
    conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306,  charset="utf8")
    cur = conn.cursor()
    aa = cur.execute('select name from company where id = 14;')
    comany_name = cur.fetchone()
    bb = cur.execute('select name from shunco where id = 18476404;')
    shunco_name = cur.fetchone()
    print aa == bb
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])