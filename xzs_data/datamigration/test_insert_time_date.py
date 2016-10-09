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
    conn_targ = MySQLdb.connect(user="root", passwd="dingyu", db="xzs",
                           host="192.168.0.156", charset='utf8', use_unicode=True)
    cursor_targ = conn_targ.cursor()
    sql = 'insert into t_gongsi(t_gongsi_id,t_gongsi_mingzi,t_gongsi_hangye,t_gongsi_img,t_gongsi_xinyongdaima,t_gongsi_jigoudaima,t_gongsi_zhucehao, t_gongsi_zhuceshijian, t_gongsi_jingyingzhuangtai, t_gongsi_leixing, t_gongsi_chengliriqi, t_gongsi_fadingren, t_gongsi_yingyeqixian, t_gongsi_zhuceziben, t_gongsi_fazhaoriqi, t_gongsi_dengjijiguan, t_gongsi_qiyedizhi, t_gongsi_dianhua, t_gongsi_jingyingfanwei, t_gongsi_youxiang, t_gongsi_touzigongsiid, t_gongsi_wangzhi, t_gongsi_sheng,t_gongsi_shi)values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");'
    print sql

    L = (
    2222002, u'\u970d\u5dde\u5e02\u8f9b\u7f6e\u519c\u6751\u4fe1\u7528\u5408\u4f5c\u793e\u5317\u6751\u5206\u793e', '', '',
    '', '', u'1426031600306', "2014-01-06", u'\u6ce8\u9500',
    u'\u96c6\u4f53\u5206\u652f\u673a\u6784(\u975e\u6cd5\u4eba)', "2014-1-6", u'\u674e\u6587\u5e73',
    u'2006-06-26\u20142008-03-15', u'5\u4e07\u5143\u4eba\u6c11\u5e01', "2014-1-6",
    u'\u5c71\u897f\u7701\u970d\u5dde\u5e02\u5de5\u5546\u884c\u653f\u7ba1\u7406\u5c40',
    u'\u970d\u5dde\u5e02\u8f9b\u7f6e\u9547\u5317\u6751', '',
    u'*\u519c\u6751\u50a8\u84c4\u5b58\u6b3e\u3001\u519c\u6237\u3001\u4e2a\u4f53\u7ecf\u6d4e\u6237\u3001\u519c\u6751\u5408\u4f5c\u7ecf\u6d4e\u3001\u7ec4\u7ec7\u53ca\u4f01\u4e8b\u4e1a\u5355\u4f4d\u7684\u5b58\u6b3e\u3001\u8d37\u6b3e\u53ca\u7ed3\u7b97\u3001\u7ecf\u4e2d\u56fd\u4eba\u6c11\u94f6\u884c\u6279\u51c6\u7684\u5176\u5b83\u4e1a\u52a1',
    '', '', '', '', '')

    print '-------------'

    print (sql, L)


    sql2 = 'insert into t_gongsi(t_gongsi_id, t_gongsi_zhuceshijian)values(%s, %s);'


    L = [L[0], L[7]]
    cursor_targ.execute(sql2, L)
    conn_targ.commit()
    print 'ok'



