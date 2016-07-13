# coding:utf-8
import urlparse

base_url = "http://www.zhihu.com"
long_url = 'http://www.baidu.com/index.php?username=guol'



url = urlparse.urlparse(long_url)   # 将long_url解析为6个部分
print(url)
long_url = urlparse.urlunparse(scheme='ftp', netloc='www.baidu.com', path='/index.php', params='', query='username=guol', fragment='')
print long_url