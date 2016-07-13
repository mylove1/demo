import scrapy
import re


class CooperProxyText(scrapy.Spider):
    name = "cooper_proxy_test"
    start_urls = ['http://httpbin.org/ip',
                  'http://httpbin.org/ip',
                  'http://httpbin.org/ip',
                  # 'http://httpbin.org/ip',
                  # 'http://httpbin.org/ip',
                  # 'http://httpbin.org/ip',
                  # 'http://httpbin.org/ip',
                  # 'http://httpbin.org/ip',
                  # 'http://httpbin.org/ip',
                  # 'http://httpbin.org/ip',
                  # 'http://httpbin.org/ip',
                  # 'http://httpbin.org/ip',
                  ]

    def parse(self, response):
        print response.text
