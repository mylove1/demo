# coding=utf-8
import scrapy
from xizhi.items import XizhiItem
from xizhi.namelist import namelist
from scrapy.http import Request


class Xizhi_Search_Spider(scrapy.Spider):
    name = 'xizhisearch'
    allowed_domains = ['xizhi.com']
    start_urls = namelist
    def parse(self, response):
        if response.xpath('//h2[@class="result-tit fl"]/span/text()').extract()[0] != '0':
            detail_url = response.xpath('//h3/a/@href').extract()[0]
            yield Request(url=detail_url, callback=self.detail)

    def is_nump(self, value):
        if value:
            return value[0].strip()
        else:
            return ''

    def detail(self, response):
        item = XizhiItem()
        # print response.url
        name = self.is_nump(response.xpath('//h2/a[@href="#"]/text()').extract())
        tyshxy = self.is_nump(response.xpath('//td[@width="270px"]/span/text()').extract())
        zc = self.is_nump(response.xpath('//td[@width="230px"]/span/text()').extract())
        zzjg = self.is_nump(response.xpath('//td[@class="line2"][1]/text()').extract())
        type = self.is_nump(response.xpath('//td[@class="line2"][2]/text()').extract())
        status = self.is_nump(response.xpath('//td[@class="line4"][1]/text()').extract())
        faren = self.is_nump(response.xpath('//td[@class="line2"][3]/text()').extract())
        zhuceziben = self.is_nump(response.xpath('//td[@class="line2"][4]/text()').extract())
        jingyingriqi = self.is_nump(response.xpath('//td[@class="line4"][2]/text()').extract())
        yingyeqixian = ''.join(self.is_nump(response.xpath('//td[@class="line4"][3]/text()').extract()).split())         #营业期限
        fazhaoriqi = self.is_nump(response.xpath('//td[@class="line2"][5]/text()').extract())
        guanwang = self.is_nump(response.xpath('//td[@class="line4"][4]/text()').extract())        #官网
        dengjijiguan = self.is_nump(response.xpath('//td[@class="line2"][6]/text()').extract())           #登记机关
        dizhi = self.is_nump(response.xpath('//td[@class="line2"][7]/text()').extract())            #企业地址
        fanwei = self.is_nump(response.xpath('//td[@class="line2"][8]/text()').extract())
        xizhiurl = response.url
        print xizhiurl

        item['name'] = name
        item['tyshxy'] = tyshxy
        item['zc'] = zc
        item['zzjg'] = zzjg
        item['type'] = type
        item['status'] = status
        item['faren'] = faren
        item['zhuceziben'] = zhuceziben
        item['jingyingriqi'] = jingyingriqi
        item['yingyeqixian'] = yingyeqixian
        item['fazhaoriqi'] = fazhaoriqi
        item['guanwang'] = guanwang
        item['dengjijiguan'] = dengjijiguan
        item['dizhi'] = dizhi
        item['fanwei'] = fanwei
        return item

    # def detail(self, response):
    #     item = XizhiItem()
    #     item['name'] = response.xpath('//h2/a[@href="#"]/text()').extract()
    #     item['tyshxy'] = response.xpath('//td[@width="270px"]/span/text()').extract()
    #     item['zc'] = response.xpath('//td[@width="230px"]/span/text()').extract()
    #     item['zzjg'] = response.xpath('//td[@class="line2"][1]/text()').extract()
    #     item['type'] = response.xpath('//td[@class="line2"][2]/text()').extract()
    #     item['status'] = response.xpath('//td[@class="line4"][1]/text()').extract()
    #     item['faren'] = response.xpath('//td[@class="line2"][3]/text()').extract()
    #     item['zhuceziben'] = response.xpath('//td[@class="line2"][4]/text()').extract()
    #     item['jingyingriqi'] = response.xpath('//td[@class="line4"][2]/text()').extract()
    #     item['yingyeqixian'] = response.xpath('//td[@class="line4"][3]/text()').extract()
    #     item['fazhaoriqi'] = response.xpath('//td[@class="line2"][5]/text()').extract()
    #     item['guanwang'] = response.xpath('//td[@class="line4"][4]/text()').extract()
    #     item['dengjijiguan'] = response.xpath('//td[@class="line2"][6]/text()').extract()
    #     item['dizhi'] = response.xpath('//td[@class="line2"][7]/text()').extract()
    #     item['fanwei'] = response.xpath('//td[@class="line2"][8]/text()').extract()
    #     return item


