# coding:utf-8
import threading
import re
import time

class Xizhi(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.num = n
    def run(self):
        while 1:
            print len(li)
            if self.num == 4:
                li.pop()
            print self.num
            time.sleep(5)


if __name__ == '__main__':
    li = []
    for x in range(6):
        a = Xizhi(x)
        a.start()