# coding:utf-8
import MySQLdb
from flask import Flask
from flask import request
import complistadd

app = Flask(__name__)


@app.route('/')
def hello():
    global getcomp
    return '''<h1>ICP备案信息</h1><h4>已经抓取：%s</h4><h4>剩余数目：%s</h4>''' % (getcomp, 27107534-getcomp)


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
    global cursor
    items = request.form["comp"]
    # a = json.loads(a)
    try:
        items = eval(items)
        for item in items:
            cursor.execute(
                """INSERT IGNORE INTO weburl(weburl_url,weburl_name,weburl_email,weburl_starttime,weburl_endtime)
                VALUES (%s, %s, %s, %s, %s)""",
                (
                    item["url"],
                    item["name"],
                    item["email"],
                    item["starttime"],
                    item["endtime"],
                )
            )
    except MySQLdb.Error, e:
        print 'Error %d %s' % (e.args[0], e.args[1])
        cursor = link_mysql()
    # db.insert({'comp': eval(a)})
    return 'o'

def link_mysql():
    conn = MySQLdb.connect(host='192.168.100.55', user='root', passwd='dingyu', db='dingyu', port=3306,
                           charset="utf8")
    cursor = conn.cursor()
    return cursor

if __name__ == '__main__':
    getcomp = 1853853
    cursor = link_mysql()
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
    app.run(host="192.168.100.55", port=12222)
    print len(kwlist)