# class Xizhi_Search_Spider(scrapy.Spider):
#     name = 'xizhisearch'
#     allowed_domains = ['xizhi.com']
#     conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db=DbConfig['db'],
#                                 host=DbConfig['host'], charset='utf8', use_unicode=True)
#
#
#
#     start_urls = ['http://www.xizhi.com/search?wd=%E5%94%90%E5%B1%B1&type=all',
#
# # class Xizhi_Spider(CrawlSpider):
# #     name = 'xizhi'
# #     allowed_domains = ['xizhi.com']
# #     start_urls = ['http://www.xizhi.com/search?wd=%E5%94%90%E5%B1%B1&type=all',    # 唐山
# #                   ]
# #
# #     rules = [
# #         Rule(SgmlLinkExtractor(allow = (u'/GS.*', )), follow=True, callback = 'parse_item'),
# #         Rule(SgmlLinkExtractor(allow = (u'/[^G].*', )), follow=True),
# #         #Rule(SgmlLinkExtractor(allow = (u'/GS.*', )), follow = True, callback = 'parse_item'),
# #     ]
#
#     def is_nump(self, value):
#         if value:
#             return value[0].strip()
#         else:
#             return ''
#
#     def parse_item(self, response):
#         item = XizhiItem()
#         # print response.url
#         name = self.is_nump(response.xpath('//h2/a[@href="#"]/text()').extract())
#         tyshxy = self.is_nump(response.xpath('//td[@width="270px"]/span/text()').extract())
#         zc = self.is_nump(response.xpath('//td[@width="230px"]/span/text()').extract())
#         zzjg = self.is_nump(response.xpath('//td[@class="line2"][1]/text()').extract())
#         type = self.is_nump(response.xpath('//td[@class="line2"][2]/text()').extract())
#         status = self.is_nump(response.xpath('//td[@class="line4"][1]/text()').extract())
#         faren = self.is_nump(response.xpath('//td[@class="line2"][3]/text()').extract())
#         zhuceziben = self.is_nump(response.xpath('//td[@class="line2"][4]/text()').extract())
#         jingyingriqi = self.is_nump(response.xpath('//td[@class="line4"][2]/text()').extract())
#         yingyeqixian = ''.join(self.is_nump(response.xpath('//td[@class="line4"][3]/text()').extract()).split())         #营业期限
#         fazhaoriqi = self.is_nump(response.xpath('//td[@class="line2"][5]/text()').extract())
#         guanwang = self.is_nump(response.xpath('//td[@class="line4"][4]/text()').extract())        #官网
#         dengjijiguan = self.is_nump(response.xpath('//td[@class="line2"][6]/text()').extract())           #登记机关
#         dizhi = self.is_nump(response.xpath('//td[@class="line2"][7]/text()').extract())            #企业地址
#         fanwei = self.is_nump(response.xpath('//td[@class="line2"][8]/text()').extract())
#
#         item['name'] = name
#         item['tyshxy'] = tyshxy
#         item['zc'] = zc
#         item['zzjg'] = zzjg
#         item['type'] = type
#         item['status'] = status
#         item['faren'] = faren
#         item['zhuceziben'] = zhuceziben
#         item['jingyingriqi'] = jingyingriqi
#         item['yingyeqixian'] = yingyeqixian
#         item['fazhaoriqi'] = fazhaoriqi
#         item['guanwang'] = guanwang
#         item['dengjijiguan'] = dengjijiguan
#         item['dizhi'] = dizhi
#         item['fanwei'] = fanwei
#         return item
#         #item['name'] = response.xpath('//h2/a[@href="#"]/text()').extract()
#         #item['tyshxy'] = response.xpath('//td[@width="270px"]/span/text()').extract()
#         #item['zc'] = response.xpath('//td[@width="230px"]/span/text()').extract()
#
#
#
#
#
#         '''
#         item['name'] = self.is_nump(response.xpath('//h2/a[@href="#"]/text()').extract())
#         item['tyshxy'] = self.is_nump(response.xpath('//td[@width="270px"]/span/text()').extract())
#         item['zc'] = self.is_nump(response.xpath('//td[@width="230px"]/span/text()').extract())
#         item['zzjg'] = self.is_nump(response.xpath('//td[@class="line2"][1]/text()').extract())
#         item['type'] = self.is_nump(response.xpath('//td[@class="line2"][2]/text()').extract())
#         item['status'] = self.is_nump(response.xpath('//td[@class="line4"][1]/text()').extract())
#         item['faren'] = self.is_nump(response.xpath('//td[@class="line2"][3]/text()').extract())
#         item['zhuceziben'] = self.is_nump(response.xpath('//td[@class="line2"][4]/text()').extract())
#         item['jingyingriqi'] = self.is_nump(response.xpath('//td[@class="line4"][2]/text()').extract())
#         item['yingyeqixian'] = self.is_nump(response.xpath('//td[@class="line4"][3]/text()').extract()).replace(' ', '')         #营业期限
#         item['fazhaoriqi'] = self.is_nump(response.xpath('//td[@class="line2"][5]/text()').extract())
#         item['guanwang'] = self.is_nump(response.xpath('//td[@class="line4"][4]/text()').extract())        #官网
#         item['dengjijiguan'] = self.is_nump(response.xpath('//td[@class="line2"][6]/text()').extract())           #登记机关
#         item['dizhi'] = self.is_nump(response.xpath('//td[@class="line2"][7]/text()').extract())            #企业地址
#         item['fanwei'] = self.is_nump(response.xpath('//td[@class="line2"][8]/text()').extract()).replace('\n', '').strip()     #经营范围
#         items.append(item)
#         return items
#
# '''
#
#
#         '''
#         tyshxy = scrapy.Field()
#         zc = scrapy.Field()
#         zzjg = scrapy.Field()
#         type = scrapy.Field()
#         states = scrapy.Field()
#         faren = scrapy.Field()
#         zhuceziben = scrapy.Field()
#         jingyingriqi = scrapy.Field()
#         yingyeqixian = scrapy.Field()
#         fazhaoriqi = scrapy.Field()
#         guanwang = scrapy.Field()
#         dengjijiguan = scrapy.Field()
#         dizhi = scrapy.Field()
#         fanwei = scrapy.Field()
#
#
#
#         #print "stop.."
# '''