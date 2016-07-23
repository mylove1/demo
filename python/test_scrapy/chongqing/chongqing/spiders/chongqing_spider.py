# -*- coding:utf-8 -*-
import scrapy
from chongqing.items import ChongqingItem
from scrapy.http import Request

def dict_jyyc_url_list(dic):
    jyyc_url_list = []
    for x in dic["jyyclist"]:
        url = "http://gsxt.cqgs.gov.cn/search_getEnt.action?_c1469155905658=_c205102&entId=" + x["_pripid"] + "&id=" + x["_regCode"] + "&stype=SAIC&type=1"
        jyyc_url_list.append(url)
    return jyyc_url_list

class ChongqingSpider(scrapy.Spider):
    name = "chongqing"
    start_urls = ["http://gsxt.cqgs.gov.cn/search_searchjyyc.action?currentpage=" + str(x) + "&itemsperpage=10" for x in xrange(1,2)]

    def parse(self, response):
        text = response.text
        name_dict = dict(eval(text))
        jyyc_url_list = dict_jyyc_url_list(name_dict)
        for x in jyyc_url_list:
            yield Request(x, callback=self.search_getEnt)

    def search_getEnt(self, response):
        text = response.text[6:]
        return text
        # item = ChongqingItem()
        # text = response.text
        # item["xinxi"] = text[6:]
        # return item













        # re_a = re.compile('''businessPublicity.*?id=(.*?)&sourceType.*?et=_blank>(.*?)</a>.*?"tb-a2">(.*?)&nbsp''')
        # items = []
        # for i in re_a.findall(txt):
        #     item = HnqyxyItem()
        #     if ' ' in i:
        #         continue
        #     else:
        #         item['url'] = 'http://222.143.24.157/bussinessPublicity.jspx?id=' + i[0].strip() + '&sourceType=1'
        #         item['name'] = i[1].strip()
        #         item['numb'] = i[2].strip()
        #         items.append(item)
        # return items



