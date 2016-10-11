#!/usr/bin/env python
# coding:utf-8

import xlrd
import os


if __name__ == '__main__':
    rootdir = "E:\\360Downloads\\08\\"
    for parent,dirnames,filenames in os.walk(rootdir):
        for x in filenames:
            print x.encode("utf-8")
