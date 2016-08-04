# coding:utf-8
import time
import random
import requests
import threading
import config


class SearchBox(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def get_kw(self):
        r = requests.get('http://192.168.0.100:11111/comp')
        return r.text

    def get_html(self, kw):
        while 1:
            this_headers = {
                'User-Agent': random.choice(config.agents),
                'Referer': 'http://www.tianyancha.com',
                'Connection': 'keep-alive',
            }
            url = ['http://www.tianyancha.com/suggest/', kw, '.json']
            try:
                proxy = requests.get('http://192.168.0.100:8384/ip').text
                r = requests.get(''.join(url), headers=this_headers, proxies={'http': proxy}, timeout=5)
                html = r.text
                if html[0:5] != '{"sta':
                    continue
                break
            except:
                pass
        r.encoding = 'utf8'
        return r.text

    def put_mess(self, mess):
        requests.post('http://192.168.0.100:11111/post', data=mess)

    def run(self):
        while 1:
            kw = self.get_kw()
            print kw
            if len(kw) >=10:
                kw = kw[:-5]
            if kw == '':
                print 'Done'
                break
            html = self.get_html(kw)
            print html
            print '------------------', kw
            self.put_mess({'comp': html})


def main():
    for x in xrange(1):
        thread = SearchBox()
        thread.start()

if __name__ == '__main__':
    main()
