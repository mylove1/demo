#!/usr/bin/env python
# coding:utf-8

from svmutil import svm_load_model
import pymongo
import MySQLdb
import pybloom
from xzs_data.xinyonggongshi.jiangsu.jiangsu import JiangSuAnalyze
import threading


DbConfig = {
    "user": "root",
    "passwd": "dingyu",
    "host": "192.168.0.50",
}

class id22info(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        id_list = []
        info_list = []
        while 1:
            try:
                # print self.getName()
                compname = namelist.pop()[0]
            except:
                print '------------------',

                break
            # if compname in bf:
            #     continue
            try:
                a = JiangSuAnalyze(name=compname)
            except:
                continue
            print a.name
            a.get_punish_info()
            # info_list.append(comp.get_gongshi_info())
            # print "公司名称", "\t", a.data["baseInfo"]["name"]
            # print "公司类型", "\t", a.data["baseInfo"]["companyOrgType"]
            # print "法人", "\t", a.data["baseInfo"]["legalPersonName"]
            # print "社会信用代码", "\t", a.data["baseInfo"]["creditCode"]
            # print "注册号", "\t", a.data["baseInfo"]["regNumber"]
            # print "状态", "\t", a.data["baseInfo"]["regStatus"]
            # print "注册资本", "\t", a.data["baseInfo"]["regCapital"]
            # print "登记机关", "\t", a.data["baseInfo"]["regInstitute"]
            # print "注册地址", "\t", a.data["baseInfo"]["regLocation"]
            # print "行业", "\t", a.data["baseInfo"]["industry"]
            # print "电话号码", "\t", a.data["baseInfo"]["phoneNumber"]
            # print "电子邮件", "\t", a.data["baseInfo"]["email"]
            # print "核准日期", "\t", a.data["baseInfo"]["approvedTime"]
            # print "注册时间", "\t", a.data["baseInfo"]["estiblishTime"]
            # print "开始时间", "\t", a.data["baseInfo"]["fromTime"]
            # print "截止时间", "\t", a.data["baseInfo"]["toTime"]
            # print "经营范围", "\t", a.data["baseInfo"]["businessScope"]
            # print '--------------------------\n'


if __name__ == "__main__":
    conn_sour = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db="xzs",
                                host=DbConfig['host'], charset='utf8', use_unicode=True)
    cursor_sour = conn_sour.cursor()
    select_sql = 'select t_gongsi_mingzi from t_gongsi where t_gongsi_id >= %s and t_gongsi_id < %s and t_gongsi_sheng="江苏省";'

    startnum = 90000
    maxnum = 5000000

    while 1:
        print "start: ", startnum
        if startnum >= maxnum:
            print "全部完成"
            break
        endnum = startnum + 10000
        cursor_sour.execute(select_sql % (startnum, endnum))
        namelist = list(cursor_sour.fetchall())
        print "total: ", len(namelist)
        threads = []
        thread_num = 1
        for i in range(thread_num):
            threads.append(id22info())
        for i in range(thread_num):
            threads[i].start()
        for i in range(thread_num):
            threads[i].join()
        print 'ok'

        startnum += 10000
        # break

