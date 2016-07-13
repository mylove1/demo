# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XizhiItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    tyshxy = scrapy.Field()
    zc = scrapy.Field()
    zzjg = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    faren = scrapy.Field()
    zhuceziben = scrapy.Field()
    jingyingriqi = scrapy.Field()
    yingyeqixian = scrapy.Field()
    fazhaoriqi = scrapy.Field()
    guanwang = scrapy.Field()
    dengjijiguan = scrapy.Field()
    dizhi = scrapy.Field()
    fanwei = scrapy.Field()

