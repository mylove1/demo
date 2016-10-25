#!/usr/bin/env python
# coding:utf-8

import pymongo
import time
import MySQLdb

DbConfig = {
    "user": "root",
    "passwd": "dingyu",
    "host": "192.168.0.156",
}


class mult_insert():
    def __init__(self, conn, cursor, table, column, lenth=1000):
        self.conn = conn
        self.cursor = cursor
        self.table = table
        self.column = column
        self.list = []
        self.lenth = lenth
        self.sql = self.get_sql()
        pass

    def get_sql(self):
        column = ','.join(self.column)
        values = ','.join(['%s' for _ in range(len(self.column))])
        sql = 'INSERT INTO %s(%s) VALUES(%s);' % (self.table,
                                                  column,
                                                  values)
        return sql

    def insert(self):
        self.cursor.executemany(self.sql, self.list)
        self.conn.commit()
        self.list = []

    def append(self, l):
        self.list.append(l)
        if len(self.list) >= self.lenth:
            self.insert()


class mult_mapping_insert(mult_insert):
    def __init__(self, conn, cursor, table,
                 column, lenth=1000, mapping={}):
        self.conn = conn
        self.cursor = cursor
        self.table = table
        self.column = column
        self.list = []
        self.lenth = lenth
        self.sql = self.get_sql()
        self.mapping = mapping
        pass

    def dict_list(self, dic):
        return [dic[self.mapping[x]] for x in self.column]

    def append(self, l, dic={}):
        if dic:
            l = self.dict_list(dic)
        self.list.append(l)
        if len(self.list) >= self.lenth:
            self.insert()



class Mongo_MySQL():
    def __init__(self, connect, cursor, config=False):
        self.connect = connect
        self.cursor = cursor
        self.config = config if config else self.set_config()

    def set_config(self):
        config = {
            # 'xingzhengxukeInfo': {
            #     'name': '',
            #     'table': '',
            #     'column': [],
            #     'mapping': {}
            # },
            'xingzhengxukeInfo': {
                'name': '',
                'table': '',
                'column': [],
                'mapping': {}
            },
            'staffList': {},
            'touzichuziInfo': {},
            'baseInfo': {},
            'comChanInfoList': {},
            'chuzhiList': {},
            'zhishichuzhiInfo': {},
            'abnormalList': {},
            'annuRepYearList': {},
            'checkList': {},
            'investorList': {},
            'branchList': {},
            'punishList': {},
            'mortgageList': {},
            'website': {},
            'baseinfo': {},
            'stock': {},
            'security': {},
            'change': {},
            'assets': {},
        }
        return config

    def data_db(self, data, conf, meta):
        data = dict(data.items() + meta.items())
        print '------------------------------------'
        print '数据是：'
        print data
        print '配置文件是：'
        print conf
        print '元信息是：'
        print meta

    def list_analysis(self, data, conf, meta):
        for x in data:
            self.analysis(x, conf, meta)

    def dict_analysis(self, data, conf, meta):
        for a in data.keys():
            if isinstance(data[a], str) or isinstance(data[a], unicode):
                self.data_db(data, conf, meta)
                break
            else:
                try:
                    self.analysis(data[a], conf[a], meta)
                except:
                    self.analysis(data[a], conf, meta)

    def analysis(self, data, conf, meta):
        if isinstance(data, dict):
            # 年报时，添加元信息
            if 'baseinfo' in data.keys():
                meta["year"] = data["baseinfo"]["reportYear"]
            self.dict_analysis(data, conf, meta)
        elif isinstance(data, list) or isinstance(data, tuple):
            self.list_analysis(data, conf, meta)


    def append(self, dic):
        # 在解析json格式的数据时，经常会用到上下相邻的数据，
        # 现在把这些会用到的数据放到meta里
        meta = {}
        meta["compName"] = dic["baseInfo"]["name"]
        xzsid = self.get_xzsid(cursor=self.cursor,
                               name=meta["compName"])
        if not xzsid:
            print '在公司列表里没有%s' % meta["compName"]
            return ''
        meta["xzsId"] = xzsid
        self.analysis(dic, self.config, meta)
        return 1

    def end(self):
        pass

    def get_xzsid(self, cursor, name):
        sql = 'select t_gongsi_id from t_gongsi where t_gongsi_mingzi = "%s";' % name
        cursor.execute(sql)
        try:
            return cursor.fetchall()[0][0]
        except:
            return 0


def get_xzsid(cursor, name):
    sql = 'select t_gongsi_id from t_gongsi where t_gongsi_mingzi = "%s";' % name
    cursor.execute(sql)
    try:
        return cursor.fetchall()[0][0]
    except:
        return 0


