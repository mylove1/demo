# coding:utf-8
import random
import base64
from settings import PROXIES
from scrapy.exceptions import IgnoreRequest
from scrapy.contrib.downloadermiddleware import DownloaderMiddleware

# 1、process_request在请求传递给下载器前可以处理请求对象
# 2、process_response在响应传递给引擎前处理响应数据
# 3、process_exception处理异步调用时发生的异常情况


# 丢弃响应数据长度等于100的数据
class CustomMiddlewares(DownloaderMiddleware):
    def process_response(self, request, response, spider):
        if len(response.body) == 100:
            return IgnoreRequest("body length == 100")
        else:
            return response


# 自动切换UserAgent
class RandomUserAgent(object):
    def __init__(self, agents):
        self.agents = agents
    @classmethod
    def from_crawler(clscls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))
    def process_request(self, request, spider):
        request.header.setdefault('User-Agent', random.choice(self.agents))
# class UserAgentMiddleware(object):
#     """ 换User-Agent """
#
#     def process_request(self, request, spider):
#         agent = random.choice(agents)
#         request.headers["User-Agent"] = agent
#

# 自动切换代理IP
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        print "******ProxyMiddleware no pass********"+proxy['ip_port']
        request.meta['proxy'] = "http://%s" % proxy['ip_port']

        # if proxy['user_pass'] is not None:
        #     request.meta['proxy']="http://%s" % proxy['ip_port']
        #     encode_user_pass = base64.encodestring(proxy['user_pass'])
        #     request.headers['Proxy-Authorization'] = 'Basic' + encode_user_pass
        #     print "******ProxyMiddleware have pass*******"+proxy['ip_port']
        # else:
        #     print "******ProxyMiddleware no pass********"+proxy['ip_port']
        #     request.meta['proxy'] = "http://%s" % proxy['ip_port']


# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64


# 自动轮换代理
# # Start your middleware class
# class ProxyMiddleware(object):
#     # overwrite process request
#     def process_request(self, request, spider):
#         # Set the location of the proxy
#         request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
#
#         # Use the following lines if your proxy requires authentication
#         proxy_user_pass = "USERNAME:PASSWORD"
#         # setup basic authentication for the proxy
#         encoded_user_pass = base64.encodestring(proxy_user_pass)
#         request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

# class CookiesMiddleware(object):
#     """ 换Cookie """
#
#     def process_request(self, request, spider):
#         cookie = random.choice(cookies)
#         request.cookies = cookie

