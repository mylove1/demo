# coding:utf-8
import requests
import random

authorization = [
    'Wwj5J89EGx63lR1uv5R17rV3BONnuEPdaqkW8+T6N6calCNpOE0TFYM11et2Ugkd',
    'Wwj5J89EGx63lR1uv5R17oPdrTS46mg6EZHLLYoSDjfu/IImwKIDg1h85raFdJg1',
]

url = 'http://api.tianyancha.com/services/v3/search/华为.json?pageNum=1&pageSize=15&base=&category='
headers = {
    'X-Auth-Token': '',
    'Content-Type': 'application/json',
    'version': 'Android 1.2.20',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1; m2 Build/LMY47D)',
    'Host': 'api.tianyancha.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
            }
r = requests.get(url, headers=headers)
for x in r.cookies:
    print x
print r.text


# [关键词搜索：可用]
# url = 'http://api.tianyancha.com/services/v3/search/华为.json?pageNum=1&pageSize=15&base=&category='
# headers = {
#     'X-Auth-Token': '',
#     'Content-Type': 'application/json',
#     'Authorization': random.choice(authorization),
#     'version': 'Android 1.2.20',
#     'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1; m2 Build/LMY47D)',
#     'Host': 'api.tianyancha.com',
#     'Connection': 'Keep-Alive',
#     'Accept-Encoding': 'gzip',
#             }
# r = requests.get(url, headers=headers)
# print r.text