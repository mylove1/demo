# coding:utf-8
'''
   guobanjia 大概10分钟可以运行一次，
   每一次会自动过滤掉本地IP池中有的ip
'''
import requests
import re
import time
import threading
import pymongo
import socket
from selenium import webdriver
import pybloom


IP = socket.gethostbyname(socket.gethostname())
mongoPORT = 27017


def link_mongo():
    conn = pymongo.Connection(IP, mongoPORT)
    db = conn.ip
    return db


def get_html(url):
    headers = {
        'Host': 'proxy.goubanjia.com',
        'Connection': 'keep-alive',
        'Referer': 'http://proxy.goubanjia.com/free/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    return ''.join(r.text.split())


def main():
    browser = webdriver.PhantomJS(
        executable_path=r"D:\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe", service_args=self.service_args)
    browser.set_page_load_timeout(20)

    # db = link_mongo()
    # f = pybloom.BloomFilter(capacity=100000, error_rate=0.0001)
    # for x in db.bigpool.find():
    #     f.add(x["ip"])

    url = 'http://proxy.goubanjia.com/free/gngn/index.shtml'
    while 1:
        try:
            self.browser.get(url)
            time.sleep(1)
            html = self.browser.execute_script("return document.documentElement.outerHTML")
            html = ''.join(html.split()).encode('utf-8')
            datas = re.findall(
                'title="发明专利">(.*?)</span>.*?record:zhuanlimc"title="(.*?)">.*?record:shenqingrxm"title="(.*?)">.*?record:shenqingr"class="text_ellipsis"title="(.*?)">.*?record:zhufenlh"title="(.*?)">',
                html)
            items = []
            for x in datas:
                item = {}
                item["company"] = x[2]
                item["number"] = x[4]
                item["type"] = x[0]
                item["name"] = x[1]
                item["date"] = x[3]
                items.append(item)
            # print json.dumps(items)
            self.put_mess({"comp": str(items)})
            break
        except:
            '---------------browser 获取网页出错--------------'
    # while 1:
    html = get_html(url)
    r = [
        '''<pstyle="display:none;">.</p>''',
        '''<pstyle="display:none;">.1</p>'''
    ]
    for txt in r:
        html = html.replace(txt, '')
    r = [
        '''<span>''',
        '''<spanstyle='display:inline-block;'>''',
        '''</span>''',
        '''</div>''',
        '''<divstyle='display:inline-block;'>''',
        '''<pstyle='display:none;'></p>''',
        '''</td><tdclass="''',
        '''<pstyle='display:none;'>''',
        '''</p>''',

    ]
    for txt in r:
        html = html.replace(txt, '')
    print html


if __name__ == '__main__':
    main()