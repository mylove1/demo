# coding:utf-8
from flask import Flask
from flask import request

app = Flask(__name__)


# @app.route('/')
# def hello():
#     global getcomp
#     return '''<h1>悉知</h1><h4>已经抓取：%s</h4><h4>剩余数目：%s</h4>''' % (getcomp, 27107534-getcomp)
#
#
# @app.route('/comp')
# def get_comp():
#     global getcomp
#     getcomp += 1
#     db.totalcount.update({"name": "total"}, {"$inc": {"count": 1}})
#     return kwlist.pop(0)


@app.route('/postinfo', methods=['POST'])
def post_info():
    print request.form["comp"]
    count += 1
    print count
    compinfo = dict(eval(request.form["comp"]))
    print compinfo
    print type(compinfo)
    return 'o'

@app.route('/post/compurl', methods=['POST'])
def post_compurl():
    compurllist = list(eval(request.form["comp"]))
    for x in compurllist:
        print x
    return 'o'


if __name__ == '__main__':
    count = 0
    MASTERIP = '192.168.0.50'
    app.run(host=MASTERIP, port=12445)


