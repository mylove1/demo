#!/usr/bin/env python
# coding:utf-8

import pymongo


def pei(name, pipei):
    for x in range(1, len(name) - 1):
        if name[:-x] in pipei.keys():
            return {"key": name, "v": pipei[name[:-x]]}
        else:
            return {"key": "no", "v": "no"}



def load_pipei():
    conn = pymongo.Connection(host="192.168.0.50", port=27017)
    db = conn.xingzheng
    pipei = {}
    for x in db.pipei.find():
        pipei[x["key"]] = x["v"]
    return pipei

if __name__ == '__main__':
    name = u"浙江信至尚"
    pipei = load_pipei()
    diqu = pei(name, pipei)
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