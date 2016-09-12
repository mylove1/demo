# coding:utf-8
import requests
import threading
import re
import time

class YouBoy(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.relist = [
        ["name", re.compile("<SPAN>(.*?)</SPAN>")],
        ["tel", re.compile(u'<LIclass="gslxl">联系电话：</LI><LIclass="gslxr">(.*?)</LI>')],
        ["chuanzhen", re.compile(u'<LIclass="gslxl">公司传真：</LI><LIclass="gslxr">(.*?)</LI>')],
        ["phone", re.compile(u'<LIclass="gslxl">手机：</LI><LIclass="gslxr">(.*?)</LI>')],
        ["person", re.compile(u'<LIclass="gslxl">联系人：</LI><LIclass="gslxr">(.*?)</LI>')],
        ]

    def gethtml(self, url):
        while 1:
            try:
                r = requests.get(url)
            except:
                print '_'
                pass
            html = r.text
            break
        self.posturl(html)
        if "/qiye" in url:
            self.postjpg(html)
        return 'ok'

    def posturl(self, html):
        rea = re.compile('href="(/.*?html)"')
        namelist = rea.findall(html)
        namelist = list(set(namelist))
        for x in range(len(namelist)):
            namelist[x] = 'http://qiye.youboy.com' + namelist[x]
        self.put_url({"comp": str(namelist)})

    def postjpg(self, html):
        info = {}
        html = ''.join(html.split())
        html = html.replace("&nbsp;", "")

        for x in self.relist:
            try:
                info[x[0]] = x[1].findall(html)[0]
            except:
                info[x[0]] = ''
        # for x in info.keys():
        #     print info[x]
        # rea = re.compile('(http://pic.meizitu.com/.*?jpg)')
        # namelist = rea.findall(html)
        # namelist = list(set(namelist))
        if info["name"] != '':
            self.put_jpg({"comp": str(info)})

    def put_url(self, mess):
        requests.post('http://' + MASTERIP + ':31111/post/url', data=mess)
        print '------------>>>'


    def put_jpg(self, mess):
        requests.post('http://' + MASTERIP + ':31111/post/jpg', data=mess)
        print '------------------------>>>'

    def get_kw(self):
        return requests.get('http://' + MASTERIP + ':31111/comp').text


    def run(self):
        while 1:
            try:
                # 加 try
                kw = self.get_kw()
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



if __name__ == '__main__':
    MASTERIP = '192.168.0.50'
    for thread in range(1):
        a = YouBoy()
        a.start()
