# -*- coding:utf-8 -*-
import scrapy
import re
from selenium import webdriver
# from zhuanli.urllist import urllist
from zhuanli.items import ZhuanliItem
from scrapy.http import Request
from zhuanli.urllist import urllist




class ZhuanliSpider(scrapy.Spider):
    def __init__(self):
        self.browser = webdriver.PhantomJS(executable_path=r"D:\PhantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    name = "zhuanli"
    # start_urls = urllist
    start_urls = urllist
    def parse(self, response):
        if 'empty_date' not in response.text:
            text = ''.join(response.text.split())
            pages = re.findall("data-totalpage='(.*?)'data-currentpage='(.*?)'", text)
            totalpage = int(pages[0][0])
            url = str(response.url)
            for page in range(1, totalpage+1):
                print '------------------------------------------------------------------------------------------------------------------', page
                next_row = 'start-row=' + str(page * 100 - 99)
                next_url = url.replace('start-row=1', next_row)
    #             return self.phantom(next_url)
    #
    # def phantom(self, url):
    #     self.browser.get(url)
    #     # time.sleep(3)
    #     html = self.browser.execute_script("return document.documentElement.outerHTML")
    #     html = ''.join(html.split()).encode('utf-8')
    #     datas = re.findall('title="发明专利">(.*?)</span>.*?record:zhuanlimc"title="(.*?)">.*?record:shenqingrxm"title="(.*?)">.*?record:shenqingr"class="text_ellipsis"title="(.*?)">.*?record:zhufenlh"title="(.*?)">', html)
    #     items = []
    #     for x in datas:
    #         item = ZhuanliItem()
    #         item["company"] = x[2]
    #         item["number"] = x[4]
    #         item["type"] = x[0]
    #         item["name"] = x[1]
    #         item["date"] = x[3]
    #         items.append(item)
    #     return items


            #     print 'this url is \t', response.url
            #     url = str(response.url)
            #     url = url.replace(start_row, next_row)
            #     print 'the next url is ', url
            #     yield Request(url=url, callback=self.parse)
            # print '---------------', totalpage, '-----------------'
            # print '---------------', currentpage, '-----------------'
            # print '---------------', pages, '-----------------'
            # print '\n\n\n'
            # print '----------------------------------',len(text),'--------------------------'



        """
        re_a = re.compile('''businessPublicity.*?id=(.*?)&sourceType.*?et=_blank>(.*?)</a>.*?"tb-a2">(.*?)&nbsp''')
        items = []
        for i in re_a.findall(txt):
            item = HnqyxyItem()
            if ' ' in i:
                continue
            else:
                item['url'] = 'http://222.143.24.157/bussinessPublicity.jspx?id=' + i[0].strip() + '&sourceType=1'
                item['name'] = i[1].strip()
                item['numb'] = i[2].strip()
                items.append(item)
        return items


        re_a = re.compile('''<div class="tb-[!a]".*?businessPublicity\.jspx\?id=(.*?)&sourceType=1.*?"tb-a2">(.*?)&nbsp;</li>''')
        for url in response.xpath('//div[@class!="tb-a"]/ul/li[@class="tb-a2"]/text()').extract():
            print url



//div/ul/li[1]/a/@href
//div[@class!="tb-a"]/ul/li[1]/a/@href
        txt = response.text
        re_a = re.compile('''<li class="tb-a1"><a href="(.*?)" target=_blank>(.*?)</a>&nbsp;</li><li class="tb-a2">(.*?)&nbsp;</li><li class="tb-a3">(.*?)</li>''')
        for i in re_a.findall(txt):
            if ' ' in i:
                continue
            else:
                print i[0]

        for url in response.xpath('//div/ul/li[1]/a/@href').extract():
            url =urlparse.urljoin("http://222.143.24.157", url)
            yield scrapy.Request(url, callback=self.parse_item)

def parse_item(self, response):
        pass
class HnqyxySpider(scrapy.Spider):
    name = "hnqyxy"
    start_urls = ["http://222.143.24.157/businessPublicity.jspx?id=35C07BE8C59F9C31E053050A080AC22E&sourceType=1"]

    def parse(self, response):
        txt = response.text
        cc = self.re_dict(txt)
        for i in cc:
            print i
    def re_dict(self, txt):
        re_No = re.compile('''<td width="30%">(.*?)</td>''')
        return re_No.findall(txt)
"""


