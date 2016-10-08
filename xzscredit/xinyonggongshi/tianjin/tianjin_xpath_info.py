#!/usr/bin/env python
# coding:utf-8
'''
天津市信用信息公示系统
企业详情页面解析
'''

import re
from bs4 import BeautifulSoup
import requests
from lxml import etree



if __name__ == '__main__':
    url = "http://tjcredit.gov.cn/platform/saic/baseInfo.json?entId=349DDA405B5E0231E04400306EF52828&departmentId=scjgw&infoClassId=dj"
    r = requests.get(url)
    a = r.text
    print a
    tree = etree.HTML(a)
    print tree.xpath('//table/tr/td/text()')