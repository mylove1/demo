# coding:utf-8
import urlparse

base_url = "http://www.zhihu.com/index.php?username=guol"
long_url = 'http://www.baidu.com/index.php?username=guol'
s = '/sdfoijsd.html'


url = urlparse.urlparse(long_url)   # 将long_url解析为6个部分
print(url)
# long_url = urlparse.urlunparse(scheme='ftp', netloc='www.baidu.com', path='/index.php', params='', query='username=guol', fragment='')
# print long_url

url = urlparse.urljoin('http://222.143.24.157/businessPublicity.jspx','?id=3')
print urlparse.urljoin(base_url, s)