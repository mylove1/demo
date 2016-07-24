# coding:utf-8
import threading
import time

l = [x for x in range(0, 50)]


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # 线程的名字默认为Thread-No形式的，
        # 更改线程的名字
        self.setName("new"+self.name)
    # 更改线程的名字
    def setName(self, name):
        self.name = "new---" + self.name

    def pr(self):
        print self.name, l.pop()
        time.sleep(0.1)

    def run(self):
        print self.name, l.pop()
        print self.name, l.pop()
        print self.name, l.pop()
        print self.name, l.pop()
        print self.name, l.pop()

    # def run(self):
    #     while len(l):
    #         print self.name, l.pop()

if __name__ == "__main__":
    for thread in range(0, 5):
        t = MyThread()
        t.start()

    print "==========================="
