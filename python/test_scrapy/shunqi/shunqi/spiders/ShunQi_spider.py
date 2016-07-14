# -*- coding:utf-8 -*-

import scrapy
from shunqi.items import ShunqiItem
import json


with open('city_count.json', 'r') as f:
    j = json.loads(''.join(f.readlines()))
# 取得{"sheng":["shi","shi2"]}样式的列表
city_dict_list = {}
for x in range(0, len(j)):
    city_dict_list[j[x]["sheng"]] = []
for x in range(0, len(j)):
    city_dict_list[j[x]["sheng"]].append(j[x]["shi"])
# 返回选择省份的所有地市的所有url列表
sheng_url_list = []
choice_sheng = u"山西"
for x in city_dict_list[choice_sheng]:
    for y in range(0, len(j)):
        if j[y]["shi"] == x:
            cityurl = j[y]["url"]
            citycount = int(j[y]["count"])
            break
    sheng_url_list.extend(cityurl + 'co/' + str(x) + '.htm' for x in xrange(1, citycount+1))




class ShunQi_spider(scrapy.Spider):
    name = "shunqi"
    allowed_domains = ["11467.com"]
    start_urls = sheng_url_list

    def parse(self, response):
        item = ShunqiItem()
        sheng = choice_sheng
        shi = response.xpath('//div[@id="sidebox"]/div[@class="box"][2]/h4[@class="boxtitle"]/text()').extract()[0][0:-4]
        url = response.url
        name = response.xpath('//title/text()').extract()[0]
        # print sheng
        # print shi
        # print url
        # print name


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


























