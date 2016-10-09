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


if __name__ == '__main__':

    row_list = [
        "t_shangbiao_id",
        "t_shangbiao_mingcheng",
        "t_shangbiao_zhucehao",
        "t_shangbiao_shenqingren",
        "t_shangbiao_gongsi_id",
    ]

    table_sour = "t_zscq_shangbiao"
    table_targ = table_sour
    biao = 0
    biaoshang = 0
    while biao <=400000:

        biao += 100000
        select_condition = "where t_shangbiao_id > %s and t_shangbiao_id <= %s" % (biaoshang, biao)
        biaoshang = biao
        # select_condition = ""

        # 构造查询语句
        select_sql = 'select ' + ','.join(row_list) + ' from ' + table_sour
        if select_condition:
            select_sql += ' ' + select_condition + ';'
        else:
            select_sql += ';'
        # print select_sql

        # 构造插入语句
        insert_sql = ('insert into ' + table_sour + '(' + ','.join(row_list) + ')' +
                     ' values ' + '(' + (len(row_list)-1)*'%s,' + '%s' + ');')

        # print insert_sql

        # 分别连接两个数据库
        conn_sour = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db="xzs",
                               host=DbConfig['host'], charset='utf8', use_unicode=True)
        cursor_sour = conn_sour.cursor()

        # conn_targ = MySQLdb.connect(user="root", passwd="dingyu", db="xzs",
        #                        host="192.168.0.156", charset='utf8', use_unicode=True)
        conn_targ = MySQLdb.connect(user=DbTarg['user'], passwd=DbTarg['passwd'], db="xinzhishang",
                                    host=DbTarg['host'], charset='utf8', use_unicode=True)
        cursor_targ = conn_targ.cursor()


        cursor_sour.execute(select_sql)
        L = []
        datalist = cursor_sour.fetchall()


        for enu, every in enumerate(datalist):
            if every[0] % 1000 == 0:
                print every[0], '\t', time.clock(), '\t', time.ctime()
            L.append(list(every))

            if enu % 1000 == 0:
                # try:
                #     print L
                    cursor_targ.executemany(insert_sql, L)
                    conn_targ.commit()
                    L = []
                # except:
                #     print 'xxx'

        try:
            cursor_targ.executemany(insert_sql, L)
            conn_targ.commit()
        except:
            print 'xxx'



