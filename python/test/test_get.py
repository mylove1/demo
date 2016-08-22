# coding:utf-8
import requests
import random
from selenium import webdriver
import config
# browser = webdriver.PhantomJS(executable_path=r"D:\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe")
# url = "http://www.tianyancha.com/company/78957398"
#
# headers = {
#     'User-Agent': random.choice(config.agents),
#     'Referer': 'http://www.creditchina.gov.cn/',
#     'Connection': 'keep-alive',
# }
# browser.get(url)
# html = browser.execute_script("return document.documentElement.outerHTML")
# print html

# Host: dis.tianyancha.com
# Connection: keep-alive
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
# Accept-Encoding: gzip, deflate, sdch
# Accept-Language: zh-CN,zh;q=0.8



# url = 'http://dis.tianyancha.com/dis/getInfoById/1698375.json'
# headers = {
# 'Host': 'dis.tianyancha.com',
# 'Connection': 'keep-alive',
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
# 'Accept-Encoding': 'gzip, deflate, sdch',
# 'Accept-Language': 'zh-CN,zh;q=0.8',
#     }
# r = requests.get(url, headers=headers)
# print r.text


# url = 'http://www.creditchina.gov.cn/credit_info_search?t=1470375459690'
# headers = {
# 'Host': 'www.creditchina.gov.cn',
# 'Connection': 'keep-alive',
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
# 'Accept-Encoding': 'gzip, deflate, sdch',
# 'Accept-Language': 'zh-CN,zh;q=0.8',
#     }
# data = {'keyword':'平顶山市科远网络技术',
#         'searchtype':'0',
#         'objectType':'2',
#         'areas': '',
#         'creditType':'',
#         'dataType':'1',
#         'areaCode':'',
#         'templateId': '',
#         'exact':'0',
#         'page':'1'
# }
# r = requests.post(url, headers=headers,)
# print r.text


url = 'http://whois.aizhan.com/reverse-whois?q=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4&t=registrant'
r = requests.get(url)
print r.status_code
print r.text















