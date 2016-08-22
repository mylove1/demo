# coding:utf-8
import pymongo

conn = pymongo.Connection('192.168.0.50', 27017)
db = conn.ip
for x, y in enumerate(db.bigpoola.find()):
    # print x, y, len(y["ip"])
    # if x in [15608, 11632, 16990]:
    #     continue
    # if len(y["ip"]) > 25:
    #     continue
    #
    db.bigpool.insert({"ip": y["ip"]})