# coding:utf-8
import MySQLdb
import pybloom
import pymongo

# f = pybloom.BloomFilter(capacity=90000000, error_rate=0.0001)

# f = pybloom.BloomFilter(capacity=1000, error_rate=0.0001)

with open('C:\Users\cooper\Documents\data\comp_have_base_total_1.fil', 'rb') as bf:
    f = pybloom.BloomFilter.fromfile(bf)

conn_mongo = pymongo.Connection('192.168.0.50', 27017)
db = conn_mongo.zhengli

try:
    conn = MySQLdb.connect(host='192.168.0.50', user='root', passwd='dingyu', db='xzs', port=3306,  charset="utf8")
    cur = conn.cursor()
    conn2 = pymongo.Connection('192.168.0.50', 27017)
    db2 = conn2.youboy
    for x in db2.comp.find():
        data = x["name"]
    # for x in xrange(1, 27107535):
    #     if (x % 1000) == 1:
    #         print x
    #     cur2.execute("select name from company_zong where id = %s;" % x)
    #     aa = cur2.fetchone()
    #     if aa:
    #         data = aa[0]
        if not (data in f):
            try:
                db.comp_not_base.insert({"comp": data})
                f.add(data)
                sql = r"""insert into t_gongsi(t_gongsi_mingzi) value ('%s');""" % (data)
                cur.execute(sql)
                conn.commit()
            except MySQLdb.Error, e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])


    # aa = cur.execute('select * from shunco;')
    # for x in cur.fetchall():
    #     f.add(x[0])

    # bb = cur.execute('select name from shunco where id = 18476404;')
    # shunco_name = cur.fetchone()
    # print aa == bb
    conn.close()
    # conn2.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

print f.count

with open('C:\Users\cooper\Documents\data\comp_have_base_total_2.fil', 'wb') as abf:
    f.tofile(abf)
