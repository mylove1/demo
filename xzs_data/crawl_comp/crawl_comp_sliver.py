# coding:utf-8
import requests
import threading
import re
import time
import config
import urlparse

class YouBoy(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.relist = config.relist
        self.use_proxy = config.use_proxy

    def gethtml(self, url):

        while 1:
            try:
                if self.use_proxy:
                    try:
                        proxy = proxypool.pop(0)
                    except:
                        proxypool.extend(requests.get("http://192.168.0.50:8384/ip/100").text.split())
                        continue
                    r = requests.post(url, proxies={'http': proxy}, timeout=7)
                else:
                    r = requests.get(url )
            except:
                print '_'
                pass
            r.encoding = config.bianma
            html = r.text
            break
        self.posturl(url, html)
        # self.postjpg(html)
        for enu,x in enumerate(config.xiangqing):
            if x in url:
                self.postjpg(html, enu)
        return 'ok'

    def get_url(self, host, html):
        rea = re.compile('href="(.*?)"')
        namelist = rea.findall(html)
        namelist = list(set(namelist))
        new_namelist = []
        for x in namelist:
            if x[:3] == 'htt' and (x[-1] == '/' or x[-1] == 'html'):
                new_namelist.append(x)
            elif x[:1] == '/' and (x[-1] == '/' or x[-1] == 'html'):
                new_namelist.append(urlparse.urljoin(host, x))
            else:
                pass
        return list(set(new_namelist))

    def fenbian_url(self, url_list):
        new_list = []
        l = config.wuyong
        for url in url_list:
            for x in l:
                if x not in url:
                    new_list.append(url)
        return new_list


    def posturl(self, url, html):
        namelist = self.get_url(url, html)
        new_namelist = self.fenbian_url(namelist)
        # print '\n'.join(new_namelist)
        self.put_url({"comp": str(new_namelist)})


    def postjpg(self, html, n):
        info = {}
        html = config.t_html(html)

        for x in self.relist[n]:
            try:
                info[x[0]] = x[1].findall(html)[0]
            except:
                info[x[0]] = ''
        # for x in info.keys():
            # print x, info[x]
        # rea = re.compile('(http://pic.meizitu.com/.*?jpg)')
        # namelist = rea.findall(html)
        # namelist = list(set(namelist))
        if info["name"] != '':
            self.put_jpg({"comp": str(info)})

    def put_url(self, mess):
        requests.post('http://' + MASTERIP + ':' + str(config.LISTENPORT) + '/post/url', data=mess)
        print '------------>>>'


    def put_jpg(self, mess):
        requests.post('http://' + MASTERIP + ':' + str(config.LISTENPORT) + '/post/jpg', data=mess)
        print '------------------------>>>'

    def get_kw(self):
        return requests.get('http://' + MASTERIP + ':' + str(config.LISTENPORT) + '/comp').text


    def run(self):
        while 1:
            try:
                # 加 try
                kw = self.get_kw()
                # kw = "http://www.herostart.com/gongsi/sq98832.html"

                if kw == '0':
                    print 'no kw'
                    time.sleep(5)
                    continue
                try:
                    print kw
                except:
                    pass

                self.gethtml(kw)

            except:
                pass
            # break



if __name__ == '__main__':
    proxypool = []
    MASTERIP = config.MASTERIP
    for thread in range(5):
        a = YouBoy()
        a.start()
