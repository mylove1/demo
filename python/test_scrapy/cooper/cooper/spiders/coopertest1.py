# -*- coding:utf-8 -*-
import scrapy
import re
from cooper.items import CooperItem

class HnqyxySpider(scrapy.Spider):
    name = "coopertest1"
    start_urls = [("http://222.143.24.157/exceptionInfoSelect.jspx?pageNo="+str(i)) for i in xrange(1,10)]

    def parse(self, response):
        item = CooperItem()
        #txt = response.text.replace('\n', ' ')
        #re_a = re.compile('''businessPublicity.*?id=(.*?)&sourceType.*?"tb-a2">(.*?)&nbsp''')
        #items = []
        #for i in re_a.findall(txt):
        #    item = HnqyxyItem()
        #    if ' ' in i:
        #        continue
        #    else:
        #        item['link'] = i[0]
        #        item['numb'] = i[1]
        #        items.append(item)
        print response.xpath('//div[@class="tb-b"]/ul/li/a/text()').extract()[0]


"""
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


