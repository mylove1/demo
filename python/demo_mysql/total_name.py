# coding:utf-8
import MySQLdb
import pybloom

# f = pybloom.BloomFilter(capacity=90000000, error_rate=0.0001)

# f = pybloom.BloomFilter(capacity=1000, error_rate=0.0001)

with open('C:\Users\cooper\Documents\data\comp_name.fil', 'rb') as bf:
    f = pybloom.BloomFilter.fromfile(bf)

try:
    conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306,  charset="utf8")
    cur = conn.cursor()
    for x in xrange(1, 20657846):
        if (x % 1000) == 1:
            print x
        cur.execute("select name,sheng,shi,shunqiurl from shunco where id = %s;" % x)
        aa = cur.fetchone()
        if aa:
            data = aa[0]
            if not (data in f):
                try:

                    sql = r"""insert into company_zong(name,sheng,shi,shunqiurl) value ('%s','%s','%s','%s');""" % (aa[0], aa[1], aa[2],aa[3])
                    cur.execute(sql)
                    conn.commit()
                    f.add(data)
                except MySQLdb.Error, e:
                    print "Mysql Error %d: %s" % (e.args[0], e.args[1])


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

with open('C:\Users\cooper\Documents\data\comp_name.fil', 'wb') as abf:
    f.tofile(abf)
