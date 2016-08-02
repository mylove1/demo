# coding:utf-8
import os
import time
import requests
import threading
import pymongo
import pybloom
import proxyweblink



def checkfile(filename, sleeptime=10):
    checknum = os.path.getmtime(filename)
    while 1:
        currentnum = os.path.getmtime(filename)
        if checknum != currentnum:
            checknum = currentnum
            reload(proxyweblink)
        time.sleep(sleeptime)

proxyweb = {
    'kuaidaili': {
        'linklist': ['http://www.kuaidaili.com/proxylist/' + str(x) for x in xrange(10)],
        'sleeptime': 600,
        're': '<tddata-title="IP">(.*?)</td><td data-title="PORT">(.*?)</td>',
        },
    '2': {
        'linklist': ['http://www.kuaidaili.com/proxylist/' + str(x) for x in xrange(10)],
        'sleeptime': 600,
        're': '<tddata-title="IP">(.*?)</td><td data-title="PORT">(.*?)</td>',
    },
}


class crawlip(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def get_html(self, url):
        this_headers = {
            'User-Agent': random.choice(headers),
            'Referer': url,
            'Connection': 'keep-alive',
        }
        r = requests.get()
def main():
    f = pybloom.BloomFilter(capacity=10000000, error_rate=0.001)
    mong = pymongo.Connection(host='192.168.0.100', port=27017)
    db = mong.ip




    a = threading.Thread(target=checkfile, args=('proxyweblink.py', 3))
    a.start()
    with open('C:\Users\cooper\Documents\data\proxy_ip.fil', 'wb') as abf:
        f.tofile(abf)

if __name__ == '__main__':
    main()


# def proxy():
#     global proxy_pool
#     rule = [
#         ['http://www.youdaili.net/Daili/guonei/4766.html', r'<br/>((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))):(.*?)'],
#         # ['http://www.xicidaili.com/wn/22', r'<td>((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))</td><td>(.*?)</td>'],
#     ]
#
#     for rangeweb in rule:
#         thisrule = re.compile(rangeweb[1])
#         r = requests.get(rangeweb[0], headers={
#             'content-type': 'application/json',
#             'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )',
#             })
#         text = r.text
#         text = ''.join(text.split())
#         proxy_yuan = thisrule.findall(text)
#         for every_ip in proxy_yuan:
#             proxy_pool[every_ip[0] + ':' + every_ip[1]] = ''

