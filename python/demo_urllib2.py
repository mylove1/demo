# coding:utf-8
import urllib2


url = "http://httpbin.org/ip"
headers = {
    'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.\
    36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'
    }
data = {
    'ABC','abc',
}
data = 'sdfsdfsdf'
# # request = urllib2.Request(url, headers=headers)
# request = urllib2.Request(url)
# # req = urllib2.
# request.add_data(data)
# # request.add_header(headers)
html = urllib2.urlopen(url, data=data)
print html.read()
print request.port
print dir(request)