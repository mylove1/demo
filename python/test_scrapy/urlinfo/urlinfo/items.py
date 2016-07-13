# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UrlinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    comp_Name = scrapy.Field()
    comp_No = scrapy.Field()
    comp_OperName = scrapy.Field()
    comp_Type = scrapy.Field()
    comp_RegistCapi = scrapy.Field()
    comp_Address = scrapy.Field()
    comp_StartDate = scrapy.Field()
    comp_TermStart = scrapy.Field()
    comp_TermEnd = scrapy.Field()
    comp_EndDate = scrapy.Field()
    comp_Scope = scrapy.Field()
    comp_BelongOrg = scrapy.Field()
    comp_CheckDate = scrapy.Field()
    comp_Status = scrapy.Field()

    pass
