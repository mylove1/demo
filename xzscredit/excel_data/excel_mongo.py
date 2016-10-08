#!/usr/bin/env python
#coding:utf-8

import xlrd
import pymongo

file_dict = [
    {
        "filename":u"F:\\企业目录（整理好）\\[青海.xls",
         "collist":[
             "mingzi",
             "lianxiren",
             "dianhua",
             "shouji",
             "chuanzhen",
             "youxiang",
             "dizhi",
             "zhuyingchanpin",
             "zhuceziben",
             "yingyee",
             "yuangongrenshu",
             "qiyeleixing",
             "jingyingmoshi",
         ],
         "first": 1,
         "sheng": u"青海",
         "shi" : u""
    },
    {
        "filename": u"F:\企业目录（整理好）\安徽\安徽.4373.xls",
        "collist": [
            "mingzi",
            "dizhi",
            "lianxiren",
            "shouji",
        ],
        "first": 1,
        "sheng": u"安徽",
        "shi": u""
    },

]


def to_mongo(db, dic):

    db.excel_one.insert(dic)


if __name__ == "__main__":

    conn = pymongo.Connection(host="192.168.0.50", port=27017)
    db = conn.excel
    file_geshi = file_dict[1]
    file = xlrd.open_workbook(file_geshi["filename"])
    table = file.sheets()[0]
    print "ok"

    for row in range(table.nrows):
        if row < file_geshi["first"]:
            continue
        data = {
            "mingzi": "",
            "lianxiren": "",
            "dianhua": "",
            "shouji": "",
            "chuanzhen": "",
            "youxiang": "",
            "dizhi": "",
            "zhuyingchanpin": "",
            "zhuceziben": "",
            "yingyee": "",
            "yuangongrenshu": "",
            "qiyeleixing": "",
            "jingyingmoshi": "",
        }
        rowdata = table.row_values(row)
        for enu,col in enumerate(file_geshi["collist"]):
            data[col] = rowdata[enu]

            to_mongo(db, data)