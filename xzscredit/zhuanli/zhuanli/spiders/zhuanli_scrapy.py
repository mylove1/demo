# -*- coding:utf-8 -*-
import scrapy
import re
# from zhuanli.urllist import urllist
# from zhuanli.items import ZhuanliItem
from scrapy.http import Request

class ZhuanliSpider(scrapy.Spider):
    name = "zhuanli"
    # start_urls = urllist
    start_urls = ['http://cpquery.sipo.gov.cn//txnQueryOrdinaryPatents.do?select-key%3Ashenqingh=&select-key%3Azhuanlimc=&select-key%3Ashenqingrxm=%E5%8D%8E%E4%B8%BA%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&select-key%3Azhuanlilx=&select-key%3Ashenqingr_from=&select-key%3Ashenqingr_to=&attribute-node:record_start-row=11&attribute-node:record_page-row=10&',
                  'http://cpquery.sipo.gov.cn//txnQueryOrdinaryPatents.do?select-key%3Ashenqingh=&select-key%3Azhuanlimc=&select-key%3Ashenqingrxm=%E5%8D%8E%E4%B8%BA%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&select-key%3Azhuanlilx=&select-key%3Ashenqingr_from=&select-key%3Ashenqingr_to=&attribute-node:record_start-row=41&attribute-node:record_page-row=10&',
                  ]
    def parse(self, response):
        if 'empty_date' not in response.text:
            text = ''.join(response.text.split())
            print text
            pages = re.findall("data-totalpage='(.*?)'data-currentpage='(.*?)'", text)
            totalpage = int(pages[0][0])
            currentpage = int(pages[0][1])
            if totalpage > currentpage:
                start_row = 'start-row' + str(currentpage * 10 - 9)
                next_row = 'start-row' + str(currentpage * 10 + 1)
                url = response.url.replace('start_row', 'next_row')
                print 'the url is ', url
                yield Request(url=url, callback=self.parse)
            print '---------------', totalpage, '-----------------'
            print '---------------', currentpage, '-----------------'
            print '---------------', pages, '-----------------'
            print '\n\n\n',
            print response.url
            print '\n\n\n'


            print '----------------------------------\n--------------------------'



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


