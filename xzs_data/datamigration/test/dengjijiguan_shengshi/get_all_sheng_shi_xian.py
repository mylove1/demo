# coding:utf-8

import pymongo
import sys
try:
    sys.setdefaultencoding("utf-8")
except:
    reload(sys)
    sys.setdefaultencoding("utf-8")
MASTERIP = '192.168.0.50'
conn = pymongo.Connection(MASTERIP, 27017)
db = conn.xingzheng
with open("zhen.txt", 'w') as f:
    for x in db.zhen.find():
        f.write(x["zhenname"])
        f.write('\n')