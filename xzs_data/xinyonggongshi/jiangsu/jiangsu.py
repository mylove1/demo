# /usr/bin/env python
# coding:utf-8

import json
import re
import requests
from __init__ import Analyze


class JiangSuAnalyze(Analyze):
    def __init__(self, name=None, org=None, jsid=None, seqid=None):
        self.data = {}
        self.mark = {
        "basic": 0,
        "investor": 0,
        "comchan": 0,
        "staff": 0,
        "branch": 0,
        "mortgage": 0,
        "chuzhi": 0,
        "punish": 0,
        "abnormal": 0,
        "check": 0,
        "report": 0,
        "touzichuzi": 0,
        "xingzhengxuke": 0,
        "zhishichuzhi": 0,
        }
        self.gongshang_info = ""
        if org and id and seqid:
            self.name = name
            self.org = org
            self.jsid = jsid
            self.seqid = seqid
        else:
            l = self.name_idlist(name)[0]
            self.name = l["name"]
            self.org = l["org"]
            self.jsid = l["jsid"]
            self.seqid = l["seqid"]
        self.all_id = {
            "name": self.name,
            "org": self.org,
            "jsid": self.jsid,
            "seqid": self.seqid,
        }
        self.headers = {
            'Host': 'www.jsgsj.gov.cn:58888',
            'Origin': 'http://www.jsgsj.gov.cn:58888',
            'Referer': 'http://www.jsgsj.gov.cn:58888/ecipplatform/inner_ci/ci_queryCorpInfor_gsRelease.jsp',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

    def get_html(self, link):
        r = requests.get(url=link, headers=self.headers)
        return r.text

    def post_json(self, link, data):
        while 1:
            try:
                r = requests.post(url=link, data=data, headers=self.headers, timeout=7)
                break
            except:
                print 'try again'
                pass
        # print r.text
        return r.json()

    def get_dict(self, link=None, text=None):
        while 1:
            if link:
                text = self.get_html(link)
            try:
                if text[:11] == '{"code":-1}':
                    return {}
                return json.loads(text[6:])
            except:
                print text
                continue

    def html_id_list(self, text):
        """
        对查询页面进行解析
        :param text:
        :return: list，包含企业名称
        """
        rea = re.compile("""gsRelease\.jsp','(.*?)','(.*?)','(.*?)','.*?','.*?','ecippla.*?>(.*?)<""")
        text = ''.join(text.split())
        l = []
        for jilu in rea.findall(text):
            l.append({"name": jilu[3],  # 企业名称
                      "jsid": jilu[1],    # 内部ID
                      "org": jilu[0],   # 内部ID
                      "seqid": jilu[2]  # 内部ID
                      })
        return l

    def name_idlist(self, name):
        """"
        江苏在搜索的时候验证码随便输入几个字母就可以了，不需要识别
        对传入的企业名称进行查询，返回一个列表，包含企业名称，信用代码，regid
        返回的结果可能为空，也可能有几个
        :param name:
        :return:
        """
        while 1:
            code = 'sdfff'
            data = {"name": name,
                    "verifyCode": code,
                    }
            r = requests.post(url='http://www.jsgsj.gov.cn:58888/province/infoQueryServlet.json?queryCinfo=true', data=data)
            if u"验证码填写错误" in r.text:
                continue
            # print r.status_code
            return self.html_id_list(r.text)


    def dict_mapping_dict(self, dic1, dic_map, dic_2):
        for x in dic_map.keys():
            try:
                dic1[x] = ''.join(dic_2[dic_map[x]].split())
            except:
                pass

    def get_basic_info(self):
        if self.mark["basic"]:
            return self.data["baseInfo"]
        else:
            self.mark["basic"] = 1
        self.data["baseInfo"] = {
                "name": "",             # 公司名称
                "businessScope": "",    # 经营范围
                "companyOrgType": "",   # 公司类型
                "legalPersonName": "",  # 法人
                "creditCode": "",       # 统一社会信用代码
                "regNumber": "",        # 工商注册号
                "regStatus": "",        # 状态

                "regCapital": "",       # 注册资本
                "regInstitute": "",     # 登记机关
                "regLocation": "",      # 注册地址

                "industry": "",         # 行业

                "phoneNumber": "",      # 电话号码
                "email": "",            # 电子邮件

                "approvedTime": "",     # 核准日期
                "estiblishTime": "",    # 注册时间
                "fromTime": "",         # 开始经营期限
                "toTime": "",           # 结束经营期限
        }

        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/ciServlet.json?ciEnter=true"
        # print link
        data = {
            "org": self.org,
            "id": self.jsid,
            "seq_id": self.seqid,
            "specificQuery": "basicInfo"
        }
        # print data
        basic_info = self.post_json(link=link, data=data)[0]
        # print basic_info
        if len(basic_info["C1"]) >=17:
            self.data["baseInfo"]["creditCode"] = basic_info["C1"]
        else:
            self.data["baseInfo"]["regNumber"] = basic_info["C1"]
        self.data["baseInfo"]["name"] = basic_info["C2"]
        self.data["baseInfo"]["companyOrgType"] = basic_info["C3"]

        if basic_info["C3"] in [u"有限责任公司分公司",]:
            dic_map = {
                "legalPersonName": "C4",
                "regLocation": "C5",
                "businessScope": "C6",
                "fromTime": "C7",
                "toTime": "C8",
                "regInstitute": "C9",
                "estiblishTime": "C10",
                "approvedTime": "C11",
                "regStatus": "C12",
            }
            self.dict_mapping_dict(self.data["baseInfo"], dic_map, basic_info)

        elif basic_info["C3"] in [u"农民专业合作社",

                                ]:
            dic_map = {
                "estiblishTime": "C4",
                "legalPersonName": "C5",
                "regCapital": "C6",
                "regLocation": "C7",
                "businessScope": "C8",
                "regInstitute": "C9",
                "fromTime": "C4",
                "approvedTime": "C10",
                "regStatus": "C13",
            }
            self.dict_mapping_dict(self.data["baseInfo"], dic_map, basic_info)
        else:
            dic_map = {
                "estiblishTime": "C4",
                "legalPersonName": "C5",
                "regCapital": "C6",
                "regLocation": "C7",
                "businessScope": "C8",
                "fromTime": "C9",
                "toTime": "C10",
                "regInstitute": "C11",
                "approvedTime": "C12",
                "regStatus": "C13",
            }
            self.dict_mapping_dict(self.data["baseInfo"], dic_map, basic_info)
        return self.data["baseInfo"]

    def get_investor_info(self):
        if self.mark["investor"]:
            return self.data["investorList"]
        else:
            self.mark["investor"] = 1
        self.data["investorList"] = []
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/fieiServlet.json?fieibTZR=true"
        data = {
            "org": self.org,
            "id": self.jsid,
            "seq_id": self.seqid,
            "pageNo": "1",
            "pageSize": "500",
        }
        investorInfo = self.post_json(link=link, data=data)
        for every in investorInfo["items"]:
            self.data["investorList"].append({
                "amount": "",   # 投资金额
                "id": "",       # 投资人ID
                "name": every["C2"],     # 投资人
                "type": every["C1"],     # 投资人类型
                "papertype": every["C3"],    # 证书类型
                "papernum": every["C4"],  # 证书号码
            })
        return self.data["investorList"]

    def get_comchan_info(self):
        if self.mark["comchan"]:
            return self.data["comChanInfoList"]
        else:
            self.mark["comchan"] = 1
        self.data["comChanInfoList"] = []
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/commonServlet.json?commonEnter=true"
        data = {
            "showRecordLine": "1",
            "specificQuery": "commonQuery",
            "propertiesName": "biangeng",
            "corp_org": self.org,
            "corp_id": self.jsid,
            "corp_seq_id": self.seqid,
            "pageNo": "1",
            "pageSize": "500",
        }
        comChanInfo = self.post_json(link=link, data=data)

        for every in comChanInfo["items"]:
            self.data["comChanInfoList"].append({
                "changeItem": every["C1"],   # 变更事项
                "changeTime": every["C4"],   # 变更时间
                "changeAfter": every["C3"],  # 变更后
                "changeBefore": every["C2"],  # 变更前
            })
        return self.data["comChanInfoList"]

    def get_staff_info(self):
        if self.mark["staff"]:
            return self.data["staffList"]
        else:
            self.mark["staff"] = 1
        self.data["staffList"] = []
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/ciServlet.json?ciEnter=true"
        data = {
            "showRecordLine": "1",
            "specificQuery": "personnelInformation",
            "CORP_ORG": self.org,
            "CORP_ID": self.jsid,
            "CORP_SEQ_ID": self.seqid,
            "pageNo": "1",
            "pageSize": "500",
        }
        staffInfo = self.post_json(link=link, data=data)
        for every in staffInfo["items"]:
            try:
                self.data["staffList"].append(
                    {
                        "id": "",
                        "name": every["PERSON_NAME2"],
                        "position": every["POSITION_NAME2"]
                    }
                )
            except:
                pass
            finally:
                self.data["staffList"].append(
                    {
                        "id": "",
                        "name": every["PERSON_NAME1"],
                        "position": every["POSITION_NAME1"]
                    }
                )
        return self.data["staffList"]

    def get_branch_info(self):
        if self.mark["branch"]:
            return self.data["branchList"]
        else:
            self.mark["branch"] = 1
        self.data["branchList"] = []
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/ciServlet.json?ciEnter=true"
        data = {
            "showRecordLine": "1",
            "specificQuery": "branchOfficeInfor",
            "CORP_ORG": self.org,
            "CORP_ID": self.jsid,
            "CORP_SEQ_ID": self.seqid,
            "pageNo": "1",
            "pageSize": "500",
        }
        branchInfo = self.post_json(link=link, data=data)

        for every in branchInfo["items"]:
            self.data["branchList"].append({
                "name": every["C2"]
            })
        return self.data["branchList"]

    def get_mortgage_info(self):
        if self.mark["mortgage"]:
            return self.data["mortgageList"]
        else:
            self.mark["mortgage"] = 1
        self.data["mortgageList"] = []
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/commonServlet.json?commonEnter=true"
        data = {
            "showRecordLine": "1",
            "specificQuery": "commonQuery",
            "propertiesName": "dongchan",
            "corp_org": self.org,
            "corp_id": self.jsid,
            "corp_seq_id": self.seqid,
            "pageNo": "1",
            "pageSize": "500",
        }
        mortgageInfo = self.post_json(link=link, data=data)

        for every in mortgageInfo["items"]:
            self.data["mortgageList"].append(
                {
                    "registerTime": every["C2"],  # 登记日期
                    "num": every["C1"],  # 编号
                    "regInstitute": every["C3"],  # 登记机关
                    "kind": every["ASSURE_KIND"],  # 种类
                    "amount": every["C4"],  # 被担保债券数额
                    "term": "",  # 债务人履行债务的期限
                    "scope": every["ASSURE_SCOPE"],  # 担保范围
                    "status": every["C5"],  # 状态
                }
            )
        return self.data["mortgageList"]

    def get_chuzhi_info(self):
        if self.mark["chuzhi"]:
            return self.data["chuzhiList"]
        else:
            self.mark["chuzhi"] = 1
        self.data["chuzhiList"] = []
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/commonServlet.json?commonEnter=true"
        data = {
            "showRecordLine": "1",
            "specificQuery": "commonQuery",
            "propertiesName": "guquanchuzhi",
            "corp_org": self.org,
            "corp_id": self.jsid,
            "corp_seq_id": self.seqid,
            "pageNo": "1",
            "pageSize": "500",
        }
        chuzhiInfo = self.post_json(link=link, data=data)
        for every in chuzhiInfo["items"]:
            re_chuzhi = re.compile("<td.*?<\/td><.*?>(.*?)<\/td><.*?>(.*?)"
                                   "<\/td><.*?>(.*?)<\/td><.*?>(.*?)<\/td>"
                                   "<.*?>(.*?)(.*?)<\/td><.*?>(.*?)<\/td>"
                                   "<td.*?>(.*?)<\/td><td.*?>(.*?)<\/td>")
            chuzhi = re_chuzhi.findall(every["D1"])
            if chuzhi:
                chuzhi = chuzhi[0]
            else:
                continue
            self.data["chuzhiList"].append(
                {
                    "registerTime": chuzhi[6],  # 登记日期
                    "num": chuzhi[0],  # 编号
                    "chuzhiren": chuzhi[1],  # 出质人
                    "zhiquanren": chuzhi[4],  # 质权人
                    "status": chuzhi[7],  # 状态
                    "chuzhiguquanshu": chuzhi[3],  # 出质股权数
                    "chuzhirenzhengjianhao": chuzhi[2],  # 出质人证件号码
                    "zhiquanrenzhengjianhao": chuzhi[5]  # 质权人证件号
                }
            )
        return self.data["chuzhiList"]

    def get_punish_info(self):
        if self.mark["punish"]:
            return self.data["punishiList"]
        else:
            self.mark["punish"] = 1
        self.data["punishList"] = []
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/commonServlet.json?commonEnter=true"
        data = {
            "showRecordLine": "1",
            "specificQuery": "commonQuery",
            "propertiesName": "chufa",
            "corp_org": self.org,
            "corp_id": self.jsid,
            "corp_seq_id": self.seqid,
            "pageNo": "1",
            "pageSize": "500",
        }
        punishInfo = self.post_json(link=link, data=data)

        for every in punishInfo["items"]:
            self.data["punishList"].append(
                {
                    "num": every["C1"],     # 行政处罚决定书文号
                    "type": every["C2"],    # 违法行为类型
                    "content": every["C3"], # 行政处罚内容
                    "institute": every["C4"],   # 决定机关
                    "time": every["C5"],        # 做出行政处罚的日期
                }
            )
        return self.data["punishList"]

    def get_abnormal_info(self):
        if self.mark["abnormal"]:
            return self.data["abnormalList"]
        else:
            self.mark["abnormal"] = 1
        self.data["abnormalList"] = []
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/commonServlet.json?commonEnter=true"
        data = {
            "showRecordLine": "1",
            "specificQuery": "commonQuery",
            "propertiesName": "abnormalInfor",
            "corp_org": self.org,
            "corp_id": self.jsid,
            "corp_seq_id": self.seqid,
            "pageNo": "1",
            "pageSize": "500",
        }
        abnormalInfo = self.post_json(link=link, data=data)

        for every in abnormalInfo["items"]:
            self.data["abnormalList"].append(
                {
                    "inTime": every["C2"],  # 列入日期
                    "institute": every["C5"],  # 做出决定机关
                    "inReason": every["C1"],  # 列入原因
                    "outTime": every["C4"],  # 移出时间
                    "outReason": every["C3"],  # 移出原因
                }
            )
        return self.data["abnormalList"]

    def get_check_info(self):
        if self.mark["check"]:
            return self.data["checkList"]
        else:
            self.mark["check"] = 1
        self.data["checkList"] = []
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/commonServlet.json?commonEnter=true"
        data = {
            "showRecordLine": "1",
            "specificQuery": "commonQuery",
            "propertiesName": "checkup",
            "corp_org": self.org,
            "corp_id": self.jsid,
            "pageNo": "1",
            "pageSize": "500",
        }
        checkInfo = self.post_json(link=link, data=data)

        for every in checkInfo["items"]:
            self.data["checkList"].append(
                {
                    "institute": every["C1"],  # 检查实施机关
                    "type": every["C2"],  # 类型
                    "time": every["C3"],  # 检查时间
                    "result": every["C4"],  # 检查结果
                }
            )
        return self.data["checkList"]

    def get_report_info(self):
        # 检测是否已经获取过一次
        if self.mark["report"]:
            return self.data["annuRepYearList"]
        else:
            self.mark["report"] = 1
        # 年报信息初始化
        self.data["annuRepYearList"] = []
        # 获取年报信息列表
        if self.mark["basic"]:
            pass
        else:
            self.get_basic_info()
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/nbServlet.json?nbEnter=true"
        if self.data["baseInfo"]["creditCode"]:
            regno = self.data["baseInfo"]["creditCode"]
        else:
            regno = self.data["baseInfo"]["regNumber"]
        data = {
            "REG_NO": regno,
            "showRecordLine": "0",
            "specificQuery": "gs_pb",
            "propertiesName": "query_report_list",
        }
        yearList = self.post_json(link, data)
        # 处理每一年的年报信息
        for everyyear in yearList:
            # 初始化信息
            # self.data["annuRepYearList"].append(
            thisyearInfo = {
                    "baseinfo": {   # 基本信息
                        "name": "",             # 公司名称
                        "reportYear": "",       # 报告年度
                        "creditCode": "",       # 统一社会信用代码
                        "regNumber": "",        # 工商注册号
                        "regStatus": "",        # 状态

                        "connectLocation": "",  # 联系地址
                        "phoneNumber": "",      # 电话号码
                        "email": "",            # 电子邮件
                        "zipCode": "",       # 邮政编码

                        "if_website": "",            # 是否有网站网店
                        "if_invest": "",# 是否有投资信息或者购买其他公司股权
                        "if_equity": "",        # 是否发生股东股权转让
                    },
                    "stock": [],                # 股东发起人及出资信息
                    "website": [],              # 网站网店信息
                    "security": [],             # 担保信息
                    "change": [],             # 修改记录
                    "assets": {
                        "netAmount": "",        # 资产总额
                        "totalEquity": "",      # 所有者权益合计
                        "saleIncome": "",       # 营业总收入
                        "profitTotal": "",      # 利润总额
                        "mainIncome": "",       # 主营业务收入
                        "profitReta": "",       # 净利润
                        "taxTotal": "",        # 纳税总额
                        "debtAmount": "",       # 负债总额
                    },
                }


            # 年报中的企业基本信息和企业资产状况信息
            ID = everyyear["ID"]
            data = {
                "ID": ID,
                "OPERATE_TYPE": "2",
                "showRecordLine": "0",
                "specificQuery": "gs_pb",
                "propertiesName": "query_basicInfo"
            }
            thisyearbasicInfo = self.post_json(link, data)
            for x in thisyearbasicInfo:
                    thisyearInfo["baseinfo"]["name"] = x["CORP_NAME"] # 公司名称
                    thisyearInfo["baseinfo"]["reportYear"] = x["REPORT_YEAR"]   # 报告年度
                    if len(x["REG_NO"]) >= 18:
                        thisyearInfo["baseinfo"]["creditCode"] = x["REG_NO"]   # 统一社会信用代码
                    else:
                        thisyearInfo["baseinfo"]["regNumber"] = x["REG_NO"]  # 工商注册号
                    thisyearInfo["baseinfo"]["regStatus"] = x["PRODUCE_STATUS"]  # 状态

                    thisyearInfo["baseinfo"]["connectLocation"] = x["ADDR"]  # 联系地址
                    thisyearInfo["baseinfo"]["phoneNumber"] = x["TEL"]  # 电话号码
                    thisyearInfo["baseinfo"]["email"] = x["E_MAIL"]  # 电子邮件
                    thisyearInfo["baseinfo"]["zipCode"] = x["ZIP"]  # 邮政编码

                    thisyearInfo["baseinfo"]["if_website"] = x["IF_WEBSITE"]  # 是否有网站网店
                    thisyearInfo["baseinfo"]["if_invest"] = x["IF_INVEST"]  # 是否有投资信息或者购买其他公司股权
                    if "IF_EQUITY" in x.values():
                        thisyearInfo["baseinfo"]["if_equity"] = x["IF_EQUITY"]  # 是否发生股东股权转让
                    thisyearInfo["assets"]["netAmount"] = x["NET_AMOUNT"]  # 资产总额
                    thisyearInfo["assets"]["totalEquity"] = x["TOTAL_EQUITY"]  # 所有者权益合计
                    thisyearInfo["assets"]["saleIncome"] = x["SALE_INCOME"]  # 营业总收入
                    thisyearInfo["assets"]["profitTotal"] = x["PROFIT_TOTAL"]  # 利润总额
                    thisyearInfo["assets"]["mainIncome"] = x["SERV_FARE_INCOME"]  # 主营业务收入
                    thisyearInfo["assets"]["profitReta"] = x["PROFIT_RETA"]  # 净利润
                    thisyearInfo["assets"]["taxTotal"] = x["TAX_TOTAL"]  # 纳税总额
                    thisyearInfo["assets"]["debtAmount"] = x["DEBT_AMOUNT"]  # 负债总额

            # 网站网店信息
            if thisyearInfo["baseinfo"]["if_website"] == u"是":
                data = {
                    "REPORT_YEAR": thisyearInfo["baseinfo"]["reportYear"],
                    "showRecordLine": "1",
                    "ID": ID,
                    "specificQuery": "gs_pb",
                    "propertiesName": "query_websiteInfo",
                    "pageNo": "1",
                    "pageSize": "500",
                }
                webInfo = self.post_json(link, data)
                for every in webInfo["items"]:
                    thisyearInfo["website"].append(
                        {
                            "webname": every["WEB_NAME"],       #网站名称
                            "webtype": every["WEB_TYPE"],       # 网站类型
                            "weburl": every["WEB_URL"]          # 网站链接
                        }
                    )

            # 股东（发起人）及出资信息
            data = {
                "MAIN_ID": ID,
                "OPERATE_TYPE": "1",
                "TYPE": "NZGS",
                "showRecordLine": "1",
                "ID": ID,
                "specificQuery": "gs_pb",
                "propertiesName": "query_stockInfo",
                "ADMIT_MAIN": "08",
                "pageNo": "1",
                "pageSize": "500",
            }
            stockInfo = self.post_json(link, data)
            # print stockInfo
            for every in stockInfo["items"]:
                thisyearInfo["stock"].append(
                    {
                        "stockname": every["STOCK_NAME"],               # 股东、发起人
                        "shouldccapi": every["SHOULD_CAPI"],            # 认缴出资额
                        "shouldcapidate": every["SHOULD_CAPI_DATE"],    # 认缴出资时间
                        "shouldcapitype": every["SHOULD_CAPI_TYPE_NAME"],# 认缴出资方式
                        "real_capi": every["REAL_CAPI"],                # 实缴出资额
                        "real_capidate": every["REAL_CAPI"],            # 实缴出资时间
                        "realcapitype": every["REAL_CAPI_TYPE_NAME"],   # 实缴出资方式
                    }
                )


            # 对外提供保证担保信息
            data = {
                "REPORT_YEAR": thisyearInfo["baseinfo"]["reportYear"],
                "showRecordLine": "1",
                "ID": ID,
                "specificQuery": "gs_pb",
                "propertiesName": "query_InformationSecurity",
                "pageNo": "1",
                "pageSize": "500",
            }
            securityInfo = self.post_json(link, data)
            for every in securityInfo["items"]:
                thisyearInfo["security"].append(
                    {
                        "credName": every["CRED_NAME"],         # 债权人
                        "debtName": every["DEBT_NAME"],         # 债务人
                        "credType": every["CRED_TYPE"],         # 主债权种类
                        "credAmount": every["CRED_AMOUNT"],     # 主债权数额
                        "guarDate": every["GUAR_DATE"],         # 履行债务的期限
                        "guarPeriod": every["GUAR_PERIOD"],     # 保证的期间
                        "guarType": every["GUAR_TYPE"],         # 保证的方式
                    }
                )


            # 修改记录
            if thisyearInfo["baseinfo"]["creditCode"]:
                regno = thisyearInfo["baseinfo"]["creditCode"]
            else:
                regno = thisyearInfo["baseinfo"]["regNumber"]
            data = {
                "REPORT_YEAR": thisyearInfo["baseinfo"]["reportYear"],
                "REG_NO": regno,
                "showRecordLine": "1",
                "specificQuery": "gs_pb",
                "propertiesName": "query_RevisionRecord",
                "pageNo": "1",
                "pageSize": "500",
            }
            changeInfo = self.post_json(link, data)
            for every in changeInfo["items"]:
                thisyearInfo["change"].append(
                    {
                        "changename": every["CHANGE_ITEM_NAME"],        # 修改事项
                        "new": every["NEW_CONTENT"],            # 修改后
                        "old": every["OLD_CONTENT"],    # 修改前
                        "time": every["CHANGE_DATE"],# 修改日期
                    }
                )


            # 年报信息提交
            self.data["annuRepYearList"].append(thisyearInfo)

    # 投资人及出资信息
    def get_touzichuzi_info(self):
        if self.mark["touzichuzi"]:
            return self.data["touzichuziInfo"]
        else:
            self.mark["touzichuzi"] = 1
        # 投资出资信息初始化
        self.data["touzichuziInfo"] = []
        if self.mark["basic"]:
            pass
        else:
            self.get_basic_info()
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/nbServlet.json?nbEnter=true"
        if self.data["baseInfo"]["creditCode"]:
            regno = self.data["baseInfo"]["creditCode"]
        else:
            regno = self.data["baseInfo"]["regNumber"]
        data = {
            "REG_NO": regno,
            "showRecordLine": "1",
            "specificQuery": "gs_pb",
            "propertiesName": "query_tzcz",
            "ADMIT_MAIN": "08",
            "pageNo": "1",
            "pageSize": "500",
        }
        touzichuziInfo = self.post_json(link, data)
        for every in touzichuziInfo["items"]:
            re_touzi = re.compile("<tr><td.*?>(.*?)<\/td><td.*?>"
                                   "(.*?)<\/td><td.*?>(.*?)<\/td>"
                                   "<td.*?>(.*?)<\/td><td.*?>(.*?)<\/td>"
                                   "<td.*?>(.*?)<\/td><td.*?>(.*?)"
                                   "<\/td><td.*?>(.*?)<\/td><td.*?>"
                                   "(.*?)<\/td><td.*?>(.*?)<\/td")
            touzi = re_touzi.findall(every["D1"])
            if touzi:
                touzi = touzi[0]
            else:
                continue
            self.data["touzichuziInfo"].append(
                {
                    "name": touzi[0],  # 投资人
                    "type": touzi[1],  # 投资人类型
                    "leijirenjiao": touzi[2],  # 累计认缴额
                    "leijishijiao": touzi[3],  # 累计实缴额
                    "renjiaochuzi": touzi[4],  # 认缴出资额
                    "chuzifangshi": touzi[5],  # 出资方式
                    "chuzishijian": touzi[6],  # 出资时间
                    "shijiaochuzi": touzi[7],  # 实缴出资
                    "shijiaochuzifangshi": touzi[8],# 实缴出资方式
                    "shijiaochuzishijian": touzi[9],# 实缴出资时间
                }
            )
        return self.data["touzichuziInfo"]

    # 行政许可信息
    def get_xingzhengxuke_info(self):
        if self.mark["xingzhengxuke"]:
            return self.data["xingzhengxukeInfo"]
        else:
            self.mark["xingzhengxuke"] = 1
        # 投资出资信息初始化
        self.data["xingzhengxukeInfo"] = []
        if self.mark["basic"]:
            pass
        else:
            self.get_basic_info()
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/nbServlet.json?nbEnter=true"
        if self.data["baseInfo"]["creditCode"]:
            regno = self.data["baseInfo"]["creditCode"]
        else:
            regno = self.data["baseInfo"]["regNumber"]
        data = {
            "REG_NO": regno,
            "showRecordLine": "1",
            "specificQuery": "gs_pb",
            "propertiesName": "query_xzxk",
            "pageNo": "1",
            "pageSize": "500",
        }
        xingzhengxukeInfo = self.post_json(link, data)
        for every in xingzhengxukeInfo["items"]:
            self.data["xingzhengxukeInfo"].append(
                {
                    "num": every["A2"],     # 许可文件编号
                    "name": every["A3"],    # 许可文件名称
                    "fromTime": every["A4"],# 有效期自
                    "toTime": every["A5"],  # 有效期至
                    "institute": every["A6"],# 许可机关
                    "content": every["A7"], # 许可内容
                }
            )
        return self.data["xingzhengxukeInfo"]

    # 知识产权出质信息
    def get_zhishichuzhi_info(self):
        if self.mark["zhishichuzhi"]:
            return self.data["zhishichuzhiInfo"]
        else:
            self.mark["zhishichuzhi"] = 1
        # 投资出资信息初始化
        self.data["zhishichuzhiInfo"] = []
        if self.mark["basic"]:
            pass
        else:
            self.get_basic_info()
        link = "http://www.jsgsj.gov.cn:58888/ecipplatform/nbServlet.json?nbEnter=true"
        if self.data["baseInfo"]["creditCode"]:
            regno = self.data["baseInfo"]["creditCode"]
        else:
            regno = self.data["baseInfo"]["regNumber"]
        data = {
            "REG_NO": regno,
            "showRecordLine": "1",
            "specificQuery": "gs_pb",
            "propertiesName": "query_zscq",
            "pageNo": "1",
            "pageSize": "500",
        }
        zhishichuzhiInfo = self.post_json(link, data)
        for every in zhishichuzhiInfo["items"]:
            self.data["zhishichuzhiInfo"].append(
                {
                    "num": every["C2"],     # 出质商标注册号
                    "name": every["C3"],    # 商标名称
                    "type": every["C4"],    # 类别
                    "chuzhiren": every["C5"],# 出质人
                    "zhiquanren": every["C6"],# 质权人
                    "zhiquanqixian": every["C7"],# 质权登记期限
                    "biangeng": every["C8"],    # 变更情况
                }
            )
        return self.data["zhishichuzhiInfo"]

    # 行政处罚信息
    # def get_xingzhengchufa_info(self):
    #     if self.mark["xingzhengchufa"]:
    #         return self.data["xingzhengchufaInfo"]
    #     else:
    #         self.mark["xingzhengchufa"] = 1
    #     # 投资出资信息初始化
    #     self.data["xingzhengchufaInfo"] = []
    #     if self.mark["basic"]:
    #         pass
    #     else:
    #         self.get_basic_info()
    #     link = "http://www.jsgsj.gov.cn:58888/ecipplatform/nbServlet.json?nbEnter=true"
    #     if self.data["baseInfo"]["creditCode"]:
    #         regno = self.data["baseInfo"]["creditCode"]
    #     else:
    #         regno = self.data["baseInfo"]["regNumber"]
    #     data = {
    #         "REG_NO": regno,
    #         "showRecordLine": "1",
    #         "specificQuery": "gs_pb",
    #         "propertiesName": "query_xzcf",
    #         "pageNo": "1",
    #         "pageSize": "500",
    #     }
    #     xingzhengchufaInfo = self.post_json(link, data)
    #     for every in xingzhengchufaInfo["items"]:
    #         self.data["xingzhengchufaInfo"].append(
    #             {
    #                 "num": every["E2"],     # 行政处罚决定书文号
    #                 "content": every["E3"], # 行政处罚内容
    #                 "institute": every["E4"],   # 决定机关
    #                 "time": every["E5"],        # 做出行政处罚的日期
    #             }
    #         )
    #     return self.data["xingzhengchufaInfo"]

    def get_gongshi_info(self):
        self.get_basic_info()
        self.get_investor_info()
        self.get_comchan_info()
        self.get_staff_info()
        self.get_branch_info()
        self.get_mortgage_info()
        self.get_chuzhi_info()
        self.get_punish_info()
        self.get_abnormal_info()
        self.get_check_info()
        self.get_report_info()
        self.get_touzichuzi_info()
        self.get_xingzhengxuke_info()
        # # self.get_xingzhengchufa_info()
        self.get_zhishichuzhi_info()
        return self.data

if __name__ == '__main__':
    name = u"名人斯诺克沙龙桌球房"
    # name = u"丹徒县大众公关礼仪事务所"
    # name = u"丹徒县化轻公司"
    name = u"泗洪县永翔水产养殖厂"
    name = u"江苏银行股份有限公司"
    # name = u"南京银行股份有限公司"
    # name = u"华尔润玻璃产业股份有限公司"
    # name = u"中新苏州工业园区创业投资有限公司"
    # name = u"徐州建达金属工具制造有限公司"
    name = u"兴化市兴发商品混凝土有限公司"

    # 投资出资信息、行政许可、行政处罚信息、知识产权出质
    name = u"常州凯本冷暖设备工程有限公司"
    name = u'josdifjoijsdf'

    a = JiangSuAnalyze(name=name)
    print '-'*40
    print '-'*40
    print a.name
    print a.jsid
    print a.org
    print a.seqid
    print ''
    print '--------------------公司基本信息-------------------'
    a.get_gongshi_info()
    print "公司名称", "\t",a.data["baseInfo"]["name"]
    print "公司类型", "\t", a.data["baseInfo"]["companyOrgType"]
    print "法人", "\t", a.data["baseInfo"]["legalPersonName"]
    print "社会信用代码", "\t", a.data["baseInfo"]["creditCode"]
    print "注册号", "\t", a.data["baseInfo"]["regNumber"]
    print "状态", "\t", a.data["baseInfo"]["regStatus"]
    print "注册资本", "\t", a.data["baseInfo"]["regCapital"]
    print "登记机关", "\t", a.data["baseInfo"]["regInstitute"]
    print "注册地址", "\t", a.data["baseInfo"]["regLocation"]
    print "行业", "\t", a.data["baseInfo"]["industry"]
    print "电话号码", "\t", a.data["baseInfo"]["phoneNumber"]
    print "电子邮件", "\t", a.data["baseInfo"]["email"]
    print "核准日期", "\t", a.data["baseInfo"]["approvedTime"]
    print "注册时间", "\t", a.data["baseInfo"]["estiblishTime"]
    print "开始时间", "\t", a.data["baseInfo"]["fromTime"]
    print "截止时间", "\t", a.data["baseInfo"]["toTime"]
    print "经营范围", "\t", a.data["baseInfo"]["businessScope"]
    print ""
    print '---------------------投资人信息----------------------'

    for x in a.data["investorList"]:
        print "投资人", "\t", x["name"]
        print "投资人类型", "\t", x["type"]
        print "证书类型", "\t", x["papertype"]
        print "证书号码", "\t", x["papernum"]
        print ''

    print '---------------------变更信息------------------------'

    for x in a.data["comChanInfoList"]:
        print "变更事项", "\t", x["changeItem"]
        print "变更前", "\t", x["changeBefore"]
        print "变更后", "\t", x["changeAfter"]
        print "变更时间", "\t", x["changeTime"]

    print '---------------------高管信息-------------------------'

    for x in a.data["staffList"]:
        print "姓名", "\t", x["name"]
        print "职位", "\t", x["position"]

    print '---------------------分支机构--------------'
    print "分支机构："
    for x in a.data["branchList"]:
        print "\t\t", x["name"]

    print '---------------------动产抵押信息-------------------'
    for x in a.data["mortgageList"]:
        print "登记日期", "\t", x["registerTime"]
        print "编号", "\t", x["num"]
        print "登记机关", "\t", x["regInstitute"]
        print "种类", "\t", x["kind"]
        print "被担保债券数额", "\t", x["amount"]
        print "债务人履行债务的期限", "\t", x["term"]
        print "担保范围", "\t", x["scope"]
        print "状态", "\t", x["status"]

    print '---------------------股权出质--------------------'
    for x in a.data["chuzhiList"]:
        print "登记日期", "\t", x["registerTime"]
        print "编号", "\t", x["num"]
        print "出质人", "\t", x["chuzhiren"]
        print "质权人", "\t", x["zhiquanren"]
        print "状态", "\t", x["status"]
        print "出质股权数", "\t", x["chuzhiguquanshu"]
        print "出质人证件号码", "\t", x["chuzhirenzhengjianhao"]
        print "质权人证件号", "\t", x["zhiquanrenzhengjianhao"]

    print '----------------异常信息---------------------'
    for x in a.data["abnormalList"]:
        print "列入日期", "\t", x["inTime"]
        print "做出决定机关", "\t", x["institute"]
        print "列入原因", "\t", x["inReason"]
        print "移出时间", "\t", x["outTime"]
        print "移出原因", "\t", x["outReason"]

    print '--------------检查抽查信息--------------------'
    for x in a.data["checkList"]:
        print "检查实施机关", '\t', x["institute"]
        print "类型", '\t', x["type"]
        print "时间", '\t', x["time"]
        print "检查结果", '\t', x["result"]

    print '-------------------年报信息-------------------'
    for x in a.data["annuRepYearList"]:
        print "公司名称", "\t", x["baseinfo"]["name"]
        print "报告年度", "\t", x["baseinfo"]["reportYear"]
        print "统一社会信用代码", "\t", x["baseinfo"]["creditCode"]
        print "工商注册号", "\t", x["baseinfo"]["regNumber"]
        print "状态", "\t", x["baseinfo"]["regStatus"]

        print "联系地址", "\t", x["baseinfo"]["connectLocation"]
        print "电话号码", "\t", x["baseinfo"]["phoneNumber"]
        print "电子邮件", "\t", x["baseinfo"]["email"]
        print "邮政编码", "\t", x["baseinfo"]["zipCode"]

        print "是否有网站网店", "\t", x["baseinfo"]["if_website"]
        print "是否有投资信息或者购买其他公司股权", "\t", x["baseinfo"]["if_invest"]
        print "是否发生股东股权转让", "\t", x["baseinfo"]["if_equity"]
        print "资产总额", "\t", x["assets"]["netAmount"]
        print "所有者权益合计", "\t", x["assets"]["totalEquity"]
        print "营业总收入", "\t", x["assets"]["saleIncome"]
        print "利润总额", "\t", x["assets"]["profitTotal"]
        print "主营业务收入", "\t", x["assets"]["mainIncome"]
        print "净利润", "\t", x["assets"]["profitReta"]
        print "纳税总额", "\t", x["assets"]["taxTotal"]
        print "负债总额", "\t", x["assets"]["debtAmount"]

    print '------------------------投资出资信息------------------'
    for x in a.data["touzichuziInfo"]:
        print "投资人", "\t", x["name"]
        print "投资人类型", "\t", x["type"]
        print "累计认缴额", "\t", x["leijirenjiao"]
        print "累计实缴额", "\t", x["leijishijiao"]
        print "认缴出资额", "\t", x["renjiaochuzi"]
        print "出资方式", "\t", x["chuzifangshi"]
        print "出资时间", "\t", x["chuzishijian"]
        print "实缴出资", "\t", x["shijiaochuzi"]
        print "实缴出资方式", "\t", x["shijiaochuzifangshi"]
        print "实缴出资时间", "\t", x["shijiaochuzishijian"]

    print '-------------------------行政许可信息--------------'
    for x in a.data["xingzhengxukeInfo"]:
        print "许可文件编号", "\t", x["num"]
        print "许可文件名称", "\t", x["name"]
        print "有效期自", "\t", x["fromTime"]
        print "有效期至", "\t", x["toTime"]
        print "许可机关", "\t", x["institute"]
        print "许可内容", "\t", x["content"]

    print '--------------------知识产权出质信息--------------'
    for x in a.data["zhishichuzhiInfo"]:
        print "出质商标注册号", "\t", x["num"]
        print "商标名称", "\t", x["name"]
        print "类别", "\t", x["type"]
        print "出质人", "\t", x["chuzhiren"]
        print "质权人", "\t", x["zhiquanren"]
        print "质权登记期限", "\t", x["zhiquanqixian"]
        print "变更情况", "\t", x["biangeng"]

    # print '-------------------------行政处罚信息-----------'
    # for x in a.data["xingzhengchufaInfo"]:
    #     print "行政处罚决定书文号", "\t", x["num"]
    #     print "行政处罚内容", "\t", x["content"]
    #     print "决定机关", "\t", x["institute"]
    #     print "做出行政处罚的日期", "\t", x["time"]

