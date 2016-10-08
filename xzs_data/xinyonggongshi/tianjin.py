#coding:utf-8
from . import Analyze
import re
import requests

class TianJinAnalyze(Analyze):
    def __init__(self, id=None, name=None):
        if id:
            self.id = id
        elif name:
            self.name = name
            # self.id = self.getid(self.name)
        else:
            print("Must input a company's id or name")

        self.dengjijinxi =


