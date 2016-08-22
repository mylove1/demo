# # coding:utf-8
# import requests
import re
# url = "http://www.zjcredit.gov.cn/page/sgs/sgsProxy.jsp?startrecord=1155530&endrecord=1156200&perpage=8&totalRecord=1155093"
# r = requests.post(url, data={"id2": ''})
# print r.text
#
# rea = re.compile('id=(.*?)"')
# for x, y in enumerate(rea.findall(r.text)):
#     print x, y

# page = 3
#
# urllist = ["http://www.zjcredit.gov.cn/page/sgs/sgsProxy.jsp?startrecord=", str(1 + (1000 * (page - 1))), "&endrecord=",
#            str(page * 1000), "&perpage=8&totalRecord=1155093"]
# print ''.join(urllist)

rea = re.compile('id=(.*?)"')
if not rea.findall('sdfsdfsdfsdf'): print 'ok'