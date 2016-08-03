# coding:utf-8
import requests
import random
from selenium import webdriver
import config
browser = webdriver.PhantomJS(executable_path=r"D:\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe")
url = "http://www.tianyancha.com/company/78957398"

headers = {
    'User-Agent': random.choice(config.agents),
    'Referer': 'http://www.creditchina.gov.cn/',
    'Connection': 'keep-alive',
}
browser.get(url)
html = browser.execute_script("return document.documentElement.outerHTML")
print html
