# coding:utf-8
from lxml import etree
import requests


r = requests.get('http://www.xizhi.com/search?wd=%E6%9D%AD%E5%B7%9E%E9%93%B6%E8%A1%8C&type=all')
r.encoding = 'gbk'
a = r.text
tree = etree.HTML(a)
# print a
print tree.xpath('//a[@href="http://company.xizhi.com/GS5706c93c1f98cc40348b47dc/"]')


# tree.xpath("//h3/a/@href")














# [kuaidaili]'http://www.kuaidaili.com/free/inha/24/'
# ip = tree.xpath("//td[@data-title='IP']/text()")
# port = tree.xpath("//td[@data-title='PORT']/text()")
# for x in range(15):
#     print ip[x] + ':' + port[x]

# [zhihu] 登陆之后的页面
# name = tree.xpath("//span[@class='name']/text()")[0]
# ques = tree.xpath("//h2/a/text()")
# list_num = len(ques)
# print(name)
# for x in range(1, list_num):
#     print x, '   ', ques[x].strip()
#
# # print(u"美国经历过" in a)