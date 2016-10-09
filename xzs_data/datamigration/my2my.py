#coding:utf-8
import MySQLdb
import time
import datetime

DbConfig = {
    "user": "root",
    "passwd": "dingyu",
    "host": "192.168.0.50",
}

DbTarg = {
    "user": "xinZhiShang",
    "passwd": "xzs123",
    "host": "192.168.0.121",
}


def to_db(conn, cursor, sql):
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        print'xxxxxxxxxxx'
        pass



if __name__ == '__main__':
    conn_sour = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db="xzs",
                           host=DbConfig['host'], charset='utf8', use_unicode=True)
    cursor_sour = conn_sour.cursor()

    conn_targ = MySQLdb.connect(user="root", passwd="dingyu", db="xzs",
                           host="192.168.0.156", charset='utf8', use_unicode=True)
    cursor_targ = conn_targ.cursor()
    cursor_sour.execute('select t_gongsi_id,t_gongsi_mingzi,t_gongsi_hangye,t_gongsi_img,t_gongsi_xinyongdaima,t_gongsi_jigoudaima,t_gongsi_zhucehao, t_gongsi_zhuceshijian, t_gongsi_jingyingzhuangtai, t_gongsi_leixing, t_gongsi_chengliriqi, t_gongsi_fadingren, t_gongsi_yingyeqixian, t_gongsi_zhuceziben, t_gongsi_fazhaoriqi, t_gongsi_dengjijiguan, t_gongsi_qiyedizhi, t_gongsi_dianhua, t_gongsi_jingyingfanwei, t_gongsi_youxiang, t_gongsi_touzigongsiid, t_gongsi_wangzhi, t_gongsi_sheng,t_gongsi_shi from t_gongsi where t_gongsi_id < 100000;')
    L = []
    datalist = cursor_sour.fetchall()


    for enu, every in enumerate(datalist):
        if enu % 1000 == 0:
            print time.clock()
            print enu
        L.append(list(every))

        if enu % 1000 == 0:
            # try:
                cursor_targ.executemany('insert into t_gongsi(t_gongsi_id,t_gongsi_mingzi,t_gongsi_hangye,t_gongsi_img,t_gongsi_xinyongdaima,t_gongsi_jigoudaima,t_gongsi_zhucehao, t_gongsi_zhuceshijian, t_gongsi_jingyingzhuangtai, t_gongsi_leixing, t_gongsi_chengliriqi, t_gongsi_fadingren, t_gongsi_yingyeqixian, t_gongsi_zhuceziben, t_gongsi_fazhaoriqi, t_gongsi_dengjijiguan, t_gongsi_qiyedizhi, t_gongsi_dianhua, t_gongsi_jingyingfanwei, t_gongsi_youxiang, t_gongsi_touzigongsiid, t_gongsi_wangzhi, t_gongsi_sheng,t_gongsi_shi)values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', L)
                conn_targ.commit()
                L = []
            # except:
            #     print 'xxx'

    try:
        cursor_targ.executemany('insert into t_gongsi(t_gongsi_id,t_gongsi_mingzi,t_gongsi_hangye,t_gongsi_img,t_gongsi_xinyongdaima,t_gongsi_jigoudaima,t_gongsi_zhucehao, t_gongsi_zhuceshijian, t_gongsi_jingyingzhuangtai, t_gongsi_leixing, t_gongsi_chengliriqi, t_gongsi_fadingren, t_gongsi_yingyeqixian, t_gongsi_zhuceziben, t_gongsi_fazhaoriqi, t_gongsi_dengjijiguan, t_gongsi_qiyedizhi, t_gongsi_dianhua, t_gongsi_jingyingfanwei, t_gongsi_youxiang, t_gongsi_touzigongsiid, t_gongsi_wangzhi, t_gongsi_sheng,t_gongsi_shi)values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', L)
        conn_targ.commit()
    except:
        print 'xxx'



