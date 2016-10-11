#!/usr/bin/env python
# coding:utf-8

import pymongo
import json

def jiancheng(name):
    rep_list = [

        u"哈萨克自治州",
        u"塔吉克自治县",
        u"哈萨克自治县",
        u"蒙古自治州",
        u"蒙古自治县",
        u"自治县",
        u"自治区",
        u"自治州",
        u"行政委员会",
        u"地区",
        u"壮族",
        u"回族",
        u"保安族",
        u"维吾尔",
        u"东乡族",
        u"彝族",
        u"达斡尔族",
        u"撒拉族",
        u"苗族",
        u"傈僳族",
        u"藏族",
        u"白族",
        u"朝鲜族",
        u"土家族",
        u"羌族",
        u"布依族",
        u"土族",
        u"固族",
        u"侗族",
        u"水族",
        u"哈尼族",
        u"拉祜族",
        u"佤族",
        u"普米族",
        u"傣族",
        u"哈萨克族",
        u"怒族",
        u"瑶族",
        u"独龙族",
        u"纳西族",
        u"仫佬族",
        u"景颇族",
        u"满族",
        u"毛南族",
        u"各族",
        u"布朗族",
        u"蒙古族",
        u"仡佬族",
        u"黎族",
        u"各族",
        u"的岛礁及其海域",
        u"区",
        u"地",
        u"省",
        u"市",
        u"县",
        u"盟",
        u"旗",

    ]
    nouse_list = [
        u"省直辖县级行政区划",
        u"直辖级行政划",
        u"市辖区",
        u"自治区直辖县级行政区划"
    ]
    if len(name) <= 2:
        return name
    if name in nouse_list:
        return ""
    for x in rep_list:
        name = name.replace(x, "")


    return name


if __name__ == '__main__':
    conn = pymongo.Connection(host="192.168.0.50", port=27017)
    db = conn.xingzheng

    # 仅仅打印省名以及简称
    # for x in db.sheng.find():
    #     print x["shengname"], '\t', jiancheng(x["shengname"])

    # 仅仅打印市以及简称
    # for x in db.shi.find():
    #     print x["shiname"], jiancheng(x["shiname"])
    #     print jiancheng(x["shiname"])
    totallist = {}

    for x in db.xian.find():
        sheng = x["shengname"]
        shi = x["shiname"]
        xian = x["xianname"]
        jsheng = jiancheng(sheng)
        jshi = jiancheng(shi)
        jxian = jiancheng(xian)
        db.pipei.insert({'key': sheng, 'v': {"sheng": sheng, "shi": "", "xian": ""}})
        db.pipei.insert({'key': shi, 'v': {"sheng": sheng, "shi": shi, "xian": ""}})
        db.pipei.insert({'key': xian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})
        db.pipei.insert({'key': jsheng, 'v': {"sheng": sheng, "shi": "", "xian": ""}})
        db.pipei.insert({'key': jshi, 'v': {"sheng": sheng, "shi": shi, "xian": ""}})
        db.pipei.insert({'key': jxian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})

        db.pipei.insert({'key': sheng + shi, 'v': {"sheng": sheng, "shi": shi, "xian": ""}})
        db.pipei.insert({'key': sheng + xian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})
        db.pipei.insert({'key': sheng + jshi, 'v': {"sheng": sheng, "shi": shi, "xian": ""}})
        db.pipei.insert({'key': sheng + jxian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})

        db.pipei.insert({'key': jsheng + shi, 'v': {"sheng": sheng, "shi": shi, "xian": ""}})
        db.pipei.insert({'key': jsheng + xian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})
        db.pipei.insert({'key': jsheng + jshi, 'v': {"sheng": sheng, "shi": shi, "xian": ""}})
        db.pipei.insert({'key': jsheng + jxian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})

        db.pipei.insert({'key': shi + xian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})
        db.pipei.insert({'key': shi + jxian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})

        db.pipei.insert({'key': jshi + xian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})
        db.pipei.insert({'key': jshi + jxian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})

        db.pipei.insert({'key': sheng + shi + xian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})
        db.pipei.insert({'key': jsheng + shi + xian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})
        db.pipei.insert({'key': sheng + jshi + xian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})
        db.pipei.insert({'key': sheng + shi + jxian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})
        db.pipei.insert({'key': jsheng + jshi + xian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})
        db.pipei.insert({'key': jsheng + shi + jxian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})
        db.pipei.insert({'key': sheng + jshi + jxian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})
        db.pipei.insert({'key': jsheng + jshi + jxian, 'v': {"sheng": sheng, "shi": shi, "xian": xian}})

        # print x["xianname"]
    print len(totallist)
    # with open("pipei.py", "w") as f:
    #     f.write("pipei = ")
    #     f.write(json.dumps(totallist))
