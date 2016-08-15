# coding:utf-8
import numpy
import time


def test():
    if 3 < 4:
        return 3
    pass
def speed_test():
    start_time = time.time()
    l = test()
    usetime = time.time() - start_time
    return usetime

def avg_test():
    total_time = 0
    times = 10000000
    for x in range(times):
        total_time += speed_test()
    return total_time/times



if __name__ == '__main__':
    print avg_test()