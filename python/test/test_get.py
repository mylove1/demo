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
url = 'http://www.tianyancha.com/annualreport/newReport.json?id=78957398&year=2015'
headers = {
            'Host': 'www.tianyancha.com',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
    }
r = requests.get(url, headers=headers)
print r.text