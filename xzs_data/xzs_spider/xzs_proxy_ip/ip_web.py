# coding:utf-8
import time
import random
from flask import Flask
import ip_check

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

def ip_web():
    print "正在初始化..."
    ippool = ip_check.ippool
    global usefulip
    usefulip = ip_check.usefulip
    print len(ippool)
    time.sleep(5)
    print len(ippool)
    print len(usefulip)
    app.run(host=config.LISTENING_IP, port=config.LISTENING_PORT)


