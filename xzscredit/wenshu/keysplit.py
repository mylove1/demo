# coding:utf-8

import requests

# url = 'http://wenshu.court.gov.cn/List/TreeContent'
# r = requests.post(url, data={"Param": ""})
# text = r.text[1:-1]
# text = text.replace('\\', '')
# l = list(eval(text))
# total_leimu = 0
# for leimu in l:
#
#     print leimu["Key"], leimu["Value"]
#     total_leimu += int(leimu["Value"])
#     total_chi = 0
#     for chi in leimu["Child"]:
#         if chi["Key"] == '':
#             continue
#         print chi["Key"], chi["Value"]
#         total_chi += int(chi["Value"])
#     print 'total count \t',total_chi
#     print '-----------------'
# print 'total count \t', total_leimu
# print '--------------------------------'



def url_list(url, data):
    req = requests.post(url=url, data=data)
    html = req.text[1:-1].replace('\\', '')
    print "Has dowit"
    return list(eval(html))


def select_list(url, data, hist):
    biaozhi = False
    global link
    print link
    l = url_list(url, data)
    # 创建L={
    #        "法院层级":{"最高法院":658464,"高级法院":684851},
    #        "地域":{"北京":6548,}
    #       }
    L = {}
    for x in l:
        if x["Key"] == '' or x["Key"] in hist: continue
        L[x["Key"]] = {}
        for y in x["Child"]:
            if y["Key"] == '':continue
            L[x["Key"]][y["Key"]] = int(y["Value"])

    LL = {}
    for x in l:
        if x["Key"] == '': continue
        LL[x["Key"]] = {}
        for y in x["Child"]:
            if y["Key"] == '': continue
            LL[x["Key"]][y["Key"]] = int(y["Value"])

    # 判断每个父类目是否小于500，如果有一个是 就返回结果，如果没有就选择最合适的然后就迭代。进入下一层

    for leimu in L.keys():
        # print '111111111'
        # print L[leimu].values()
        if len(L[leimu].values()) == 0:
            for guanjianci in LL["关键词"].keys():
                print '-----------1-------------'
                # print guanjianci
                this_data= {}
                this_data["Param"] = ',' + data["Param"] + leimu + ':' + guanjianci
                # print this_data["Param"]
                link.append([this_data, 9999999999])
                biaozhi = True
                # print link
            break

        if max(L[leimu].values()) <= 500:
            print '---------2-------------'
            for guanjianci in L[leimu].keys():
                if data["Param"] == '':
                    this_data= {}
                    this_data["Param"] = data["Param"] + leimu + ':' + guanjianci
                    # print this_data["Param"]
                    link.append([this_data, L[leimu][guanjianci]])
                else:
                    this_data= {}
                    this_data["Param"] = ',' + data["Param"] + leimu + ':' + guanjianci
                    # print this_data["Param"]
                    link.append([this_data, L[leimu][guanjianci]])
            biaozhi = True
            # print link
            break
    if not biaozhi:
        print '-----------3----------'
        count_list = {}
        for x in l:
            if x["Key"] in hist: continue
            count_list[int(x["Value"])] = x["Key"]
        # print '-'.join(count_list.values())
        diedaiquyu = count_list[max(count_list.keys())]

        for die in L[diedaiquyu].keys():
            this_hist = hist
            this_hist.append(diedaiquyu)
            this_data = {}
            if data["Param"] == '':
                this_data["Param"] = data["Param"] + diedaiquyu + ':' + die
            else:
                this_data["Param"] = ',' + data["Param"] + diedaiquyu + ':' + die
            print 'zuihoul-----------------------zuihou'
            select_list(url, this_data, this_hist)
            # print 'wanl'


if __name__ == "__main__":
    link = []
    url = 'http://wenshu.court.gov.cn/List/TreeContent'
    data={"Param": ""}
    hist = ["关键词"]
    select_list(url, data=data, hist=hist)
    print 'link:\t\t', link

