# coding:utf-8
import requests
import time

DbConfig = {
 # db config
 'user': 'root',
 'passwd': 'dingyu',
 'db': 'dingyu',
 'host': '192.168.0.102',
}


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
        'Referer': 'http://gsxt.cqgs.gov.cn/',
    }
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    return r.text


def dict_jyyc_url_list(dic):
    jyyc_url_list = []
    for x in dic["jyyclist"]:
        d = {}
        d["_url"] = "http://gsxt.cqgs.gov.cn/search_getEnt.action?_c1469155905658=_c205102&entId=" + x["_pripid"] + "&id=" + x["_regCode"] + "&stype=SAIC&type=1"
        d["_name"] = x["_name"]
        d["_numb"] = x["_regCode"]

        jyyc_url_list.append(d)
    return jyyc_url_list

if __name__ == '__main__':
    # try:
    #     conn = MySQLdb.connect(user=DbConfig['user'],
    #                            passwd=DbConfig['passwd'],
    #                            db=DbConfig['db'],
    #                            host=DbConfig['host'],
    #                            charset='utf8',
    #                            use_unicode=True
    #                            )
    #     cursor = conn.cursor()
        for page in range(1, 2):
            url = "http://gsxt.cqgs.gov.cn/search_searchjyyc.action?currentpage=%s&itemsperpage=10" % page
            url = "http://gsxt.cqgs.gov.cn/search_getEnt.action?_c1469155905658=_c205102&entId=500222010100000669&id=500103000073365&stype=SAIC&type=1"

            # print url
            text = get_html(url)
            print text[6:]
            # print text
            # [测试返回数量]
            # name_dict = dict(eval(text))
            # print len(name_dict["jyyclist"])
            # [企业名称列表解析为每个企业详细连接]
            # name_dict = dict(eval(text))
            # jyyc_url_list = dict_jyyc_url_list(name_dict)
            # for x in jyyc_url_list:
            #     print x[""]
                # print get_html(x)
                # try:
                #     print "charu1"
                #     self.cursor.execute(
                #         """INSERT IGNORE INTO t_hnxy (t_hnxy_name, t_hnxy_url, t_hnxy_numb)
                #         VALUES (%s, %s, %s)""",
                #         (
                #             item['name'],
                #             item['url'],
                #             item['numb']
                #         )
                #     )
                #     conn.commit()
                # except MySQLdb.Error, e:
                #     print 'Error %d %s' % (e.args[0], e.args[1])






            # except MySQLdb.Error, e:
            #     print 'Error %d %s' % (e.args[0], e.args[1])


            # print text
            # tree = etree.HTML(text)
            # info_url = tree.xpath("//h3/a/@href")
            # print info_url
            # if info_url: info_url = info_url[0]
            # print info_url