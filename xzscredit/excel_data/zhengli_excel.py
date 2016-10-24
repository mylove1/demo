#!/usr/bin/env python
# coding:utf-8

import xlrd
import os

def walk_file(rootdir):
    for parent,dirnames,filenames in os.walk(rootdir):
        for x in filenames:
            yield os.path.join(parent, x).replace("\\", "\\\\")

def excel2dict(year, f, data):
    guide = {
        u"单位名称": "",
        u"电话": "",
        u"传真": "",
        u"移动电话": "",
        u"负责人": "",
        u"联系人": "",
        u"职位": "",
        u"地址": "",
        u"邮政编码": "",
        u"经济类型": "",
        u"email": "",
        u"注册资金": "",
        u"经营方式": "",
        u"主营行业": "",
        u"主营产品": "",
        u"职工人数": "",
        u"年销售额": "",
        u"成立时间": "",
        u"网址": "",
    }
    global l

    table = f.sheets()[0]
    # nrow = table.nrows
    # print nrow
    # for hang in (1, nrow):

    # print '\n'.join(table.row_values(0))
    # print '\n'.join(table.row_values(1))
    for x in table.row_values(0):
        if x not in l:
            print x
            l.append(x)

if __name__ == '__main__':

    l = [
        u"单位名称",
        u"电话",
        u"传真",
        u"移动电话",
        u"负责人",
        u"联系人",
        u"职位",
        u"地址",
        u"邮政编码",
        u"经济类型",
        u"email",
        u"注册资金",
        u"经营方式",
        u"主营行业",
        u"主营产品",
        u"职工人数",
        u"年销售额",
        u"成立时间",
        u"网址",
    ]
    data = {
        "name": "",
        "dizhi": "",
        "youbian": "",
        "fuzeren": "",
        "lianxiren": "",
        "guhua": "",
        "shouji": "",
        "chuanzhen": "",
        "type": "",
        "zhuceziben": "",
        "renshu": "",
        "chenglishijian": "",
        "zhuyinghangye": "",
        "zhuyingchanpin": "",
        "yingyee": "",
        "wangzhan": "",
        "jingyingfangshi": ""
    }
    rootdir = r"E:\360Downloads\08"
    for x in walk_file(rootdir):
        # print x.decode("gbk")
        try:
            file = xlrd.open_workbook(x)
        except:
            pass
        year = 0
        if "2011" in x:
            year = 2011
        elif "2012" in x:
            year = 2012
        else:
            pass
        excel2dict(year, file, data)
        # break
