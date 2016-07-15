# coding:utf-8
import time
# from urllib import request
from lxml import etree
from selenium import webdriver

url = "http://httpbin.org/headers"
url = "https://list.tmall.com/search_product.htm?q=%B7%E7%C9%C8&type=p&vmarket=&spm=875.7931836%2FA.a2227oh.d100&xl=feng_1&from=mallfp..pc_1_suggest"
browser = webdriver.PhantomJS(executable_path= \
    r"D:\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe")
browser.get(url)
time.sleep(3)
html = browser.execute_script("return document.documentElement.outerHTML")
print html
