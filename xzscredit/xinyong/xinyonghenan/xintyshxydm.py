# coding:utf-8
import requests
import json
import pymongo
import config


url = "http://222.143.254.138:8704/DataQuery/temp/getCreditCodeList.json"

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '29',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': '222.143.254.138:8704',
    'Origin': 'http://222.143.254.138:8704',
    'Referer': 'http://222.143.254.138:8704/DataQuery/temp/creditCodeIndex?codeType=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

conn = pymongo.Connection(config.master, 27017)
db = conn.xinyonghenan
for page in xrange(1, 27):
    # codeType为1：新赋代码，2旧码转换
    data = {
        'codeType': '2',
        'page': str(page),
        'pageSize': '10000'
    }
    r = requests.post(url, headers=headers, data=data)
    text = r.text
    text = json.loads(text)
    for x in text["list"]:
        db.tyshxydm.insert(x)
    print '------------->    ',page