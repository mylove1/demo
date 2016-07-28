# # coding=utf-8
# import requests
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
#     'Referer': 'http://wenshu.court.gov.cn/List/ListContent',
#     'Connection': 'keep-alive',
# }
#
# data = {
#     'Param': '上传日期:2016-07-22,案件类型:刑事案件',
#     'Index': '1',
#     'Page': '5',
#     'Order': '法院层级',
#     'Direction': 'asc',
# }
# '''
# Param	全文检索:华为技术有限公司
# Index	1
# Page	5
# Order	法院层级
# Direction	asc
# '''
# '''
# Param	全文检索:华为技术有限公司
# Index	2
# Page	5
# Order	法院层级
# Direction	asc
# '''
#
# url = 'http://wenshu.court.gov.cn/List/ListContent'
# # '?Param=上传日期:2016-07-22,案件类型:刑事案件&Index=1&Page=5&Order=法院层级&Direction=asc'
#
# r = requests.get(url)
# print r.text
#
#
# '''



class search_company_wenshu:
    def __init__(self):
        self.url = ''
        self.data = {}

    def get(self):
        print hello

hello = 'hello'
a = search_company_wenshu()
a.get()



# '''




# a = [0,1,2,3,4,5]
# for num,x in enumerate(a):
#     if x == 3:
#         a[num] = 'x'
#     print x
# print a

# import requests
# url = 'http://gsxt.zjaic.gov.cn/appbasicinfo/doReadAppBasicInfo.do?corpid=F58C60CE41314E1812AA3829B3EE31DEB4C88C7A60FE75B8FB3B1A0C5B84F133'
# headers = {
#     'Referer': 'http://gsxt.zjaic.gov.cn/appbasicinfo/doViewAppBasicInfo.do;jsessionid=8FD4E3E4AFB9FAEAA5FC64E182EBF96D.gsxt46?corpid=F58C60CE41314E1812AA3829B3EE31DEB4C88C7A60FE75B8FB3B1A0C5B84F133&no=7'
# }
# r = requests.get(url, headers=headers)
# print r.text








