#coding:utf-8

import re
import requests

class Analyze():
    def get_id(self, name):
        pass

    def get_html(self, url):
        r = requests.get(url)

    def data(self):
        info = {
            "baseinfo":{
                "comp_name": "",
                "comp_type": "",
                "creditcode": "",
            }
        }
        return info