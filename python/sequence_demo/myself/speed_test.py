# coding:utf-8
import numpy
import time


if __name__ == '__main__':
    # l = numpy.random.randint(1000, size=20)
    # l = list(l)
    start_time = time.time()
    for x in xrange(10000000):
        l = []
    print time.time() - start_time
