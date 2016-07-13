# coding=utf-8
# requests 模块

import requests

url = 'http://httpbin.org/get'
geturl = 'http://httpbin.org/headers'
posturl = 'http://httpbin.org/post'
payload = dict(key1='value1', key2='value2')
data = dict(key='value')
headers = {
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'
    }
# [Session]
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookies/456123')
r = s.get("http://httpbin.org/cookies")
print(r.text)
print(r.request)

# cookies = dict(cookies_are='working')
# files = {'file': open('report.xls', 'rb')}

# get
# params:在URL后端？后加参数
# cookies:传递cookies
# rg = requests.get(geturl, params=data, headers = headers, cookies=cookies, timeout=0.01)
# rg = requests.get(geturl, params=data)
# rg = requests.get('http://www.nailcui.com')

# post
# data:表单数据等需提交的数据
# files：上传多部分编码文件
# rp = requests.post(posturl, headers=headers, data=payload, files=files)
# rp = requests.post(posturl, headers=headers, data=payload)

# r = requests.put(url, data)
# r = requests.head(url)
# r = requests.delete('http://httpbin.org/delete')
# r = requests.options('http://httpbin.org/get')

print('------------------------')
# r.url
# r.status_code
# r.encoding
# r.history #返回列表
# r.text
# r.json

# print('get:', rg.status_code)
# print(rg.url)
# # print(rg.encoding)
# # rg.encoding = 'utf-8'
# print(rg.text)
# print(rg.json)
# print('-'*20)
# print('post:', rp.status_code)
# print(rp.text)
# print(rp.cookies)
# print(rp.history)

