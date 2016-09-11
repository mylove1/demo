# coding:utf-8
'''
从mongo里的悉知网上的基本信息，转成sql语句形式
'''
# coding:utf-8
import pymongo
MASTERIP = '192.168.0.2'
conn = pymongo.Connection(MASTERIP, 27017)
db = conn.xizhi

infolist = db.compinfo.find().limit(50)
with open('t_gongsi_xizhi.sql', 'w') as f:
    for x in infolist:
        print '1'
        name = x["name"],
        xinyongid = x["baseinfo"]["xinyongid"],
        zuzhijigouid = x["baseinfo"]["zuzhijigouid"],
        zhucehao = x["baseinfo"]["zhucehao"],
        jingyingriqi = x["baseinfo"]["jingyingriqi"],
        status = x["baseinfo"]["status"],
        type = x["baseinfo"]["type"],
        fazhaoriqi = x["baseinfo"]["fazhaoriqi"],
        faren = x["baseinfo"]["faren"],
        yingyeqixian = x["baseinfo"]["yingyeqixian"],
        zhuceziben = x["baseinfo"]["zhuceziben"],
        fazhaoriqi = x["baseinfo"]["fazhaoriqi"],
        dengjijiguan = x["baseinfo"]["dengjijiguan"],
        qiyedizhi = x["baseinfo"]["qiyedizhi"],
        fanwei = x["baseinfo"]["fanwei"],
        wangzhi = x["baseinfo"]["wangzhi"]
        f.write("INSERT INTO t_gongsi\
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
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);\n" %(
        name,
        xinyongid,
        zuzhijigouid,
        zhucehao,
        jingyingriqi,
        status,
        type,
        fazhaoriqi,
        faren,
        yingyeqixian,
        zhuceziben,
        fazhaoriqi,
        dengjijiguan,
        qiyedizhi,
        fanwei,
        wangzhi,
        ))
        print x

