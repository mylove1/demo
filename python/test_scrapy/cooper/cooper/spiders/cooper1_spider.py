# -*- coding:utf-8 -*-

import scrapy
from cooper.items import CooperItem



class CooperSpider(scrapy.Spider):
    name = "cooper1"
    allowed_domains = ["www.cooper.com"]
    start_urls = [
        "http://www.cooper.com"
    ]

    def parse(self, response):
        item = CooperItem()

        return item