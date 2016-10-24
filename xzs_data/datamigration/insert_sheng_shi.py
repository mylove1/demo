#!/usr/bin/env python
# coding:utf-8
import pymongo
import MySQLdb
import time

DbConfig = {
    "user": "root",
    "passwd": "dingyu",
    "db": "xzs",
    "host": "192.168.0.50",
}

def gongsi_name2diqu(name):
    repl = [
        u"有限责任公司",
        u"股份有限公司",
        u"有限公司",
        u"专业合作社",
        u"合作社",
        u"工商和质量监督管理局",
        u"市场监督管理局",
        u"市场监督管理所",
        u"工商行政管理总局",
        u"工商质监局",
        u"工商局",
        u"市场监管局",
    ]

    fen = [
        u"营业部",
        u"加油站",
        u"分公司",
        u"支行",
    ]

    if name[-3:] in fen:
        if u"公司" in name:
            name = name[name.find(u"公司") + 2:]

    for x in repl:
        name = name.replace(x, "")
    # print name
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


def l2l(l):
    if l[2]:
        diqu = pei(l[2], pipei)
        if diqu:
            l[3] = diqu["v"]["sheng"]
            l[4] = diqu["v"]["shi"]
            return l

    else:
        diqu = pei(l[1], pipei)
        if diqu:
            l[3] = diqu["v"]["sheng"]
            l[4] = diqu["v"]["shi"]
            return l
    return ""


if __name__ == "__main__":
    pipei = load_pipei()
    conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db=DbConfig['db'],
                           host=DbConfig['host'], charset='utf8', use_unicode=True)
    cursor = conn.cursor()
    row_list = [
        "t_gongsi_id",
        "t_gongsi_mingzi",
        "t_gongsi_dengjijiguan",
        "t_gongsi_sheng",
        "t_gongsi_shi"
    ]

    table_sour = "t_gongsi"
    table_targ = table_sour
    biao = 193000
    biaoshang = 193000
    while biao <5000000:

        biao += 500000
        select_condition = "where t_gongsi_id >= %s and t_gongsi_id <= %s" % (biaoshang, biao)
        biaoshang = biao
        # select_condition = ""

        # 构造查询语句
        select_sql = 'select ' + ','.join(row_list) + ' from ' + table_sour
        if select_condition:
            select_sql += ' ' + select_condition + ';'
        else:
            select_sql += ';'
        # print select_sql

        cursor.execute(select_sql)
        L = []
        datalist = cursor.fetchall()

        for enu, every in enumerate(datalist):
            if every[0] % 1000 == 0:
                print every[0], '\t', time.clock(), '\t', time.ctime()
            l = l2l(list(every))
            if l:
                L.append([l[3], l[4], l[0]])
            else:
                continue

            if enu % 1000 == 0:
                # try:
                    cursor.executemany('update t_gongsi set t_gongsi_sheng = %s, t_gongsi_shi = %s where t_gongsi_id = %s;', L)
                    conn.commit()
                    L = []
                # except:
                #     print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                #     for x in L:
                #         try:
                #             cursor_targ.executemany(insert_sql, [x])
                #
                #             print '-------------------------------------------->>>'
                #         except:
                #             "xxx"
                #     conn_targ.commit()
                #     L = []

        try:
            cursor.executemany('update t_gongsi set t_gongsi_sheng = %s, t_gongsi_shi = %s where t_gongsi_id = %s;', L)
            conn.commit()
        except:
            print 'xxx'