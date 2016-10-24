#!/usr/bin/env python
# coding:utf-8

import xlrd
import os

def walk_file(rootdir):
    for parent,dirnames,filenames in os.walk(rootdir):
        for x in filenames:
            yield os.path.join(parent, x).replace("\\", "\\\\")

def excel2dict(f, data):
    table = f.sheets()[0]
    print table.nrows

if __name__ == '__main__':
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
        print x
        file = xlrd.open_workbook(x)
        excel2dict(file, data)
        break
