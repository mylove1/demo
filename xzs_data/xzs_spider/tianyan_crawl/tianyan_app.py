# coding:utf-8
import json
import time
import random
from flask import Flask
from flask import request
import threading
import requests
import config

app = Flask(__name__)


@app.route('/')
def hello():
    usefulipcount = len(usefulip)
    return """<h1>代理IP</h1><h4>可用IP数量：%s</h4>""" % usefulipcount

@app.route('/ip')
def getip():
    return random.choice(usefulip)

@app.route('/ip/<int:count>')
def mutip(count):
    return '\n'.join(random.sample(usefulip, count))

# @app.route('/', methods=['POST'])
# def post_comp():
#     print request.form
#     return '3333333333333333'

if __name__ == '__main__':

    print len(ippool)
    time.sleep(5)
    print len(ippool)
    print len(usefulip)

    # 启动web
    app.run(host=config.master, port=8384)
    print 'ok'