if __name__ == '__main__':
    data = {
    u'abnormalList': [
        {
            u'institute': u'宜兴市市场监督管理局',
            u'inReason': u'在2015年6月30日前未按规定报送2014年度年度报告，根据《企业经营异常名录管理暂行办法》第六条之规定列入经营异常名录',
            u'outTime': None,
            u'inTime': u'2015-07-10',
            u'outReason': None
        }
    ],
    u'xingzhengxukeInfo': [

    ],
    u'annuRepYearList': [
        {
            u'website': [

            ],
            u'assets': {
                u'profitTotal': u'企业选择不公示',
                u'netAmount': u'企业选择不公示',
                u'debtAmount': u'企业选择不公示',
                u'profitReta': u'企业选择不公示',
                u'mainIncome': u'企业选择不公示',
                u'saleIncome': u'企业选择不公示',
                u'totalEquity': u'企业选择不公示',
                u'taxTotal': u'企业选择不公示'
            },
            u'baseinfo': {
                u'connectLocation': u'屺亭街道三阳居委',
                u'if_website': u'否',
                u'zipCode': u'214266',
                u'if_equity': u'',
                u'regNumber': u'320282000076792',
                u'regStatus': u'停业',
                u'creditCode': u'',
                u'reportYear': 2015,
                u'phoneNumber': u'13601530555',
                u'email': u'0',
                u'if_invest': u'否',
                u'name': u'江苏星能电池有限公司'
            },
            u'security': [

            ],
            u'change': [

            ],
            u'stock': [
                {
                    u'realcapitype': u'货币',
                    u'stockname': u'吴庆元',
                    u'real_capidate': u'603.9万元人民币',
                    u'shouldcapidate': u'2010年04月09日',
                    u'shouldccapi': u'1098万元人民币',
                    u'real_capi': u'603.9万元人民币',
                    u'shouldcapitype': u'货币'
                }
            ]
        },
        {
            u'website': [

            ],
            u'assets': {
                u'profitTotal': u'企业选择不公示',
                u'netAmount': u'企业选择不公示',
                u'debtAmount': u'企业选择不公示',
                u'profitReta': u'企业选择不公示',
                u'mainIncome': u'企业选择不公示',
                u'saleIncome': u'企业选择不公示',
                u'totalEquity': u'企业选择不公示',
                u'taxTotal': u'企业选择不公示'
            },
            u'baseinfo': {
                u'connectLocation': u'宜兴市宜城街道三阳居委',
                u'if_website': u'否',
                u'zipCode': u'214200',
                u'if_equity': u'',
                u'regNumber': u'320282000076792',
                u'regStatus': u'开业/正常经营',
                u'creditCode': u'',
                u'reportYear': 2014,
                u'phoneNumber': u'87597969',
                u'email': u'',
                u'if_invest': u'否',
                u'name': u'江苏星能电池有限公司'
            },
            u'security': [

            ],
            u'change': [

            ],
            u'stock': [
                {
                    u'realcapitype': u'货币',
                    u'stockname': u'吴庆元',
                    u'real_capidate': u'603.9万元人民币',
                    u'shouldcapidate': u'2010年04月09日',
                    u'shouldccapi': u'603.9万元人民币',
                    u'real_capi': u'603.9万元人民币',
                    u'shouldcapitype': u'货币'
                },
                {
                    u'realcapitype': u'货币',
                    u'stockname': u'王燕飞',
                    u'real_capidate': u'491.1万元人民币',
                    u'shouldcapidate': u'2010年04月09日',
                    u'shouldccapi': u'491.1万元人民币',
                    u'real_capi': u'491.1万元人民币',
                    u'shouldcapitype': u'货币'
                }
            ]
        },
        {
            u'website': [

            ],
            u'assets': {
                u'profitTotal': u'企业选择不公示',
                u'netAmount': u'企业选择不公示',
                u'debtAmount': u'企业选择不公示',
                u'profitReta': u'企业选择不公示',
                u'mainIncome': u'企业选择不公示',
                u'saleIncome': u'企业选择不公示',
                u'totalEquity': u'企业选择不公示',
                u'taxTotal': u'企业选择不公示'
            },
            u'baseinfo': {
                u'connectLocation': u'宜兴市屺亭街道三阳居委',
                u'if_website': u'否',
                u'zipCode': u'214267',
                u'if_equity': u'',
                u'regNumber': u'320282000076792',
                u'regStatus': u'开业/正常经营',
                u'creditCode': u'',
                u'reportYear': 2013,
                u'phoneNumber': u'87597969',
                u'email': u'',
                u'if_invest': u'否',
                u'name': u'江苏星能电池有限公司'
            },
            u'security': [

            ],
            u'change': [

            ],
            u'stock': [
                {
                    u'realcapitype': u'货币',
                    u'stockname': u'王燕飞',
                    u'real_capidate': u'494.1万元人民币',
                    u'shouldcapidate': u'2010年04月09日',
                    u'shouldccapi': u'494.1万元人民币',
                    u'real_capi': u'494.1万元人民币',
                    u'shouldcapitype': u'货币'
                },
                {
                    u'realcapitype': u'货币',
                    u'stockname': u'吴庆元',
                    u'real_capidate': u'603.9万元人民币',
                    u'shouldcapidate': u'2010年04月09日',
                    u'shouldccapi': u'603.9万元人民币',
                    u'real_capi': u'603.9万元人民币',
                    u'shouldcapitype': u'货币'
                }
            ]
        }
    ],
    u'staffList': [
        {
            u'position': u'总经理',
            u'id': u'',
            u'name': u'吴庆元'
        },
        {
            u'position': u'执行董事',
            u'id': u'',
            u'name': u'吴庆元'
        },
        {
            u'position': u'监事',
            u'id': u'',
            u'name': u'王燕飞'
        }
    ],
    u'checkList': [
        {
            u'institute': u'宜兴市市场监督管理局开发区分局',
            u'type': u'抽查',
            u'result': u'公示信息正常',
            u'time': u'2016-05-05'
        }
    ],
    u'chuzhiList': [

    ],
    u'touzichuziInfo': [
        {
            u'leijishijiao': u'491.1万元人民币',
            u'name': u'王燕飞',
            u'chuzishijian': u'2010年04月09日',
            u'renjiaochuzi': u'491.1万元人民币',
            u'shijiaochuzishijian': u'2010年04月09日',
            u'leijirenjiao': u'491.1万元人民币',
            u'shijiaochuzifangshi': u'货币',
            u'type': u'自然人股东',
            u'shijiaochuzi': u'491.1万元人民币',
            u'chuzifangshi': u'货币'
        },
        {
            u'leijishijiao': u'603.9万元人民币',
            u'name': u'吴庆元',
            u'chuzishijian': u'2010年04月09日',
            u'renjiaochuzi': u'603.9万元人民币',
            u'shijiaochuzishijian': u'2010年04月09日',
            u'leijirenjiao': u'603.9万元人民币',
            u'shijiaochuzifangshi': u'货币',
            u'type': u'自然人股东',
            u'shijiaochuzi': u'603.9万元人民币',
            u'chuzifangshi': u'货币'
        }
    ],
    u'baseInfo': {
        u'regCapital': u'1098万元人民币',
        u'name': u'江苏星能电池有限公司',
        u'industry': u'',
        u'legalPersonName': u'吴庆元',
        u'businessScope': u'锂电池的组装、销售；蓄电池销售。（依法须经批准的项目，经相关部门批准后方可开展经营活动）',
        u'estiblishTime': u'2006-04-24',
        u'approvedTime': u'2015-08-24',
        u'creditCode': u'',
        u'regNumber': u'320282000076792',
        u'regStatus': u'在业',
        u'toTime': u'2026-04-20',
        u'regInstitute': u'宜兴市市场监督管理局',
        u'regLocation': u'宜兴市屺亭街道三阳居委',
        u'phoneNumber': u'',
        u'fromTime': u'2006-04-24',
        u'email': u'',
        u'companyOrgType': u'有限责任公司(自然人独资)'
    },
    u'investorList': [
        {
            u'name': u'吴庆元',
            u'papertype': u'身份证',
            u'amount': u'',
            u'papernum': None,
            u'type': u'境内中国公民',
            u'id': u''
        }
    ],
    u'branchList': [

    ],
    u'mortgageList': [

    ],
    u'comChanInfoList': [
        {
            u'changeTime': u'2015-08-24',
            u'changeItem': u'企业类型变更',
            u'changeBefore': u'有限责任公司(自然人投资或控股)',
            u'changeAfter': u'有限责任公司(自然人独资)'
        },
        {
            u'changeTime': u'2015-08-24',
            u'changeItem': u'经营范围',
            u'changeBefore': u'锂电池的组装、销售；蓄电池销售。',
            u'changeAfter': u'锂电池的组装、销售；蓄电池销售。（依法须经批准的项目，经相关部门批准后方可开展经营活动）'
        },
        {
            u'changeTime': u'2015-08-24',
            u'changeItem': u'股东变更',
            u'changeBefore': u'吴庆元,王燕飞',
            u'changeAfter': u'吴庆元'
        }
    ],
    u'punishList': [],
    u'zhishichuzhiInfo': [

    ]
}


    # # 连接MySQL
    conn = MySQLdb.connect(user=DbConfig['user'], passwd=DbConfig['passwd'], db="xzstest",
                           host=DbConfig['host'], charset='utf8', use_unicode=True)
    cursor = conn.cursor()
    print '---------------------'
    a = Mongo_MySQL(conn, cursor)
    a.append(data)

    print '---------------------'




    conn.close()


    # conn_mongo = pymongo.Connection(host='192.168.0.50', port=27017)
    # db = conn_mongo.gongshi_id
    #
    # print db.jiangsu_all_info.find({u"baseInfo.name": u"江苏星能电池有限公司"})[0]
