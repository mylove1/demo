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
cursor_sb.execute("select t_zhuanli_company, t_zhuanli_number, t_zhuanli_type, t_zhuanli_name, t_zhuanli_date from t_zhuanli;")
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
            getidsql = "select t_gongsi_id from t_gongsi where t_gongsi_mingzi='%s';" % every[0]
            cursor.execute(getidsql)
            company_id = cursor.fetchone()[0]
            history[0] = every[0]
            history[1] = company_id
            # print '1'
        # print company_id, every[0]
        updatesql = 'insert into t_zscq_zhuanlixinxi(t_zhuanlixinxi_leixing, t_zhuanlixinxi_shenqinghao, t_zhuanlixinxi_faburiqi, t_zhuanlixinxi_mingcheng, t_zhuanlixinxi_shenqingren, t_zhuanlixinxi_gongsi_id)values("%s", "%s", "%s", "%s", "%s", "%s");' %(every[2], every[1], every[4], every[3], every[0], company_id)
        cursor.execute(updatesql)
        conn.commit()
    except:
        continue
conn.close()
conn_sb.close()