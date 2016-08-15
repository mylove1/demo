# coding:utf-8
import requests
import re
import time
import threading


def get_html(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Referer': 'http://www.rain8.com/',
    'Connection': 'keep-alive',
    }
    r = requests.get(url, headers=headers)
    return r

class download(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.threadlist = threadlist

    def run(self):
        while 1:
            try:
                x, name, url = self.threadlist.pop(0)
                with open('F:/book/' + name + '.rar', 'wb') as f:
                    r = get_html(url)
                    f.write(r.content)
                print '       ', x, '\tis download'
            except:
                print 'sleep'
                time.sleep(3)


class geturl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.threadlist = threadlist

    def run(self):
        for x in xrange(23440, 23750):
            print 'try', x

            url = ['http://txt.rain8.com/plus/xiazai_yfx.php?open=0&aid=', str(x), '&cid=3']
            url = ''.join(url)
            r = get_html(url)
            try:
                name = re.findall('<h2>.*?<a.*?>(.*?)</a>', r.text)[0]
                url = re.findall('href="(http.*?hash=.*?)"', r.text)[0]
            except:
                continue
            self.threadlist.append([x, name, url])
            print x, '\tadd it'
if __name__ == '__main__':
    threadlist = []
    a = geturl()
    a.start()
    for thread in range(10):
        b = download()
        b.start()

