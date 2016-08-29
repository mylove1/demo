# coding:utf-8
'''
data中的session不可省略
headers中的cookie不可省略这就基本上没办法了
8.29日早上试过一次，等上午了再试一次
'''


import requests

def fujian_search_post(kw):
    url = 'http://wsgs.fjaic.gov.cn/creditpub/search/ent_info_list'
    data = {
        'captcha': '-2',
        'condition.pageNo': '1',
        'condition.insType': '',
        'session.token': 'db167222-948c-4dcb-b4cc-1235c561de0c',
        'condition.keyword': kw,
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '154',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'Hm_lvt_f7c37bed0f803872ca930a355260a54b=1467625318; _gscu_2074118766=676253186cfklh19; JSESSIONID=0000DYN_Sh65HlgW8VqczO_YLLV: 18klqqne7; fjgs=20111142',
        'Host': 'wsgs.fjaic.gov.cn',# 可以省略
        'Origin': 'http://wsgs.fjaic.gov.cn',# 可以省略
        'Referer': 'http://wsgs.fjaic.gov.cn/creditpub/search/ent_info_list',# 可以省略
        'Upgrade-Insecure-Requests': '1',# 可以省略
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',# 可以省略
    }
    html = requests.post(url, data, headers=headers)
    print html.text




if __name__ == '__main__':
    fujian_search_post("中国石化")