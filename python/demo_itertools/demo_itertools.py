# coding:utf-8
from itertools import cycle
import threading
import time


class appen(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for x in xrange(100):
            if x > 20:
                break
            l.append(x)
            time.sleep(1)

class prin(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for inem in cycle(l):
            print inem
            time.sleep(0.3)

if __name__ == '__main__':
    l = []
    a = appen()
    a.start()
    time.sleep(3)
    b = prin()
    b.start()