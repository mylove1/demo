# coding:utf-8
import MySQLdb


DbConfig = {
    "user": "root",
    "passwd": "dingyu",
    "host": "192.168.0.50",
}



conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db="xzs",
                       host=DbConfig['host'], charset='utf8', use_unicode=True)
cursor = conn.cursor()

conn_sb = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db="dingyu",
                       host=DbConfig['host'], charset='utf8', use_unicode=True)


cursor_sb = conn_sb.cursor()
cursor_sb.execute("select weburl_url, weburl_name, weburl_email, weburl_starttime from weburl;")
shangbiaolist = cursor_sb.fetchall()
history = ["", 8]
for enu,every in enumerate(shangbiaolist):
    if enu % 1000 == 0:
        print enu
    try:
        if every[0] == history[0]:
            company_id = history[1]
            # print '0'
        else:
            getidsql = "select t_gongsi_id from t_gongsi where t_gongsi_mingzi='%s';" % every[1]
            cursor.execute(getidsql)
            company_id = cursor.fetchone()[0]
            history[0] = every[0]
            history[1] = company_id
            # print '1'
        # print company_id, every[0]
        updatesql = 'insert into t_zscq_yuming(t_yuming_wangzhi, t_yuming_pizhunriqi, t_shangbiao_gongsi_id)values("%s", "%s", "%s");' %(every[0], every[3], company_id)
        cursor.execute(updatesql)
        conn.commit()
    except:
        continue
conn.close()
conn_sb.close()