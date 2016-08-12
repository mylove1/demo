# coding:utf-8
import requests
import pybloom
import pymongo
f = pybloom.BloomFilter(capacity=200000, error_rate=0.0001)
conn = pymongo.Connection('192.168.100.55', 27017)
db = conn.ip
total = 0

# for x in db.bigpool.find():
#     f.add(x["ip"])

for x in db.proxy.find():
    ip = x["ip"]
    if ip in f:
        continue
    else:
        f.add(ip)
        db.proxy2.insert({"ip": ip})
        total += 1

print 'ok', total
    # f.add(ip)

# for x in db.proxy.find():
#     ip = x["ip"]
#     if ip in f:
#         continue
#     else:
#         f.add(ip)
#         db.pool.insert({"ip": ip})
#
#
# print total

