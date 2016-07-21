# coding:utf-8

#### 样式一
# import urllib2
# opener = urllib2.build_opener()
# opener.addheaders.append(('Cookie','cookiename=cookievalue'))
# f = opener.open('http://httpbin.org/headers')
# 返回样式
# {
#   "headers": {
#     "Accept-Encoding": "identity",
#     "Cookie": "cookiename=cookievalue",
#     "Host": "httpbin.org",
#     "User-Agent": "Python-urllib/2.7"
#   }
# }


#### 样式二
import urllib2
import urllib
from cookielib import CookieJar

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# input-type values from the html form
formdata = {"username": 'cui', "password": '234', "form-id": "1234"}
data_encoded = urllib.urlencode(formdata)
response = opener.open("http://httpbin.org/headers", data_encoded)
content = response.read()
print content

