# coding=utf-8
import requests
import re
import MySQLdb
index = 11
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
    'Referer': 'http://wenshu.court.gov.cn/List/ListContent',
    'Connection': 'keep-alive',
}
DbConfig = {
 # db config
 'user': 'root',
 'passwd': 'dingyu',
 'db': 'dingyu',
 'host': '192.168.0.102',
}
if __name__ == '__main__':
    conn = MySQLdb.connect(user=DbConfig['user'],
                           passwd=DbConfig['passwd'],
                           db=DbConfig['db'],
                           host=DbConfig['host'],
                           charset='utf8',
                           use_unicode=True
                           )
    cursor = conn.cursor()

    url = 'http://wenshu.court.gov.cn/List/ListContent'
    data = {
        'Param': '',
        'Index': '1',
        'Page': '20',
        'Order': '裁判日期',
        'Direction': 'asc',
    }
    for ind in xrange(10, index):
        data['Index'] = str(ind)
        # try:
        r = requests.post(url, data=data)
        text = r.text[2:-3]
        dell = [
            'titleu0026amp;',
            '\\',
            '/',
            '&amp;#xA;',
            'title&amp;',
            'gt;',
            'u0026amp;',
            '#xA;',
            'lt;',
            '&amp;lt;',
            '&amp;',
            'p&amp;',
            'pp',
            'amp;',
            'nbsp;',
            'times;'
        ]
        for dell_l in dell:
            text = text.replace(dell_l, '')
        # print text
        l = text.split('},{')
        # l[0] = l[0][1:]
        for x in l[1:]:
            x = "{" + x + "}"
            print x
            # 尝试转换为字典
            d = dict(eval(x))

            for key in d.keys():
                print key + '\t:\t' + d[key]
            # r_yuangao = re.compile('原告(.*?)，')
            # # r_beigao = ''
            # l_yuangao = r_yuangao.findall(d['DocContent'])
            # for yuangao in l_yuangao:
            #     print yuangao
            # print "文书ID"+ '\t:\t' +d["文书ID"]
            # if not d["裁判要旨段原文"]:
            #     print "裁判要旨段原文"+ '\t:\t' +d["裁判要旨段原文"]
            # print "审判程序"+ '\t:\t' +d["审判程序"]
            # print "案号"+ '\t:\t' +d["案号"]
            # print "裁判日期"+ '\t:\t' +d["裁判日期"]
            # print "案件类型"+ '\t:\t' +d["案件类型"]
            # print "法院名称"+ '\t:\t' +d["法院名称"]
            # print "案件名称"+ '\t:\t' +d["案件名称"]
            # print "DocContent"+ '\t:\t' +d["DocContent"]

        print '-----------------'
        # except:
        #     print 'xxxxxxxxxxxxxxxx'
        #     continue
    cursor.close()
    conn.close()

