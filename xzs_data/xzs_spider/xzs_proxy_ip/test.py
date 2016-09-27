# coding:utf-8

class glo():
    def __init__(self, v):
        self.v = v
        self.v += 1
    def v(self):
        print self.v

a = 3
b = glo(a)
print a
print b.v