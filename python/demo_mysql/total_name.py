# coding:utf-8
import MySQLdb
import pybloom

f = pybloom.BloomFilter(capacity=90000000, error_rate=0.0001)

# f = pybloom.BloomFilter(capacity=1000, error_rate=0.0001)

# with open('C:\Users\cooper\Documents\data\comp_name.fil', 'rb') as bf:
#     f = pybloom.BloomFilter.fromfile(bf)

try:
    conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306,  charset="utf8")
    cur = conn.cursor()
    for x in xrange(36000, 13987355):
        if (x % 1000) == 1:
            print x
        cur.execute("select * from company where id = %s;" % x)
        aa = cur.fetchone()
        if aa:
            data = aa[1]
            if not (data in f):
                try:
                    sql = r"""insert into company_zong(name,tyshxy,zc,zzjg,type,status,faren,zhuceziben,jingyingriqi,yingyeqixian,fazhaoriqi,guanwang,dengjijiguan,dizhi,fanwei) value ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');""" % aa[1:]
                    cur.execute(sql)
                    f.add(data)
                except:

                    print x
                    print sql
                    for r in range(1, len(aa)):
                        aa[r] = aa[r].replace("'", '"')
                        aa[r] = aa[r].replace("\\", "")
                        aa[r] = aa[r].replace("(", "（")
                        aa[r] = aa[r].replace(")", "）")
                    sql = r"""insert into company_zong(name,tyshxy,zc,zzjg,type,status,faren,zhuceziben,jingyingriqi,yingyeqixian,fazhaoriqi,guanwang,dengjijiguan,dizhi,fanwei) value ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');""" % aa[1:]
                    cur.execute(sql)
                    f.add(data)



            f.add(data)
    conn.commit()

    # aa = cur.execute('select * from shunco;')
    # for x in cur.fetchall():
    #     f.add(x[0])

    # bb = cur.execute('select name from shunco where id = 18476404;')
    # shunco_name = cur.fetchone()
    # print aa == bb
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

print f.count

# with open('C:\Users\cooper\Documents\data\comp_name.fil', 'wb') as bf:
#     f.tofile(bf)
