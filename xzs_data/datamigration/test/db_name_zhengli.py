#!/usr/bin/env python
# coding:utf-8

import MySQLdb

DbConfig = {
    "user": "root",
    "passwd": "dingyu",
    "db": "xzs",
    "host": "192.168.0.50",
}


if __name__ == "__main__":
    conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db=DbConfig['db'],
                           host=DbConfig['host'], charset='utf8', use_unicode=True)
    cursor = conn.cursor()
    sql = 'select t_gongsi_id, t_gongsi_mingzi from t_gongsi where t_gongsi_mingzi like "%*";'
    cursor.execute(sql)
    total_list = cursor.fetchall()
    for x in total_list:

    #     if x[1][:3] == u"（１）":
    #         continue
    #
    #
    #     index = x[1].find(u"）")
    #     name = x[1][index+1:]

        name = x[1][0:-1]
        print x[0], '\t', x[1], '\t\t', name




        check_sql = 'select t_gongsi_id, t_gongsi_mingzi from t_gongsi where t_gongsi_mingzi = "%s";' % name
        cursor.execute(check_sql)
        if cursor.fetchall():
            cursor.execute('delete from t_gongsi where t_gongsi_id = %d;' % int(x[0]))
            pass

        else:
            cursor.execute('update t_gongsi set t_gongsi_mingzi = "%s" where t_gongsi_id = %d;' % (name, int(x[0])))
            # cursor.execute('insert into t_gongsi(t_gongsi_mingzi) values("%s");' % (name))
    conn.commit()
    conn.close()


