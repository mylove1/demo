# coding:utf-8
import json
import time
import random
import MySQLdb
import pymongo
import re
import pybloom
from flask import Flask
from flask import request
import complistadd

app = Flask(__name__)


@app.route('/')
def hello():
    global getcomp, newcomp
    return '''<h1>天眼查·公司ld列表</h1><h4>已经抓取：%s</h4><h4>剩余数目：%s</h4><h4>新公司%s个''' % (getcomp, 27107534-getcomp, newcomp)


@app.route('/comp')
def get_comp():
    global getcomp
    getcomp += 1
    db.totalcount.update({"name": "total"}, {"$inc": {"count": 1}})
    try:
        kw = kwlist.pop(0)
        return kw
    except:
        return ''


@app.route('/post', methods=['POST'])
def post_comp():
    global db, f, newcomp
    a = request.form["comp"]
    rea = re.compile('name":"(.*?)",')
    for x in rea.findall(a):
        if not (x in f):
            try:
                db.newcomp.insert({"name": x})
                newcomp += 1
                f.add(x)
            except MySQLdb.Error, e:
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return 'o'

if __name__ == '__main__':
    newcomp = 0
    MASTERIP = '192.168.0.50'
    getcomp = complistadd.start

    conn = pymongo.Connection(MASTERIP, 27017)
    db = conn.tianyan
    kwlist = complistadd.kwlist

    # f = pybloom.BloomFilter(capacity=1000000, error_rate=0.0001)
    # conn = MySQLdb.connect(host='192.168.0.100', user='root', passwd='dingyu', db='dingyu', port=3306, charset="utf8")
    # cur = conn.cursor()
    # a = 20001
    # b = 2000000
    # cur.execute("select name from company_zong where id between %s and %s  ;" % (a, b))
    # aa = cur.fetchall()
    # for x in aa:
    #     kwlist.append(x[0])
    # starttime = time.time()
    #
    # cur.execute("select t_tian_name from t_tian;")
    # aa = cur.fetchall()
    # for x in aa:
    #     f.add(x[0])
    # print 'current company count', len(f)
    # print 'thistotal', b-a

    with open('C:\Users\cooper\Documents\data\comp_name.fil', 'rb') as bf:
        f = pybloom.BloomFilter.fromfile(bf)

    # f = pybloom.BloomFilter(capacity=100000, error_rate=0.0001)
    # for comp in [u"杭州司麦数据技术有限公司",u"杭州司景峰贸易有限公司",u"杭州司捷汽车修理有限公司"]:
    #     f.add(comp)
    # kwlist = ["杭州司","杭州司","杭州","杭州 公司","杭州司目科技有限公司",]
    app.run(host="192.168.0.50", port=11111)


