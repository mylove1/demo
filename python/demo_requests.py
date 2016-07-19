# coding=utf-8

import requests

# [编码]
r = requests.get("http://www.11467.com")
print r.text.encode('latin1').decode('gbk')

# [指定编码方式]
r = requests.get("http://www.11467.com")
r.encoding='gbk'
print r.text


# url = 'http://httpbin.org/get'
# geturl = 'http://httpbin.org/headers'
# posturl = 'http://httpbin.org/post'
# payload = dict(key1='value1', key2='value2')
# data = dict(key='value')
# headers = {
#     'content-type': 'application/json',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'
#     }


# [Session]
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookies/456123')
# r = s.get("http://httpbin.org/cookies")
# r = s.post(loginURL, data=postData)

# jsonStr = r.content.decode('gbk')
# info = json.loads(jsonStr)

# print(r.text)
# print(r.request)

# cookie = s.cookies.get_dict()


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

# print('------------------------')
# r = requests.get('http://httpbin.org/ip')
# # r.url
# # r.status_code
# # r.encoding
# # r.history #返回列表
# # print r.text
# # print r.json
# print r.elapsed                 # 0:00:03.997000
# print r.elapsed.seconds         # 3
# print r.elapsed.microseconds    # 997000
# print r.elapsed.total_seconds() # 3.997
# print r.elapsed.days            # 0
# print r.elapsed.max             # 999999999 days, 23:59:59.999999
# print r.elapsed.min             # -999999999 days, 0:00:00
# print r.elapsed.resolution      # 0:00:00.000001

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