# -*- coding:utf-8 -*-
import scrapy
import MySQLdb
import re
from urlinfo.settings import DbConfig
from urlinfo.items import UrlinfoItem


class UrlinfoSpider(scrapy.Spider):
    name = "urlinfo"
    # 读数据库生成url列表
    """
    try:
        conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'],
                               db=DbConfig['db'], host=DbConfig['host'], charset='utf8', use_unicode=True)
        cur = conn.cursor()
        cur.execute("select link from hnqyxyurl;")
        conn.close()
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    """
    # "http://222.143.24.157/businessPublicity.jspx?id="+ x + "&sourceT
    start_urls = [
        "http://222.143.24.157/businessPublicity.jspx?id=35ED94CD71B4A102E053050A080A5B20&sourceType=1"
    ]

    def parse(self, response):
        print "start"
        # print  response.xpath('//div[@id="jibenxinxi"]/table').extract()
        html = ''.join(response.xpath('//div[@id="jibenxinxi"]/table').extract())
        print html

        #re_name = re.compile("")
        #re_no = re.compile("")
        #re_openname = re.compile("")
        #re_type = re.compile("")
        #re_registcapi = re.compile("")
        #re_address = re.compile("")
        #re_startdate = re.compile("")
        #re_termstart = re.compile("")
        #re_termend = re.compile("")
        #re_enddate = re.compile("")
        #re_scope = re.compile("")
        #re_belongorg = re.compile("")
        #re_checkdate = re.compile("")
        #re_status = re.compile("")


        print "ok"
        # "# item = UrlinfoItem()
        # item["comp_Name"] = response.xpath('//div[@id="jibenxinxi"]/table[1]/tr[2]/td[2]/text()').extract()[0]
        # item["comp_No"] = response.xpath('//div[@id="jibenxinxi"]/table[1]/tr[2]/td[1]/text()').extract()[0].strip()
        # item["comp_OperName"] = response.xpath('//div[@id="jibenxinxi"]/table[1]/tr[3]/td[2]/text()').extract()[0]
        # item["comp_Type"] = response.xpath('//div[@id="jibenxinxi"]/table[1]/tr[3]/td[1]/text()').extract()[0]
        # item["comp_RegistCapi"] =
        # item["comp_Address"] =
        # item["comp_StartDate"] =
        # item["comp_TermStart"] =
        # item["comp_TermEnd"] =
        # item["comp_EndDate"] =
        # item["comp_Scope"] =
        # item["comp_BelongOrg"] =
        # item["comp_CheckDate"] =
        # item["comp_Status"] =









'''
    def parse(self, response):
        print "start"
        print response.url

        a = response.xpath('//div[@id="jibenxinxi"]/table[1]/tr/th/text()').extract()
        b = response.xpath('//div[@id="jibenxinxi"]/table[1]/tr/td/text()').extract()
        print len(a)
        print len(b)
        if len(a) != len(b):
            for x in range(len(a)):
                print a[x],b[x]

        print "ok"
'''