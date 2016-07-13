# coding=utf-8
from xizhi.items import XizhiItem
#from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor


class Xizhi_Spider(CrawlSpider):
    name = 'xizhi'
    allowed_domains = ['xizhi.com']
    start_urls = ['http://www.xizhi.com/search?wd=%E5%94%90%E5%B1%B1&type=all',    # 唐山
                  ]

    rules = [
        Rule(SgmlLinkExtractor(allow = (u'/GS.*', )), follow=True, callback = 'parse_item'),
        Rule(SgmlLinkExtractor(allow = (u'/[^G].*', )), follow=True),
        #Rule(SgmlLinkExtractor(allow = (u'/GS.*', )), follow = True, callback = 'parse_item'),
    ]

    def is_nump(self, value):
        if value:
            return value[0].strip()
        else:
            return ''

    def parse_item(self, response):
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

        #item['name'] = response.xpath('//h2/a[@href="#"]/text()').extract()
        #item['tyshxy'] = response.xpath('//td[@width="270px"]/span/text()').extract()
        #item['zc'] = response.xpath('//td[@width="230px"]/span/text()').extract()
        return item




        '''
        item['name'] = self.is_nump(response.xpath('//h2/a[@href="#"]/text()').extract())
        item['tyshxy'] = self.is_nump(response.xpath('//td[@width="270px"]/span/text()').extract())
        item['zc'] = self.is_nump(response.xpath('//td[@width="230px"]/span/text()').extract())
        item['zzjg'] = self.is_nump(response.xpath('//td[@class="line2"][1]/text()').extract())
        item['type'] = self.is_nump(response.xpath('//td[@class="line2"][2]/text()').extract())
        item['status'] = self.is_nump(response.xpath('//td[@class="line4"][1]/text()').extract())
        item['faren'] = self.is_nump(response.xpath('//td[@class="line2"][3]/text()').extract())
        item['zhuceziben'] = self.is_nump(response.xpath('//td[@class="line2"][4]/text()').extract())
        item['jingyingriqi'] = self.is_nump(response.xpath('//td[@class="line4"][2]/text()').extract())
        item['yingyeqixian'] = self.is_nump(response.xpath('//td[@class="line4"][3]/text()').extract()).replace(' ', '')         #营业期限
        item['fazhaoriqi'] = self.is_nump(response.xpath('//td[@class="line2"][5]/text()').extract())
        item['guanwang'] = self.is_nump(response.xpath('//td[@class="line4"][4]/text()').extract())        #官网
        item['dengjijiguan'] = self.is_nump(response.xpath('//td[@class="line2"][6]/text()').extract())           #登记机关
        item['dizhi'] = self.is_nump(response.xpath('//td[@class="line2"][7]/text()').extract())            #企业地址
        item['fanwei'] = self.is_nump(response.xpath('//td[@class="line2"][8]/text()').extract()).replace('\n', '').strip()     #经营范围
        items.append(item)
        return items

'''


        '''
        tyshxy = scrapy.Field()
        zc = scrapy.Field()
        zzjg = scrapy.Field()
        type = scrapy.Field()
        states = scrapy.Field()
        faren = scrapy.Field()
        zhuceziben = scrapy.Field()
        jingyingriqi = scrapy.Field()
        yingyeqixian = scrapy.Field()
        fazhaoriqi = scrapy.Field()
        guanwang = scrapy.Field()
        dengjijiguan = scrapy.Field()
        dizhi = scrapy.Field()
        fanwei = scrapy.Field()



        #print "stop.."
'''