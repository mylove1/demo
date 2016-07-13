# coding:utf-8
import requests

url = "http://www.tianyancha.com/search/page/5?base=%E6%B5%99%E6%B1%9F&filterType=prov"
p = requests.get(url)
print p.cookies
print p.text
print p.headers
print p.url