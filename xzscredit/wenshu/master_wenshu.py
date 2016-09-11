# coding:utf-8
import json
import time
import random
import MySQLdb
import re
import config
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
    return '''<h4>已经抓取：%s</h4><h4>剩余数目：%s</h4>''' % (getcomp, 27107534-getcomp)


@app.route('/comp')
def get_comp():
    global getcomp
    getcomp += 1
    if len(kwlist) == 0:
        return ''
        # return '没有了'
    return kwlist.pop(0)


@app.route('/post', methods=['POST'])
def post_comp():
    a = request.form["comp"]
    # a = json.loads(a)
    db.insert({'comp': eval(a)})
    return 'o'


if __name__ == '__main__':
    getcomp = 25914522

    conn = pymongo.Connection(config.master, 27017)
    db = conn.wenshu.wenshu

    kwlist = complistadd.kwlist

    # conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306, charset="utf8")
    # cur = conn.cursor()
    # a = 1
    # b = 2000000
    # cur.execute("select name from company_zong where id between %s and %s  ;" % (a, b))
    # aa = cur.fetchall()
    # for x in aa:
    #     kwlist.append(x[0])
    # conn.close()
    # starttime = time.time()
    #
    # cur.execute("select t_tian_name from t_tian;")
    # aa = cur.fetchall()
    # for x in aa:
    #     f.add(x[0])
    # print 'current company count', len(f)
    # print 'thistotal', b-a

    # with open('C:\Users\cooper\Documents\data\comp_name.fil', 'rb') as bf:
    #     f = pybloom.BloomFilter.fromfile(bf)

    # f = pybloom.BloomFilter(capacity=100000, error_rate=0.0001)
    # for comp in [u"杭州司麦数据技术有限公司",u"杭州司景峰贸易有限公司",u"杭州司捷汽车修理有限公司"]:
    #     f.add(comp)
    # kwlist = ["杭州司","杭州司","杭州","杭州 公司","杭州司目科技有限公司",]
    app.run(host=config.master, port=12315)


