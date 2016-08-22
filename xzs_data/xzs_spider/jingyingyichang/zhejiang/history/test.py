# coding:utf-8
import re
import requests
from lxml import etree

r = requests.get("http://www.zjcredit.gov.cn/sgs/sgsDetail.do?id=D24BE9D2F8A26FDEEFD081A851C8279F3FB4F0227424F2B9")
a = r.text
tree = etree.HTML(a)

# for x in  tree.xpath('//table[@class="xzcf_bg"]/tr/td[2]/text()'):
#
#     print x
#
# for y in tree.xpath('//table[@class="xzcf_bg"]/tr/td[3]/text()'):
#     print y
#
# for x in  tree.xpath('//table[@class="listf4"]//table[@class="listf2"]/text()'):
#     print x

print '-----------'

for x, y in  enumerate(tree.xpath('//table[@class="listf4"]/tr[2]/td/table/tr/td/text()')):
    print x, y
# {"id": "id", "title": li[0], "bookid": li[2], "company": li[4], "bumen": li[7], "data": li[9], "info": li[12]}
# aaa = ''.join(r.text.split())
# rea = re.compile("""<tablewidth="1000"border="0"align="center"cellpadding="0"cellspacing="0"><tr><tdstyle="padding-top:10px"align="center"class="listf2">(.*?)</td></tr></table><!----><tablewidth="100%"border="0"cellspacing="0"cellpadding="0"class="xzcf_bg"><tr><tdwidth="100"height="50"align="center"class="xzcf_tb"><imgsrc="/html/images/xzcf_wh.jpg"width="25"height="25"/></td><tdwidth="230"align="right"class="xzcf_mc">行政处罚决定书文号：</td><tdclass="xzcf_xx">(.*?)</td></tr><tr><tdheight="50"align="center"class="xzcf_tb"><imgsrc="/html/images/xzcf_rw.jpg"width="25"height="24"/></td><tdalign="right"class="xzcf_mc">被处罚单位（被处罚人）：</td><tdclass="xzcf_xx">(.*?)&nbsp;&nbsp;&nbsp;&nbsp;<spanclass="xzcf_mc">法定代表人（或单位负责人）：</span></td></tr><tr><tdheight="50"align="center"class="xzcf_tb"><imgsrc="/html/images/xzcf_bm.jpg"width="25"height="22"/></td><tdalign="right"class="xzcf_mc">执法部门：</td><tdclass="xzcf_xx">(.*?)</td></tr><tr><tdheight="50"align="center"class="xzcf_tb"><imgsrc="/html/images/xzcf_rq.jpg"width="26"height="26"/></td><tdalign="right"class="xzcf_mc">作出行政处罚的日期：</td><tdclass="xzcf_xx">(.*?)</td></tr></table><tablewidth="100%"border="0"cellspacing="0"cellpadding="0"style="margin-top:30px;"><tr><tdheight="47"width="47"bgcolor="#0a9ce9"><imgsrc="/html/images/xzcf_jds.jpg"width="47"height="47"/></td><tdwidth="270"bgcolor="#0a9ce9"align="center"style="color:white;font-size:18px;">行政处罚决定书（全文或摘要）</td><tdstyle="border-bottom:#0a9ce9solid2px;">&nbsp;</td></tr></table><tablewidth="100%"border="0"cellspacing="0"cellpadding="0"><tr><tdvalign="top"class="xzcf_jds"height="200">(.*?)</td></tr></table>""")
# print rea.findall(aaa)
