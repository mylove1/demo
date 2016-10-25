#!/usr/bin/env python
# coding:utf-8

from svmutil import svm_load_model
import pymongo
import MySQLdb
from xzs_data.xinyonggongshi.jiangsu.jiangsu import JiangSuAnalyze
import threading
import time


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
                if id_list:
                    print '------------------',
                    db.jiangsu_all_id.insert(id_list)
                    db.jiangsu_all_info.insert(info_list)
                    # print "chucuo"
                    print '>>>>>>>>>>'
                break
            # if compname in bf:
            #     continue
            try:
                comp = JiangSuAnalyze(name=compname)
            except:
                continue
            # print comp.name
            id_list.append(comp.all_id)
            info_list.append(comp.get_gongshi_info())


if __name__ == "__main__":
    conn = pymongo.Connection("192.168.0.50", 27017)
    db = conn.gongshi_id
    # bf = pybloom.BloomFilter(500000, 0.001)
    # print "开始加载已有记录...",
    # for x in db.chongqing_id.find():
        # print x
        # try:
        #     bf.add(x["name"])
        # except:
        #     continue
    # print "加载完成"

    conn_sour = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db="xzs",
                                host=DbConfig['host'], charset='utf8', use_unicode=True)
    cursor_sour = conn_sour.cursor()
    select_sql = 'select t_gongsi_mingzi from t_gongsi where t_gongsi_id >= %s and t_gongsi_id < %s and t_gongsi_sheng="江苏省";'

    startnum = 2502000
    maxnum = 5000000
    step = 500
    # model = svm_load_model("jiangsu.mo")

    while 1:
        print "start: ", startnum, time.ctime()
        if startnum >= maxnum:
            print "全部完成"
            break
        endnum = startnum + step
        cursor_sour.execute(select_sql % (startnum, endnum))
        namelist = list(cursor_sour.fetchall())
        print "total: ", len(namelist)
        threads = []
        thread_num = 10
        for i in range(thread_num):
            threads.append(id22info())
        for i in range(thread_num):
            threads[i].start()
        for i in range(thread_num):
            threads[i].join()

        startnum += step
        # break

