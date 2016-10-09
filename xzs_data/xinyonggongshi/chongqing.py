#coding:utf-8
from __init__ import Analyze
from pprint import pprint
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

        self.dengjijinxi =''



if __name__ == '__main__':
    url = "http://gsxt.cqgs.gov.cn/search_getEnt.action?_c1475992115348=_c414255&entId=5001031201601141331706&id=500103008520659&stype=SAIC&type=1"
    a = TianJinAnalyze(id=23)
    pprint(a.info)