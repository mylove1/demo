# coding:utf-8
import sys

print hasattr(sys, "frozen")
print sys.executable
print __file__
class M():
    def __init__(self):
        self.name = "M"
class MM(M):
    def __init__(self):
        M.__init__(self)
a = MM()
print a.name