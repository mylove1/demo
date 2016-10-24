#!/usr/bin/env python
# coding:utf-8

import pymongo
import MySQLdb

class mult_insert():
    def __init__(self, lenth=1000):
        self.list = []
        self.lenth = lenth
        pass

    def append(self, l):
        self.list.append(l)
        if len(self.list) >= self.lenth:
            self.insert()

