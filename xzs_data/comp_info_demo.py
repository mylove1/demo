# coding:utf-8

data = {
    # 企业基本信息
    "baseInfo": {
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
    },

    # 股东信息
    "investorList": [
        {
            "amount": "",   # 投资金额
            "id": "",       # 投资人ID
            "name": "",     # 投资人
            "type": "",     # 投资人类型
            "papertype": "",    # 证书类型
            "papernum": ""  # 证书号码
        },
    ],

    # 变更信息
    "comChanInfoList": [
        {
            "changeItem": "",   # 变更事项
            "changeTime": "",   # 变更时间
            "changeAfter": "",  # 变更后
            "changeBefore": "",  # 变更前
        }
    ],

    # 高管信息
    "staffList": [
        {
            "id": "",   # id
            "name": "", # 名字
            "position": "", # 职位
        },
    ],

    # 分支机构信息
    "branchList": [
        {
            "name": "",# 分支机构名字
        }
      ],

    # "动产抵押信息"
    "mortgage": [
    {
        "registerTime": "", # 登记日期
        "num": "",  # 编号
        "regInstitute": "", # 登记机关
        "kind": "", # 种类
        "amount": "",   # 被担保债券数额
        "term": "", # 债务人履行债务的期限
        "scope": "",    # 担保范围
        "status": "",   # 状态
    }
     ],

    # 股权出质信息
    "chuzhiList": [
        {
            "registerTime": "", # 登记日期
            "num": "",  # 编号
            "chuzhiren": "", # 出质人
            "zhiquanren": "",    # 质权人
            "status": "",   # 状态
            "chuzhiguquanshu": "", # 出质股权数
            "chuzhirenzhengjianhao": "",  # 出质人证件号码
            "zhiquanrenzhengjianhao": "",    # 质权人证件号
        },
    ],

    # 异常信息
    "abnormalList": [
        {
            "inTime": "",       # 列入日期
            "institute": "",    # 做出决定机关
            "inReason": "",     # 列入原因
            "outTime": "",      # 移出时间
            "outReason": "",    # 移出原因
        }
    ],

    # 检查抽查信息
    "checkList": [
        {
            "institute": "",  # 检查实施机关
            "type": "",  # 类型
            "time": "",  # 检查时间
            "result": "",  # 检查结果
        }
    ],

    # 公司年报信息
    "annuRepYearList": [
        {
            "baseinfo": {  # 基本信息
                "name": "",  # 公司名称
                "reportYear": "",  # 报告年度
                "creditCode": "",  # 统一社会信用代码
                "regNumber": "",  # 工商注册号
                "regStatus": "",  # 状态

                "connectLocation": "",  # 联系地址
                "phoneNumber": "",  # 电话号码
                "email": "",  # 电子邮件
                "zipCode": "",  # 邮政编码

                "if_website": "",  # 是否有网站网店
                "if_invest": "",  # 是否有投资信息或者购买其他公司股权
                "if_equity": "",  # 是否发生股东股权转让
            },
            "stock": [  # 股东发起人及出资信息
                        {
                        "stockname": "",  # 股东、发起人
                        "shouldccapi": "",  # 认缴出资额
                        "shouldcapidate": "",  # 认缴出资时间
                        "shouldcapitype": "",  # 认缴出资方式
                        "real_capi": "",  # 实缴出资额
                        "real_capidate": "",  # 实缴出资时间
                        "realcapitype":"" ,  # 实缴出资方式
                        },
                ],
            "website": [  # 网站网店信息
                    {
                        "webname": "",  # 网站名称
                        "webtype": "",  # 网站类型
                        "weburl": "",  # 网站链接
                    }
                ],
            "security": [],  # 担保信息
            "change": [  # 修改记录
                        {
                        "changename": "",  # 修改事项
                        "new": "",  # 修改后
                        "old": "",  # 修改前
                        "time": "",  # 修改日期
                        },
                ],
            "assets": {
                "netAmount": "",  # 资产总额
                "totalEquity": "",  # 所有者权益合计
                "saleIncome": "",  # 营业总收入
                "profitTotal": "",  # 利润总额
                "mainIncome": "",  # 主营业务收入
                "profitReta": "",  # 净利润
                "taxTotal": "",  # 纳税总额
                "debtAmount": "",  # 负债总额
            },
        },
    ],

    # 投资出资信息
    "touzichuziInfo":[
        {
            "name": "",  # 投资人
            "type": "",  # 投资人类型
            "leijirenjiao": "",  # 累计认缴额
            "leijishijiao": "",  # 累计实缴额
            "renjiaochuzi": "",  # 认缴出资额
            "chuzifangshi": "",  # 出资方式
            "chuzishijian": "",  # 出资时间
            "shijiaochuzi": "",  # 实缴出资
            "shijiaochuzifangshi": "",  # 实缴出资方式
            "shijiaochuzishijian": "",  # 实缴出资时间
        },
    ],

    # 行政许可信息
    "xingzhengxukeInfo": [
        {
            "num": "",  # 许可文件编号
            "name": "",  # 许可文件名称
            "fromTime": "",  # 有效期自
            "toTime": "",  # 有效期至
            "institute": "",  # 许可机关
            "content": "",  # 许可内容
        }
    ],

    # 知识产权出质信息
    "zhishichuzhiInfo": [
        {
            "num": "",  # 出质商标注册号
            "name": "",  # 商标名称
            "type": "",  # 类别
            "chuzhiren": "",  # 出质人
            "zhiquanren": "",  # 质权人
            "zhiquanqixian": "",  # 质权登记期限
            "biangeng": "",  # 变更情况
        },
    ],

    # 行政处罚信息
    "xingzhengchufaInfo": [
        {
            "num": "",  # 行政处罚决定书文号
            "content": "",  # 行政处罚内容
            "institute": "",  # 决定机关
            "time": "",  # 做出行政处罚的日期
        }
    ],
}
