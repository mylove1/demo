# coding:utf-8
import MySQLdb
import pymongo
import sys
reload(sys)
try:
    sys.setdefaultencoding("utf-8")
except:
    reload(sys)
    sys.setdefaultencoding("utf-8")

DbConfig = {
    "user": "root",
    "passwd": "dingyu",
    "host": "192.168.0.50",
}



conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db="xzs",
                       host=DbConfig['host'], charset='utf8', use_unicode=True)
cursor = conn.cursor()

conn_mongo = pymongo.Connection(host='192.168.0.50', port=27017)
db = conn_mongo.wenshu

for enu,everyone in enumerate(db.wenshu.find()):
    if enu % 1000 == 0:
        print enu
        # break
    try:
        # print everyone["comp"].keys()
        # print everyone

        getidsql = "select t_gongsi_id from t_gongsi where t_gongsi_mingzi='%s';" % everyone["comp"]["company"]
        cursor.execute(getidsql)
        company_id = cursor.fetchone()[0]
        # print company_id
        # print everyone["comp"]["count"]

        for x in range(everyone["comp"]["count"]):
            # print company_id, every[0]
            DocContent = everyone["comp"]["wenshu"][x]["DocContent"].replace('&amp;#xA;', '').replace("'", '‘').replace(";", "；").replace('(', '（').replace(')', '）').replace('\\', '/')
            updatesql = 'insert into t_fxxx_fayuanpanjue(t_fayuanpanjue_shijian, t_fayuanpanjue_jieguo, t_fayuanpanjue_wenjianlujing, t_fayuanpanjue_gongsi_id, t_fayuanpanjue_biaoti)values("%s", "%s", "%s", "%s", "%s");' %(everyone["comp"]["wenshu"][x][u"裁判日期"], everyone["comp"]["wenshu"][x][u"裁判要旨段原文"], DocContent, company_id, everyone["comp"]["wenshu"][x][u"案件名称"])
            # print 'jjjj'
            # print updatesql
            cursor.execute(updatesql)
        conn.commit()
    except:
        continue
conn.close()
