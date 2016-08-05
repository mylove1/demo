# coding:utf-8
import requests
import random
from selenium.webdriver.common.proxy import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import config
import time
import urllib2
import cookielib

# [搜索关键词使用cookie]
# urla = 'http://www.tianyancha.com'
# urlb = 'http://www.tianyancha.com/search/%E6%9D%AD%E5%B7%9E%E9%93%B6%E8%A1%8C%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8?checkFrom=searchBox'
# proxy = requests.get('http://192.168.0.100:8384/ip').text
# print proxy
# headersa = {
#     'Host': 'www.tianyancha.com',
#     'Connection': 'keep-alive',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': random.choice(config.agents),
#     'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
# }
# r = requests.get(urlb, headers=headersa, proxies={'http': proxy})
# r.encoding = 'utf8'
# print r.text
# print r.cookies













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
# url = 'http://www.tianyancha.com/search/%E6%9D%AD%E5%B7%9E%E9%93%B6%E8%A1%8C%E8%82%A1?checkFrom=searchBox'
# proxy = requests.get('http://192.168.0.100:8384/ip').text
# headers = {
#     'User-Agent': random.choice(config.agents),
#     'Referer': 'http://www.tianyancha.com/',
#     'Connection': 'keep-alive',
# }
# r = requests.get(url, headers=headers, proxies={'http': proxy})
# print r.text






for x in range(1):

    myProxy = requests.get('http://192.168.0.100:8384/ip').text
    print myProxy
    service_args = [
        # '--proxy=' + myProxy,
        '--proxy=119.6.136.122:83'
        '--proxy-type=http',
        '--load-images=false',
        ]


    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        random.choice(config.agents)
    )
    browser = webdriver.PhantomJS(executable_path=r"D:\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe",
                                  service_args=service_args,
                                  desired_capabilities=dcap)
    print '0'
    url = "http://www.tianyancha.com/company/78957398"
    url = 'http://www.tianyancha.com/search/%E6%9D%AD%E5%B7%9E%E9%93%B6%E8%A1%8C%E8%82%A1?checkFrom=searchBox'
    # url = 'http://www.tianyancha.com/company/526616406'
    # url = 'http://www.tianyancha.com/company/78957398'
    # url = 'http://httpbin.org/headers'

    # headers = {
    #         'Host': 'www.tianyancha.com',
    #         'Connection': 'keep-alive',
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #         'Upgrade-Insecure-Requests': '1',
    #         'Accept-Encoding': 'gzip, deflate',
    #         'Accept-Language': 'zh-CN,zh;q=0.8',
    # }
    print '1'
    # browser.get(url)
    browser.set_page_load_timeout(20)
    try:
        browser.get(url)
        time.sleep(2)
        html = browser.execute_script("return document.documentElement.outerHTML")
        print html
    except TimeoutException:
        print 'time out after 30 seconds when loading page'
        browser.execute_script('window.stop()')
    finally:
        browser.quit()
