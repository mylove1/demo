# coding:utf-8

import pybloom
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/comp')
def get_comp():
    global clo
    if urllist:
        return urllist.pop()
    while 1:
        try:
            kw = kwlist.pop(0)

            break
        except IndexError:
            if clo > 1000:
                f.close()
            clo += 1
            print 'file closed'
            return 'xxx'
    return kw


@app.route('/post/jpg', methods=['POST'])
def post_info():
    global total_jpg
    compurllist = list(eval(request.form["comp"]))
    

    for x in compurllist:
        if x not in f_url:
            f_url.add(x)
            f.write(x + '\n')
            total_jpg += 1
    print '---------------------------------------jpg',total_jpg
    return 'o'

@app.route('/post/url', methods=['POST'])
def post_compurl():
    global total_page
    compurllist = list(eval(request.form["comp"]))


    for x in compurllist:
        if x not in f_url:
            f_url.add(x)
            total_page += 1
            urllist.append(x)
    print '--------------------------page',total_page
    print '------------------------------------------------------------',len(urllist)

    return 'o'


if __name__ == '__main__':
    MASTERIP = '192.168.0.50'
    kwlist = ['http://www.meizitu.com/']
    total_page = 0
    total_jpg = 0
    clo = 0


    f_url = pybloom.BloomFilter(50000000, 0.0001)
    f = open('meizitu.txt', 'w')
    urllist = []
    app.run(host=MASTERIP, port=12666)


