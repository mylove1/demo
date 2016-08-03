# coding:utf-8
import requests
import random
from selenium.webdriver.common.proxy import *
from selenium import webdriver
import config
import urllib2
import cookielib
# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# r = opener.open('http://www.tianyancha.com/')
# r = opener.open('http://www.tianyancha.com/company/78957398.json')
# print r.read()

# [关键词提示]
# url = 'http://www.tianyancha.com/suggest/%E5%8F%91.json'
# headers = {
#     'User-Agent': random.choice(config.agents),
#     'Referer': 'http://www.creditchina.gov.cn/',
#     'Connection': 'keep-alive',
# }
# r = requests.get(url, headers=headers)
# print r.text


# [搜索关键词]
# url = 'http://www.tianyancha.com/search/杭州银行股份有限公司.json'
# proxy = requests.get('http://192.168.0.100:8384/ip').text
# headers = {
#     'User-Agent': random.choice(config.agents),
#     'Referer': 'http://www.creditchina.gov.cn/',
#     'Connection': 'keep-alive',
# }
# r = requests.get(url, headers=headers, proxies={'http': proxy})
# print r.text






# for x in range(10):
#
#     myProxy = requests.get('http://192.168.0.100:8384/ip').text
#     service_args = [
#         '--proxy=' + myProxy,
#         '--proxy-type=http',
#         ]
#     browser = webdriver.PhantomJS(executable_path=r"D:\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe", service_args=service_args)
#     print '0'
#     url = "http://www.tianyancha.com/company/78957398"
#     url = 'http://httpbin.org/ip'
#
#     headers = {
#         'User-Agent': random.choice(config.agents),
#         'Referer': 'http://www.creditchina.gov.cn/',
#         'Connection': 'keep-alive',
#     }
#     print '1'
#     browser.get(url)
#     html = browser.execute_script("return document.documentElement.outerHTML")
#     print html
