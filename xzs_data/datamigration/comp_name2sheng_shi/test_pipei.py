#!/usr/bin/env python
#coding:utf-8

import pymongo
import sys

print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding("utf-8")
from diqu_pipei import pipei


def pei(name, db):
    for x in range(1, len(name) - 1):
        for y in db.pipei.find({"key": name[:-x]}):
            return y


name = u"浙江信至尚企业征信服务"
conn = pymongo.Connection(host="192.168.0.50", port=27017)
db = conn.xingzheng
diqu = pei(name, db, pipei)
if diqu:
    print diqu["key"], diqu["v"]["sheng"], diqu["v"]["shi"], diqu["v"]["xian"]


# 把数据写入文件
# with open("diqu_pipei.py", "wb") as f:
#     f.write("pipei = {\n")
#     for x in db.pipei.find():
#         f.write('"'+ x["key"]+ '": {"sheng": "'+ x["v"]["sheng"]+ '", "shi": "'+ x["v"]["shi"]+ '"+ "xian": "'+ x["v"]["xian"]+ '"},\n')
#     f.write("}\n")
#     # print("pipei = {\n")
#     # for x in db.pipei.find():
#     #     print('"'+ x["key"]+ '": {"sheng": "'+ x["v"]["sheng"]+ '", "shi": "'+ x["v"]["shi"]+ '"+ "xian": "'+ x["v"]["xian"]+ '"},\n')
#     # print("}\n")