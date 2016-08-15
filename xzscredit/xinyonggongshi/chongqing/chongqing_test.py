# coding:utf-8
import requests
import time
import pymongo
import json

DbConfig = {
 # db config
 'user': 'root',
 'passwd': 'dingyu',
 'db': 'dingyu',
 'host': '192.168.0.102',
}


def get_html(url):
    while 1:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
                'Referer': 'http://gsxt.cqgs.gov.cn/',
            }
            r = requests.get(url, headers=headers)
            r.encoding = "utf-8"
            return r.text
        except:
            pass


if __name__ == '__main__':
    conn = pymongo.Connection('192.168.100.55', 27017)
    db = conn.chongqing
    for page in range(816, 8904):
        print page
        url = "http://gsxt.cqgs.gov.cn/search_searchjyyc.action?currentpage=%s&itemsperpage=10" % page


        # print url
        text = get_html(url)
        jsontext = json.loads(text)
        for x in jsontext["jyyclist"]:
            d = {}
            d["name"] = x["_name"]
            d["regcode"] = x["_regCode"]
            d["pripid"] = x["_pripid"]
            db.namelist.insert(d)
