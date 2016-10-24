#!/usr/bin/env python
# coding:utf-8

import pymongo


def gongsi_name2diqu(name):
    repl = [
        u"有限责任公司",
        u"股份有限公司",
        u"有限公司",
        u"合作社",
    ]

    fen = [
        u"营业部",
        u"加油站",
        u"分公司",
        u"",
    ]

    if name[-3:] in fen:
        if u"公司" in name:
            name = name[name.find(u"公司") + 2:]

    for x in repl:
        name = name.replace(x, "")
    print name
    return name


def pei(name, pipei):
    name = gongsi_name2diqu(name)
    for x in range(1, len(name) - 1):
        if name[:-x] in pipei.keys():
            return {"key": name, "v": pipei[name[:-x]]}




def load_pipei():
    conn = pymongo.Connection(host="192.168.0.50", port=27017)
    db = conn.xingzheng
    pipei = {}
    for x in db.pipei.find():
        pipei[x["key"]] = x["v"]
    return pipei

if __name__ == '__main__':
    name = u"中国移动有限公司浙江杭州滨江营业部"
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