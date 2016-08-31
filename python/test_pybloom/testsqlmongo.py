# coding:utf-8
import pybloom
import pymongo

# print(help(pybloom))
# print(dir(pybloom))
# f = pybloom.BloomFilter(capacity=1000, error_rate=0.0001)
# for x in range(100):
#     f.add(x)
# print(33 in f)

# [save to file]
# with open('bf','wb') as bf:
#     f.tofile(bf)

# [read from file]
with open('C:\Users\cooper\Documents\data\comp_name.fil', 'rb') as bf:
    f = pybloom.BloomFilter.fromfile(bf)

print u"上海天墅市场营销策划有限公司" in f
moconn = pymongo.Connection("192.168.0.50", 27017)
db = moconn.test
a = db.lindmysql.find()
for x in a:
    print x["name"], x["info"] in f
