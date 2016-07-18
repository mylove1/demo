# coding:utf-8
import threading
import time

l = [x for x in range(0, 50)]


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def pr(self):
        print self.name, l.pop()
        time.sleep(0.1)

    def run(self):
        while True:
            if len(l):
                self.pr()

if __name__ == "__main__":
    for thread in range(0, 10):
        t = MyThread()
        t.start()
