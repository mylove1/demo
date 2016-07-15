# coding:utf-8
import hashlib

a = "570906f01f98ccc65a8b4629"
n = "成都P源健康咨询有限公司"
m = hashlib.md5()
m.update(n)

print m.hexdigest()

