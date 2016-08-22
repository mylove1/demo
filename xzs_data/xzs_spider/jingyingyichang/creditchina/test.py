# coding:utf-8
import requests
import time
import json

kw = '平煤神马建工集团'
data = {
    'keyword': kw,
    'searchtype': '0',
    'objectType': '2',
    'areas': '',
    'creditType': '',
    'dataType': '1',
    'areaCode': '',
    'templateId': '',
    'exact': '0',
    'page': '2',
    'pagesize': '20'
}

headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '173',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.creditchina.gov.cn',
    'Origin': 'http://www.creditchina.gov.cn',
    'Referer': 'http://www.creditchina.gov.cn/search_all',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
url = 'http://www.creditchina.gov.cn/credit_info_search?t=' + ''.join(str('%.3f' % time.time()).split('.'))
# url = 'http://www.creditchina.gov.cn/credit_info_search?t=1471836362883'

r = requests.post(url, headers=headers, data=data)
j = json.loads(r.text)
for page in range(1,(j["result"]["totalPageCount"])):
    print page + 1






# def toinfo():
#     r = requests.post(url, headers=headers, data=data)
#     j = json.loads(r.text)
#     # print r.text
#     for x in (j["result"]["results"]):
#         yield x
# for y in toinfo():
#     print y["objectType"]