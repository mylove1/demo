# coding:utf-8
import MySQLdb
import pybloom
import pymongo

f = pybloom.BloomFilter(capacity=50000000, error_rate=0.0001)

# f = pybloom.BloomFilter(capacity=1000, error_rate=0.0001)

conn_mongo = pymongo.Connection('192.168.0.50', 27017)
db = conn_mongo.zhengli

# with open('C:\Users\cooper\Documents\data\comp_name.fil', 'rb') as bf:
#     f = pybloom.BloomFilter.fromfile(bf)

try:
    conn = MySQLdb.connect(host='192.168.0.50', user='root', passwd='dingyu', db='xzs', port=3306,  charset="utf8")
    cur = conn.cursor()
    for x in xrange(1659, 21470433):
        if (x % 1000) == 1:
            print x
        cur.execute("select t_gongsi_mingzi from t_gongsi where t_gongsi_id = %s;" % x)
        aa = cur.fetchone()
        if aa:
            data = aa[0]
            if not (data in f):
                try:

                    db.comp_have_base.insert({"comp": data})
                    f.add(data)
                except MySQLdb.Error, e:
                    pass


    # aa = cur.execute('select * from shunco;')
    # for x in cur.fetchall():
    #     f.add(x[0])

    # bb = cur.execute('select name from shunco where id = 18476404;')
    # shunco_name = cur.fetchone()
    # print aa == bb
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

print f.count

with open('C:\Users\cooper\Documents\data\comp_have_base.fil', 'wb') as abf:
    f.tofile(abf)
