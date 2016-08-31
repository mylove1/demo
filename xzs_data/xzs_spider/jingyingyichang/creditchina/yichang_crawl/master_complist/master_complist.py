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
    return '''<h1>信用中国·公司ld列表</h1><h4>已经抓取：%s</h4><h4>剩余数目：%s</h4>''' % (getcomp, 27107534-getcomp)


@app.route('/comp')
def get_comp():
    global getcomp
    getcomp += 1
    db.totalcount.update({"name": "total"}, {"$inc": {"count": 1}})
    return kwlist.pop(0)


@app.route('/post', methods=['POST'])
def post_comp():
    a = request.form["comp"]
    a = json.loads(a)
    db.complist.insert(a)
    return 'o'


if __name__ == '__main__':
    MASTERIP = '192.168.0.50'
    getcomp = complistadd.start

    conn = pymongo.Connection(MASTERIP, 27017)
    db = conn.creditchina

    # kwlist = ["平顶山市科远网络技术有限公司"]
    #
    kwlist = complistadd.kwlist


    app.run(host=MASTERIP, port=12333)


