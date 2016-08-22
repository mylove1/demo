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
# import master_complistadd

app = Flask(__name__)


@app.route('/')
def hello():
    return "----xxxxxxxxxxxxxxxxxxxxxx---------------------"
#     global getcomp
#     return '''<h4>已经抓取：%s</h4><h4>剩余数目：%s</h4>''' % (getcomp, 27107534-getcomp)


# @app.route('/comp')
# def get_comp():
#     global getcomp
#     getcomp += 1
#     if len(kwlist) == 0:
#         return ''
#         # return '没有了'
#     return kwlist.pop(0)


@app.route('/post/index', methods=['POST'])
def post_comp():

    data = list(request.form)
    data = json.loads(data[0])
    for x in  data["data"]:
        print x["name"].replace("<em>", '').replace("</em>", '')



    # a = json.loads(a)
    # db.insert({'comp': eval(a)})
    return 'o'


if __name__ == '__main__':
    getcomp = 1

    # conn = pymongo.Connection(config.master, 27017)
    # db = conn.wenshu.wenshu

    # kwlist = complistadd.kwlist

    app.run(host=config.master, port=12345)


