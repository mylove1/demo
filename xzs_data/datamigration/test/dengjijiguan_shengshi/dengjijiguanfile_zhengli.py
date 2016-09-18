# coding:utf-8
import re
import pymongo
MASTERIP = '192.168.0.50'
conn = pymongo.Connection(MASTERIP, 27017)
db = conn.xingzheng



if __name__ == '__main__':
    rea = re.compile('(^.*?)市.*?')
    re_sheng_shi = re.compile('(.*?省)(.*?市).*?')
    re_sheng_xian = re.compile('(.*?省)(.*?县).*?')
    re_shi_shi = re.compile('(.*?市)(.*?市).*?')
    re_shi_xian = re.compile('(.*?市)(.*?县).*?')
    re_shi_qu = re.compile('(.*?市)(.*?区).*?')
    re_shi_ = re.compile(('(.*?市)(.*?)$'))
    re_shi = re.compile(('(.*?市)$'))
    re_sheng = re.compile(('(.*?省)$'))
    re_sheng_ = re.compile(('(.*?省)(.*?)$'))
    with open("dengjijiguan3.txt", 'r') as f:
        # with open("dengjijiguan4.txt", 'w') as f2:
            for enu, x in enumerate(f.readlines()):
                x = x.strip()
                x = x.split('工商行政管理')[0]
                x = x.split('市场监督管理局')[0]
                x = x.split('市场和质量')[0]
                x = x.split('工商和质量监督管理局')[0]
                x = x.split('经济技术开发区')[0]
                x = x.split('经济开发区')[0]
                x = x.split('市场监督管理所')[0]
                x = x.split('工商质监局')[0]
                x = x.split('工商局')[0]
                x = x.split('工商所')[0]
                x = x.split('分局')[0]
                x = x.split('工商管理和质量技术监督局')[0]
                x = x.split('高新技术开发区')[0]
                x = x.split('市场监管局')[0]
                x = x.split('工商行政管理总局')[0]
                x = x.split('工业园区')[0]
                x = x.split('保税区')[0]
                sheng_shi = re_sheng_shi.findall(x)
                if sheng_shi:
                    # print sheng_shi[0][0], '   ', sheng_shi[0][1]
                    continue
                sheng_xian = re_sheng_xian.findall(x)
                if sheng_xian:
                    # print sheng_xian[0][0], '   ', sheng_xian[0][1]
                    continue
                _sheng = re_sheng.findall(x)
                if _sheng:
                    # shengcode = db.sheng.find({"shengname": _sheng[0]})[0]["shengcode"]
                    # shenghui = db.shi.find({"shicode": (shengcode + '0100000000')})[0]["shiname"]
                    # print _sheng[0], '   ', shenghui
                    continue
                _sheng_ = re_sheng_.findall(x)
                if _sheng_:
                    # print x
                    # re_this = re.compile(".*?" +_sheng_[0][1] + ".*?")
                    # shiname = db.shi.find({"shiname": re_this})#[0]#["shiname"]
                    # if shiname.count() != 0:
                    #     print _sheng_[0][0], '   ', shiname[0]["shiname"]
                    # else:
                    #     shiname = db.xian.find({"xianname": re_this})#[0]#["shiname"]
                    #     print _sheng_[0][0], '   ', shiname[0]["shiname"]
                    continue
                shi_shi = re_shi_shi.findall(x)
                if shi_shi:
                    # # print shi_shi[0][0], shi_shi[0][1]
                    # shengname = db.shi.find({"shiname": shi_shi[0][0]})
                    # if shengname.count() != 0:
                    #     shengname = db.shi.find({"shiname": shi_shi[0][0]})[0]["shengname"]
                    #     print shengname, '   ', shi_shi[0][0]
                    # else:
                    #     try:
                    #         shengname = db.xian.find({"xianname": shi_shi[0][1]})[0]["shengname"]
                    #         print shengname, '   ', shi_shi[0][0]
                    #     except:
                    #         shengname = shi_shi[0][0]
                    #         print shengname, '   ', shi_shi[0][0]
                    continue
                shi_xian = re_shi_xian.findall(x)
                if shi_xian:
                    # # print shi_xian[0][0], shi_xian[0][1]
                    # shengname = db.shi.find({"shiname": shi_xian[0][0]})
                    # if shengname.count() != 0:
                    #     shengname = db.shi.find({"shiname": shi_xian[0][0]})[0]["shengname"]
                    #     print shengname, '   ', shi_xian[0][0]
                    # else:
                    #     try:
                    #         shengname = db.xian.find({"xianname": shi_xian[0][1]})[0]["shengname"]
                    #         print shengname, '   ', shi_xian[0][0]
                    #     except:
                    #         shengname = shi_xian[0][0]
                    #         print shengname, '   ', shi_xian[0][0]
                    continue
                shi_qu = re_shi_qu.findall(x)
                if shi_qu:
                    # print shi_qu[0][0], shi_qu[0][1]
                    # shengname = db.shi.find({"shiname": shi_qu[0][0]})
                    # # print shengname.count()
                    # if shengname.count() != 0:
                    #     shengname = db.shi.find({"shiname": shi_qu[0][0]})[0]["shengname"]
                    #     print shengname, '   ', shi_qu[0][0]
                    # else:
                    #     try:
                    #         shengname = db.xian.find({"xianname": shi_qu[0][1]})[0]["shengname"]
                    #         print shengname, '   ', shi_qu[0][0]
                    #     except:
                    #         shengname = shi_qu[0][0]
                    #         print shengname, '   ', shi_qu[0][0]
                    continue

                if sheng_xian:
                    # print sheng_xian[0][0], '   ', sheng_xian[0][1]
                    continue

                # _shi = re_shi.findall(x)
                # if _shi:
                #     # print _shi[0]
                #     shengname = db.shi.find({"shiname": _shi[0]})
                #     # print shengname.count()
                #     if shengname.count() != 0:
                #         shengname = shengname[0]["shengname"]
                #         # print shengname, '   ', _shi[0]
                #     else :
                #         shengname = db.xian.find({"xianname": _shi[0]})
                #         if shengname.count() != 0:
                #             # print shengname[0]["shengname"], '   ', _shi[0]
                #             pass
                #         else:
                #             shengname = db.sheng.find({"shengname": _shi[0]})
                #             print _shi[0]
                #     # shengcode = db.sheng.find({"shengname": _sheng[0]})[0]["shengcode"]
                #     # shenghui = db.shi.find({"shicode": (shengcode + '0100000000')})[0]["shiname"]
                #     # print _sheng[0], '   ', shenghui
                #     continue
                # _shi_ = re_sheng_.findall(x)
                # if _shi_:
                #     # print x
                #     # re_this = re.compile(".*?" +_sheng_[0][1] + ".*?")
                #     # shiname = db.shi.find({"shiname": re_this})#[0]#["shiname"]
                #     # if shiname.count() != 0:
                #     #     print _sheng_[0][0], '   ', shiname[0]["shiname"]
                #     # else:
                #     #     shiname = db.xian.find({"xianname": re_this})#[0]#["shiname"]
                #     #     print _sheng_[0][0], '   ', shiname[0]["shiname"]
                #     continue

                # if "省" in x:
                #     print x, '--------'
                # print x






                # f2.write(x)
                # f2.write('\n')
                # print x
                # sheng = rea.findall(x)
                # if sheng:
                #     print sheng[0]
                # print '\n', '------------------------'
                # # db.dengjijiguan.insert({"name": x.strip(), "sheng": "不知道", "shi": "也不知道"})
                if enu >= 1000:break

