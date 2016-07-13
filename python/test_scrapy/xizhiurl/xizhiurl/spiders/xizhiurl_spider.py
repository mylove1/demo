# coding=utf-8
from xizhi.items import XizhiItem
#from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor



class XiZhiURL_Spider(CrawlSpider):
    name = 'xizhiurl'
    allowed_domains = ['xizhi.com']
    start_urls = ['http://www.xizhi.com']

    rules = [
        Rule(SgmlLinkExtractor(allow = (u'/GS.*', )), follow=False),
        Rule(SgmlLinkExtractor(allow = (u'/[^G].*', )), follow=True),
    ]

    def parse_item(self, response):
        name = self.is_nump(response.xpath('//h2/a[@href="#"]/text()').extract())
        xizhi_url = self.is_nump(response.xpath('//td[@class="line2"][8]/text()').extract())

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

