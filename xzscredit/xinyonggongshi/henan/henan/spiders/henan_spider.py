# coding=utf-8
import scrapy
import re
from henan.items import HenanItem
import MySQLdb
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor


class Henan_Spider(CrawlSpider):
    name = 'henan'
    allowed_domains = ['http://222.143.24.157']
    start_urls = ['http://222.143.24.157/businessPublicity.jspx?id=33D1559F7E785FA4E053050A080AED3E',
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow=(u'/business.*',)), follow=True, callback='gongshanggongshi_item'),
        Rule(SgmlLinkExtractor(allow=(u'/enterp.*', )), follow=True, callback='qiyegongshi_item'),
    ]

    def parse_item(self, response):
        pass

    def gongshanggongshi_item(self, response):
        item = HenanItem()
        item["url"] = response.url
        return item

    def qiyegongshi_item(self, response):
        item = HenanItem()
        item["url"] = response.url
        return item

