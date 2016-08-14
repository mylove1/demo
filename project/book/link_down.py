# coding:utf-8
import requests
import re
import time
import threading


def get_html(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Referer': 'http://ctext.org/',
    'Connection': 'keep-alive',
    }
    r = requests.get(url, headers=headers)
    return r


def link_down(url):
    with open('F:/pdf/houhanshu/' + url[32:38] + '.pdf', 'wb') as f:
        r = get_html(url)
        f.write(r.content)
    print '       ', x, '\tis download'




if __name__ == '__main__':
    for x in xrange(64151, 64152):
        link = ''.join(['http://download.ctext.org/zh/060', str(x), '.cn.pdf'])
        link_down(link)



