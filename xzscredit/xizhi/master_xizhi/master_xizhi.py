# coding:utf-8
import json
import time
import random
import MySQLdb
import re
import pybloom
import pymongo
from flask import Flask
from flask import request
import threading
import complistadd

app = Flask(__name__)


@app.route('/')
def hello():
    global getcomp
    return '''<h1>悉知</h1><h4>已经抓取：%s</h4><h4>剩余数目：%s</h4>''' % (getcomp, 27107534-getcomp)


@app.route('/comp')
def get_comp():
    if urllist:
        return urllist.pop()

    while 1:
        try:
            db.totalcount.update({"name": "total"}, {"$inc": {"count": 1}})
            kw = kwlist.pop(0)
            if kw not in f_geted_name: break
        except IndexError:
            return 'xxx'
    return kw


@app.route('/post', methods=['POST'])
def post_comp():
    a = dict(eval(request.form["comp"]))
    db.geted.insert({"name": a["name"], "url": a["url"]})
    db.xizhi.insert(a)
    a = json.loads(a)
    db.complist.insert(a)
    return 'o'

@app.route('/post/compurl', methods=['POST'])
def post_compurl():
    compurllist = list(eval(request.form["comp"]))
    for x in compurllist:
        if x not in f_geted_url:
            f_geted_url.add(x)
            urllist.append(x)
        print x
    return 'o'


if __name__ == '__main__':
    MASTERIP = '192.168.0.50'
    conn = pymongo.Connection(MASTERIP, 27017)
    db = conn.xizhi

    f_geted_url = pybloom.BloomFilter(50000000, 0.0001)
    f_geted_name = pybloom.BloomFilter(50000000, 0.0001)
    for x in db.geted:
        f_geted_url.add(x["url"])
        f_geted_name.add(x["name"])


    getcomp = complistadd.start
    urllist = []
    kwlist = complistadd.kwlist


    app.run(host=MASTERIP, port=12333)


