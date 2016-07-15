# coding:utf-8
import requests
from lxml import etree

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
        'Referer': 'http://gsxt.cqgs.gov.cn/',
    }
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    return r.text


if __name__ == '__main__':
    url = "http://gsxt.cqgs.gov.cn/search_searchjyyc.action?currentpage=3&itemsperpage=10"
    text = get_html(url)
    print text
    # tree = etree.HTML(text)
    # info_url = tree.xpath("//h3/a/@href")
    # print info_url
    # if info_url: info_url = info_url[0]
    # print info_url