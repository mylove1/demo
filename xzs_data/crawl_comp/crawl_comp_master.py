# coding:utf-8

import pybloom
from flask import Flask
from flask import request
import config
import pymongo

app = Flask(__name__)



@app.route('/')
def hello():
    global total_url, total_comp
    html_page = """<h1>youboy</h1><h4>总链接数：%s</h4><h4>总结果数：%s</h4>"""%(total_url, total_comp)
    return html_page

@app.route('/comp')
def get_comp():
    if urllist:
        return urllist.pop()
    else:
        return '0'


@app.route('/post/jpg', methods=['POST'])
def post_info():
    global total_comp
    compinfo = dict(eval(request.form["comp"]))
    db.comp_huanqiumaoyi.insert(compinfo)
    total_comp += 1

    return 'o'

@app.route('/post/url', methods=['POST'])
def post_compurl():
    global total_url
    compurllist = list(eval(request.form["comp"]))


    for x in compurllist:
        if ">" in x:
            continue
        if x not in f_comp:
            f_comp.add(x)
            total_url += 1
            urllist.append(x)

    return 'ok'


if __name__ == '__main__':
    MASTERIP = config.MASTERIP
    LISTENPORT = config.LISTENPORT
    urllist = config.kwlist

    conn = pymongo.Connection(MASTERIP, 27017)
    db = conn.youboy

    total_url = 0
    total_comp = 0

    f_comp = pybloom.BloomFilter(50000000, 0.0001)
    app.run(host=MASTERIP, port=LISTENPORT)


