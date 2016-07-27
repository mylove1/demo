# coding:utf-8
import time
# from urllib import request
from lxml import etree
import re
from selenium import webdriver

url = "http://httpbin.org/headers"
url = "http://cpquery.sipo.gov.cn//txnQueryOrdinaryPatents.do?select-key%3Ashenqingh=&select-key%3Azhuanlimc=&select-key%3Ashenqingrxm=%E5%8D%8E%E4%B8%BA%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&select-key%3Azhuanlilx=&select-key%3Ashenqingr_from=&select-key%3Ashenqingr_to=&attribute-node:record_start-row=41&attribute-node:record_page-row=10&"
browser = webdriver.PhantomJS(executable_path=r"D:\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe")
browser.get(url)
# time.sleep(3)
html = browser.execute_script("return document.documentElement.outerHTML")
print ''.join(html.split())
datas = re.findall(
    '"title="发明专利">(.*?)</span>.*?record:zhuanlimc"title="(.*?)">.*?record:shenqingrxm"title="(.*?)">.*?record:shenqingr"class="text_ellipsis"title="(.*?)">.*?record:zhufenlh"title="(.*?)">',
    html)
print datas
for x in datas:
    print x

