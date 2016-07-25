# coding=utf-8
'''
查看‘失信被执行人’网信息及策略
'''
import requests
url = 'http://shixin.court.gov.cn/index_publish.jsp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Referer': 'http://wenshu.court.gov.cn/List/ListContent',
    'Connection': 'keep-alive',
}

if __name__ == "__main__":
    r = requests.get(url, headers=headers)
    text = r.text
    print text