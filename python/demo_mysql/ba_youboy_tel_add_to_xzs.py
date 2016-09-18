# coding:utf-8
import MySQLdb
import pymongo
conn_mongo = pymongo.Connection('192.168.0.50', 27017)
db = conn_mongo.youboy

conn = MySQLdb.connect(host='192.168.0.50', user='root', passwd='dingyu', db='xzs', port=3306,  charset="utf8")
cur = conn.cursor()
for enu, compinfo in enumerate(db.comp.find()):
    dianhua = compinfo["tel"]
    if not dianhua:
        continue
    # print dianhua
    compname = compinfo["name"]
    print compname
    print dianhua

    # 判断名称中是否有特殊字符
    if "'" in compname or "\\" in compname:
        continue
    #
    # # 查询公司ID
    # cur.execute('select t_gongsi_id from t_gongsi where t_gongsi_mingzi = "%s";' % compname)
    # t_gongsi_id =  cur.fetchone()
    #
    #
    #
    # sql = 'update t_gongsi set t_gongsi_dianhua="%s" where t_gongsi_mingzi = "%s";'% (dianhua, compname)

    #
    if enu%10000 == 0:
        print enu

    if enu >=100:
        break