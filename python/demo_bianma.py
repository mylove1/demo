# coding:utf-8
import urllib2
import requests


def encoding(data):
    types = ['utf8','gb2312','gbk']
    for type in types:
        try:
            return data.decode(type)
        except:
            pass
    return None
url='http://www.11467.com'

# # 现在测试只能用urllib2，在requests下出错
# res=urllib2.urlopen(url)
# data=encoding(res.read())
# print(data)

# # 在requests下出错
# res=requests.get(url)
# data=encoding(res.text)
# print(data)

# # 在requests下：解决方法
r = requests.get(url)
print r.encoding
r.encoding = 'gbk'
print r.text
# print type(r.text)
# print r.text.encode('latin1').decode('gbk')
