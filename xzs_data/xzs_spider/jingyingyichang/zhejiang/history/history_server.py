# coding:utf-8
import pymongo
from flask import Flask
from flask import request
import config

app = Flask(__name__)


@app.route('/')
def hello():
    global getcomp
    return '''<h1>浙江</h1><h4>已经抓取：%s</h4>''' % getcomp


@app.route('/comp')
def get_comp():
    global getcomp
    getcomp += 1
    try:
        return kwlist.pop(0)
    except:
        print 'meiyoul'
        return '000'


@app.route('/post', methods=['POST'])
def post_comp():
    global db
    a = request.form["comp"]
    # a = json.loads(a)
    db.chufa.insert({'comp': eval(a)})
    return 'ok'


if __name__ == '__main__':
    getcomp = 0
    kwlist = []
    conn = pymongo.Connection('192.168.0.50', 27017)
    db = conn.xinyongzhejiang
    for x in db.chufaideid.find():
        kwlist.append(x["id"])

    app.run("192.168.0.50", port=12111)
    print len(kwlist)


