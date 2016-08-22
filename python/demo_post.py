# coding:utf-8
import requests
import threading
import re
import pymongo

conn = pymongo.Connection("192.168.100.55", 27017)
db = conn.zhejiang

headers = {
    "Host": "gsxt.zjaic.gov.cn",
    "Referer": "http://gsxt.zjaic.gov.cn/unusualcatalog/doReadUnusualCatalogList.do",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

url = "http://gsxt.zjaic.gov.cn/unusualcatalog/doReadUnusualCatalogListJSON.do?_id=doReadCatalogList1471058567706"
data = {
    "qryParam": "",
    "pagination.currentPage": "1",
    "pagination.pageSize": "10",
}
r = requests.post(url, data, headers=headers)
print r.text
text = r.text
li = re.findall('''{"catRegNo":"(.*?)","corpid":"(.*?)","catRemark":".*?","catNo":"(.*?)","canOutReaCodeName":".*?","catState":".*?","catEntName":"(.*?)","catOrgName''', text)
for x in li:
    pagedict = {}
    pagedict["catRegNo"] = x[0]
    pagedict["corpid"] = x[1]
    pagedict["catNo"] = x[2]
    pagedict["catEntName"] = x[3]
    db.yichanglist.insert(pagedict)


class YichangCrawl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.agent = config.agents
        self.url = 'http://whois.chinaz.com/reverse'
        self.proxypool = proxypool

    def get_html(self, key, url, page=1):
        data = {
            'host': key,
               }
        if page == 1:
            data["ddlSearchMode"] = '2',
        else:
            data["type"] = '2'
            data["page"] = page

        while 1:
            this_headers = {
                'User-Agent': random.choice(self.agent),
                'Referer': 'http://whois.chinaz.com',
                'Connection': 'keep-alive',
            }
            # [use proxy]
            try:
                proxy = random.choice(self.proxypool)
                r = requests.post(url, headers=this_headers, data=data, proxies={'http': proxy}, timeout=5)
                break
            except:
                    print '.'
        return r.text

    def get_list(self, key, page):
        url = 'http://whois.chinaz.com/pagehtml.ashx'
        page = page
        html = self.get_html(key, url=url, page=page).encode('utf8')
        reweburl = re.compile('<a href=.*?blank">(.*?)</a></div><div class="w280"><a.*?_blank">(.*?)</a></div><div class="w280"><a href=.*?>(.*?)</a></div><div class="w100">(.*?)</div><div class="w100">(.*?)</div><div class="w70">')
        datas = reweburl.findall(html)
        return datas

    def put_mess(self, mess):
        requests.post('http://192.168.100.55:12222/post', data=mess)



    def get_kw(self):
        r = requests.get('http://192.168.100.55:12222/comp')
        return r.text


    def run(self):
        while True:
            key = self.get_kw().encode('utf8')
            # key = '华为技术有限公司'
            print key
            if key == '':
                time.sleep(10)
                continue
            while 1:
                html = self.get_html(key, url=self.url).encode('utf8')
                if '>查询过于频繁。' in html:
                    print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
                    continue
                else:
                    break
            if '>暂无相关数据' in html:
                print key, '\t\t\tnot'
                continue
            else:
                datas = re.findall(
                    '<a href=.*?blank">(.*?)</a></div><div class="w280">(.*?)</div><div class="w280"><a href=.*?>(.*?)</a></div><div class="w100">(.*?)</div><div class="w100">(.*?)</div><div class="w70">',
                    html)
                if datas:
                    items = []
                    for x in datas:
                        item = {}
                        item["url"] = x[0]
                        item["name"] = x[1]
                        item["email"] = x[2]
                        item["starttime"] = x[3]
                        item["endtime"] = x[4]
                        items.append(item)
                    # print str(items)
                    print '---------', key, '--------------->>>>>>>>>>>>>>>'
                    self.put_mess({"comp": str(items)})
                    try:
                        pages = re.findall('共(.*?)页，到第', html)[0]
                        pages = int(pages)
                        if pages > 1:
                            for page in range(2, pages + 1):
                                print '---', key, '---', page
                                datas = self.get_list(key, page)
                                if datas:
                                    items = []
                                    for x in datas:
                                        item = {}
                                        item["url"] = x[0]
                                        item["name"] = x[1]
                                        item["email"] = x[2]
                                        item["starttime"] = x[3]
                                        item["endtime"] = x[4]
                                        items.append(item)
                                    # print str(items)
                                    print '---------', key, '---', page, '------------>>>>>>>>>>>>>>>'
                                    self.put_mess({"comp": str(items)})
                    except:
                        pass


def main():
    pagelist = [x for x in xrange(18746)]
    for x in range(5):
        pass



if __name__ == '__main__':
    main()
