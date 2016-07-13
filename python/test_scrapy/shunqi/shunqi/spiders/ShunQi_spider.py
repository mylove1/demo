# -*- coding:utf-8 -*-

import scrapy
from shunqi.items import ShunqiItem
import json


with open('city_count.json', 'r') as f:
    j = json.loads(''.join(f.readlines()))
searchsheng = \
u"浙江"
searchcity = \
u"丽水"

for x in range(0,len(j)):
    if j[x]["shi"] == searchcity:
        cityurl = j[x]["url"]
        citycount = int(j[x]["count"])
        break
        # citycount = 100




class ShunQi_spider(scrapy.Spider):
    name = "shunqi"
    allowed_domains = ["11467.com"]
    start_urls = [cityurl + 'co/' + str(x) + '.htm' for x in xrange(1,citycount+1)]

    def parse(self, response):
        item = ShunqiItem()
        sheng = searchsheng
        shi = searchcity
        url = response.url
        name = response.xpath('//title/text()').extract()[0]



        item['name'] = name
        item['shi'] = shi
        item['sheng'] = sheng
        item['url'] = url
        return item


        # item = ShunqiItem()
        # sheng = response.xpath('//strong[2]/text()').extract()[0][0:-4]
        # shi = response.xpath('//title/text()').extract()[0][0:-6]
        # stop = -37 - len(shi)
        # count = response.xpath('//div[@id="nav"]/span/text()').extract()[0][3:stop]
        # url = response.url
        # item['sheng'] = sheng
        # item['shi'] = shi
        # item['count'] = count
        # item['url'] = url
        # return item



        # shi = response.xpath('//title/text()').extract()[0][0:-6]
        # count = response.xpath('//div[@id="nav"]/span/text()').extract()[0][3:-39]
        # url = response.url
        # print shi
        # print count
        # print url


























