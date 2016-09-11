# coding:utf-8
import pymongo
import sys
import MySQLdb
import time
reload(sys)
try:
    sys.setdefaultencoding("utf-8")
except:
    reload(sys)
    sys.setdefaultencoding("utf-8")
MASTERIP = '192.168.0.2'
conn = pymongo.Connection(MASTERIP, 27017)
db = conn.xizhi
jiguanlist = []
with open('dengjijiguan.txt', 'w') as f:
    infolist = db.compinfo.find()#.limit(44950)
    for enu, x in enumerate(infolist):
        if enu%10000 == 0:
            print enu
        j = x["baseinfo"]["dengjijiguan"].replace('(', '（').replace(')', '）')
        if j in jiguanlist:
            continue
        else:
            jiguanlist.append(j)
    print "总共有%d个登记机关"%len(jiguanlist)
    f.write('\n'.join(jiguanlist))
    f.write('\n')

# print '总共用时：%f'%(time.time()-starttime)
conn.close()
