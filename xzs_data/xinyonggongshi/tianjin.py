#coding:utf-8
from __init__ import Analyze
import re
import requests

class TianJinAnalyze(Analyze):
    def __init__(self, id=None, name=None):
        self.info = self.data()
        if id:
            self.id = id
        elif name:
            self.name = name
            # self.id = self.getid(self.name)
        else:
            print("Must input a company's id or name")

        # self.dengjijinxi =


if __name__ == '__main__':
    a = TianJinAnalyze(id=33333)
    print a.info