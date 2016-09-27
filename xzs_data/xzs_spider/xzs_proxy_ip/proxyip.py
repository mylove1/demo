# coding:utf-8
import sys
from crawl import crawl


help = '''
Usage: python proxyip.py [OPTIONS]
  crawl     from web get useful proxy ip
'''

COMMOND = sys.argv[1:]
if len(COMMOND) == 0:
    print help
    sys.exit(0)

if COMMOND[0] == "crawl":
    crawl()
elif COMMOND[0] == 'ip_web':
    from ip_web import ip_web
    ip_web()

else:
    print help