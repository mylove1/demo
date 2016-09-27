# coding:utf-8

DB_FILE = r'.\data\proxy.db'

# 监听的ip和端口
LISTENING_IP = "192.168.0.50"
LISTENING_PORT = 8384


TEST_URL = "http://static.gcimg.net/i/201604/2Pg1E4D61w.png"
CHECK_LENTH = 3183

# TEST_URL = "http://www.baidu.com/img/bd_logo1.png"
# CHECK_LENTH = 7877


# 这个列表里每一项是一个可以采集ip的网站的配置
resources = [
    {
        "name": "快代理",
        "urllist": ["http://www.kuaidaili.com/proxylist/%s/" % x for x in range(1, 11)],
        "rule": '<tr><tddata-title="IP">(.*?)</td><tddata-title="PORT">(.*?)</td>',
        "frequency": 600,
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }
    },
    {
        "name": "代理ip检测平台818",
        "urllist": ['http://www.ip181.com/'],
        "rule": '<tr.*?><td>(.*?)</td><td>(.*?)</td><td>.*?</td>',
        "frequency": 100,
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }
    },
    {
        "name": "开心代理",
        "urllist": ["http://www.kxdaili.com/dailiip/%s/%s.html#ip" % (x, y) for x in range(1, 5) for y in range(1, 11)],
        "rule": '<tr.*?><td>(.*?)</td><td>(.*?)</td>',
        "frequency": 600,
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }
    },
    {
        "name": "酷伯伯",
        "urllist": ["http://www.coobobo.com/free-http-proxy/%s" % x for x in range(1, 11)],
        "rule": '<tr><td>(.*?)</td><td>(.*?)</td>',
        "frequency": 600,
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }
    },
    {
        "name": "西刺代理",
        "urllist": ["http://www.xicidaili.com/%s/1" % x for x in ['nn', 'nt', 'wn', 'wt', 'qq']],
        "rule": '<trclass=.*?<tdclass="country".*?</td><td>(.*?)</td><td>(.*?)</td>',
        "frequency": 600,
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }
    },
    {
        "name": "66IP",
        "urllist": ["http://www.66ip.cn/nmtq.php?getnum=800&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=0&proxytype=2&api=66ip"],
        "rule": '>(.*?):(.*?)<',
        "frequency": 60,
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }
    },
    {
        "name": "秘密代理IP",
        "urllist": ["http://www.mimiip.com/%s/" % x for x in ["gngao", "gnpu", "gntou", "hw"]],
        "rule": '<tr><td>(.*?)</td><td>(.*?)</td>',
        "frequency": 60,
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }
    },
    {
        "name": "云代理",
        "urllist": ["http://www.ip3366.net/free/?stype=%s&page=%s" % (x, y) for x in range(1, 5) for y in range(1, 5)],
        "rule": '<tr><td>(.*?)</td><td>(.*?)</td>',
        "frequency": 600,
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }
    },
    {
        "name": "瑶瑶代理",
        "urllist": ["http://www.httpsdaili.com/index.asp?stype=%s" % x for x in range(1, 5)],
        "rule": '<trclass="odd"><tdclass="style1">(.*?)</td><tdclass="style2">(.*?)</td>',
        "frequency": 600,
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        }
    },
]