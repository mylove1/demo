#coding=utf-8
import scrapy


class Login_Zhihu_Spider(scrapy.Spider):
    name = 'login_zhihu'
    allowed_domains = ["www.zhihu.com"]
    def __init__(self):
