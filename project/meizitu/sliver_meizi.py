# coding:utf-8
import requests
import threading
import re
import time

class Xizhi(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def gethtml(self, url):
        while 1:
            try:
                r = requests.get(url)
            except:
                print '_'
                pass
            r.encoding = 'gbk'
            html = r.text
            break
        self.posturl(html)
        self.postjpg(html)
        return 'xx'

    def posturl(self, html):
        rea = re.compile('(http://www.meizitu.com/.*?html)')
        namelist = rea.findall(html)
        namelist = list(set(namelist))
        self.put_url({"comp": str(namelist)})

    def postjpg(self, html):
        rea = re.compile('(http://pic.meizitu.com/.*?jpg)')
        namelist = rea.findall(html)
        namelist = list(set(namelist))
        self.put_jpg({"comp": str(namelist)})

    def put_url(self, mess):
        requests.post('http://' + MASTERIP + ':12666/post/url', data=mess)
        print '------------>>>'


    def put_jpg(self, mess):
        requests.post('http://' + MASTERIP + ':12666/post/jpg', data=mess)
        print '------------------------>>>'

    def get_kw():
        return requests.get('http://' + MASTERIP + ':12666/comp').text


    def run(self):
        while 1:
            try:
                # 加 try
                kw = self.get_kw()
                try:
                    print kw
                except:
                    pass
                if kw == 'xxx': time.sleep(10)
                self.gethtml(kw)



if __name__ == '__main__':
    MASTERIP = '192.168.0.50'
    for thread in range(1):
        a = Xizhi()
        a.start()
