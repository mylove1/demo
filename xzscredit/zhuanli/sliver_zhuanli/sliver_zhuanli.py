# coding:utf-8
import time
import random
import requests
import threading
from selenium import webdriver
import json
import re
import config

class ZhuanliCrawl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.agent = config.agents
        self.service_args = [
            '--load-images=false',
        ]
        self.browser = webdriver.PhantomJS(
            executable_path=r"D:\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe", service_args=self.service_args)
        self.browser.set_page_load_timeout(20)

    def get_html(self, url):
        while 1:
            this_headers = {
                'User-Agent': random.choice(self.agent),
                'Referer': 'cpquery.sipo.gov.cn',
                'Connection': 'keep-alive',
            }
            try:
                # proxy = requests.get('http://192.168.0.100:8384/ip').text
                r = requests.get(url, headers=this_headers)# , proxies={'http': proxy},
                                  # timeout=7)
                break
            except:
                pass
        return r

    def phantom(self, url):
        while 1:
            try:
                self.browser.get(url)
                time.sleep(1)
                html = self.browser.execute_script("return document.documentElement.outerHTML")
                html = ''.join(html.split()).encode('utf-8')
                datas = re.findall('title="发明专利">(.*?)</span>.*?record:zhuanlimc"title="(.*?)">.*?record:shenqingrxm"title="(.*?)">.*?record:shenqingr"class="text_ellipsis"title="(.*?)">.*?record:zhufenlh"title="(.*?)">', html)
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


    def put_mess(self, mess):
        requests.post('http://192.168.100.55:7474/post', data=mess)



    def get_kw(self):
        r = requests.get('http://192.168.100.55:7474/comp')
        return r.text



    def run(self):
        while True:
            key = self.get_kw()
            # key = '华为技术有限公司'
            try:
                print key
            except:
                continue
            if key == '':
                time.sleep(10)
                continue
            url = 'http://cpquery.sipo.gov.cn//txnQueryOrdinaryPatents.do?select-key%3Ashenqingh=&select-key%3Azhuanlimc=&select-key%3Ashenqingrxm=' + key + '&select-key%3Azhuanlilx=&select-key%3Ashenqingr_from=&select-key%3Ashenqingr_to=&attribute-node:record_start-row=1&attribute-node:record_page-row=100&'
            response = self.get_html(url)
            if 'empty_date' not in response.text:
                text = ''.join(response.text.split())
                pages = re.findall("data-totalpage='(.*?)'data-currentpage='(.*?)'", text)
                try:
                    totalpage = int(pages[0][0])
                except:
                    continue
                url = str(response.url)
                for page in range(1, totalpage + 1):
                    print '-----------------------------', key, '-------', page
                    next_row = 'start-row=' + str(page * 100 - 99)
                    next_url = url.replace('start-row=1', next_row)
                    self.phantom(next_url)
            else:
                print key, 'kong'


        # print 'start run'

        #     url = 'http://cpquery.sipo.gov.cn//txnQueryOrdinaryPatents.do?select-key%3Ashenqingh=&select-key%3Azhuanlimc=&select-key%3Ashenqingrxm=' + key + '&select-key%3Azhuanlilx=&select-key%3Ashenqingr_from=&select-key%3Ashenqingr_to=&attribute-node:record_start-row=1&attribute-node:record_page-row=100&'
        #     response = self.get_html(url)
        #     if 'empty_date' not in response.text:
        #         text = ''.join(response.text.split())
        #         pages = re.findall("data-totalpage='(.*?)'data-currentpage='(.*?)'", text)
        #         totalpage = int(pages[0][0])
        #         url = str(response.url)
        #         for page in range(1, totalpage + 1):
        #             print '------------------------------------------------------------------------------------------------------------------', page
        #             next_row = 'start-row=' + str(page * 100 - 99)
        #             next_url = url.replace('start-row=1', next_row)
        #             self.phantom(next_url)



def main():
    for x in xrange(5):
        thread = ZhuanliCrawl()
        thread.start()

if __name__ == '__main__':
    # time.sleep(3600)
    main()
