# coding:utf-8
import requests
import re
import json
from lxml import etree


def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Host": "www.11467.com",
        "Referer": "http://www.11467.com/nanyang/co/65854.html",
        "Accept-Languange": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Content-type": "text/html; charset=utf-8"
            }
    r = requests.get(url, headers=headers)
    html = r.text
    return html


def get_city_url(url):
    url = url
    html = get_html(url)
    tree = etree.HTML(html)
    urllist = []
    for x in tree.xpath('//a/@href'):
        if ("http://www.11467.com/" in x) & (x[-1] == "/") & (x[-5:] != ".com/") & (x[-6:] != "temap/"):
            urllist.append(x)
    return urllist


def get_sheng_name(url):
    print url
    html = get_html(url)
    tree = etree.HTML(html)
    a = tree.xpath('//strong[2]/text()')[0]
    return a


def file_list(file):
    l = []
    with open(file, 'r') as f:
        for x in f.readlines():
            x = x.strip()
            l.append(x)
    return l


def get_city_count(url):
    html = get_html(url)
    tree = etree.HTML(html)
    # a = re.match(r'<span>', html)
    a = tree.xpath('//div[@id="nav"]/span/text()')[0]
    print len(a)
    return a


if __name__ == '__main__':
    # l = file_list('city_url.txt')
    # for x in l:
    #     print '"' + x + '",'
    with open('city_count.json', 'r') as f:
        j = json.loads(''.join(f.readlines()))
    ttt = 0
    for x in range(0,len(j)):
        if j[x]["sheng"] == u"浙江":
            print j[x]["shi"],j[x]["count"]
            ttt += int(j[x]["count"])
    print ttt

    # for x in range(0, len(j)):
    #     print j[x]["sheng"] + ' ' + j[x]["shi"] + ' ' + j[x]["count"] + ' ' + j[x]["url"]


    # ttt = 0
    # for x in range(0, len(j)):
    #     ttt += int(j[x]["count"])
    # print ttt





























    # url = 'http://www.11467.com/'
    # total_url = []
    # for x in get_city_url(url):
    #     for y in get_city_url(x):
    #         total_url.append(y)
    #         print '"' + y + '",'
    # ids = list(set(total_url))
    # print '-----------------------------------------------'
    # total_url = []
    # for x in ids:
    #     print len(total_url)
    #     for y in get_city_url(x):
    #         total_url.append(y)
    # ids = list(set(total_url))
    # with open('city_url.txt','w') as f:
    #         for x in ids:
    #             f.write(x)
    #             f.write('\n')
    # print len(ids)
    # print 'ok'


