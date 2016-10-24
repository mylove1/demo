import threading
import time

counter = 0


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            name = l.pop()
            print name


if __name__ == "__main__":
    l = [x for x in range(2000)]
    for i in range(0, 20):
        my_thread = MyThread()
        my_thread.start()