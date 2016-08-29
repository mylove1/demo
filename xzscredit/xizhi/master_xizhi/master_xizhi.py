# coding:utf-8

import pybloom
import pymongo
from flask import Flask
from flask import request
import complistadd

app = Flask(__name__)


@app.route('/')
def hello():
    return '''<h1>悉知</h1>'''


@app.route('/comp')
def get_comp():
    if urllist:
        return urllist.pop()
    while 1:
        try:

            kw = kwlist.pop(0)
            db.totalcount.update({"name": "total"}, {"$inc": {"count": 1}})
            if kw not in f_geted_name: break
        except IndexError:
            return 'xxx'
    return kw


@app.route('/postinfo', methods=['POST'])
def post_info():
    compinfo = dict(eval(request.form["comp"]))
    db.geted.insert({"name": compinfo["name"], "url": compinfo["url"]})
    db.compinfo.insert(compinfo)
    return 'o'

@app.route('/post/compurl', methods=['POST'])
def post_compurl():
    compurllist = list(eval(request.form["comp"]))
    for x in compurllist:
        if x not in f_geted_url:
            f_geted_url.add(x)
            urllist.append(x)
    return 'o'


if __name__ == '__main__':
    MASTERIP = '192.168.0.50'
    conn = pymongo.Connection(MASTERIP, 27017)
    db = conn.xizhi

    # count = [0, 0]
    # # 0: 使用过的企业名称数目
    # count[0] = complistadd.start
    # # 1: 已经取得的企业信息数目
    # count[1] = 0

    f_geted_url = pybloom.BloomFilter(50000000, 0.0001)
    f_geted_name = pybloom.BloomFilter(50000000, 0.0001)
    for x in db.geted.find():
        f_geted_url.add(x["url"])
        f_geted_name.add(x["name"])
    print 'have read it'
    print len(f_geted_name)
    print len(f_geted_url)


    urllist = ['http://www.xizhi.com',]
    kwlist = complistadd.kwlist
    app.run(host=MASTERIP, port=12445)


