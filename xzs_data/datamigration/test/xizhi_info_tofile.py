# coding:utf-8
import pymongo
import sys
import MySQLdb
import time
reload(sys)
try:
    sys.setdefaultencoding("utf-8")
except:
    reload(sys)
    sys.setdefaultencoding("utf-8")
MASTERIP = '192.168.0.2'
conn = pymongo.Connection(MASTERIP, 27017)
db = conn.xizhi
DbConfig = {
    "user": "root",
    "passwd": "dingyu",
    "db": "xinzhishang",
    "host": "192.168.0.50",
}
# conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db=DbConfig['db'],
#                             host=DbConfig['host'], charset='utf8', use_unicode=True)
# cursor = conn.cursor()
starttime = time.time()
infolist = db.compinfo.find().limit(10000)
with open('E:\\t_gongsi_xizhi.sql', 'w') as f:
    for enu, x in enumerate(infolist):
        # if enu <= 800000 : continue
        # if enu >= 1000: continue
        # if enu < 9740: continue
        # if enu < 9740: continue
        # if enu < 9740: continue
        # if enu < 9740: continue
        # if enu < 9740: continue
        # if enu < 9740: continue
        sql = ("INSERT INTO t_gongsi\
(t_gongsi_mingzi, \
t_gongsi_xinyongdaima,\
t_gongsi_jigoudaima,\
t_gongsi_zhucehao,\
t_gongsi_zhuceshijian,\
t_gongsi_jingyingzhuangtai,\
t_gongsi_leixing,\
t_gongsi_chengliriqi,\
t_gongsi_fadingren,\
t_gongsi_yingyeqixian,\
t_gongsi_zhuceziben,\
t_gongsi_fazhaoriqi,\
t_gongsi_dengjijiguan,\
t_gongsi_qiyedizhi,\
t_gongsi_jingyingfanwei,\
t_gongsi_wangzhi)\
VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" %(
                    x["name"],
                    x["baseinfo"]["xinyongid"],
                    x["baseinfo"]["zuzhijigouid"],
                    x["baseinfo"]["zhucehao"],
                    x["baseinfo"]["jingyingriqi"] if x["baseinfo"]["jingyingriqi"] != '-' else '',
                    x["baseinfo"]["status"],
                    x["baseinfo"]["type"],
                    x["baseinfo"]["fazhaoriqi"] if x["baseinfo"]["fazhaoriqi"] != '-' else '',
                    x["baseinfo"]["faren"].replace("'", "‘"),
                    x["baseinfo"]["yingyeqixian"],
                    x["baseinfo"]["zhuceziben"],
                    x["baseinfo"]["fazhaoriqi"] if x["baseinfo"]["fazhaoriqi"] != '-' else '',
                    x["baseinfo"]["dengjijiguan"].replace('(', '（').replace(')', '）'),
                    x["baseinfo"]["qiyedizhi"],
                    x["baseinfo"]["fanwei"].replace("'", "‘").replace('"', '“').replace(';', '；'),
                    x["baseinfo"]["wangzhi"]
        ))
        # sql = str({"name": sql})[11:-2]
        # sql = sql.replace(", )", ", '')")
        # sql = sql.replace(", ,", ", '',")
        # sql = sql.replace(", ,", ", '',")
        # sql = sql.replace(", ,", ", '',")
        # sql = sql.replace(", ,", ", '',")
        # sql = sql.replace(", ,", ", '',")
        # sql = sql.replace(", ,", ", '',")
        # print enu, sql
        # try:
        #     cursor.execute(sql)
        # except:continue
        # conn.commit()
        f.write(sql)
        f.write('\n')

        if enu%1000 == 0:
            print enu
print '总共用时：%f'%(time.time()-starttime)
# conn.close()
