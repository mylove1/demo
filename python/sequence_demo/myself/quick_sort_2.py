# coding:utf-8
import time
import numpy

# 对写的第一个快排进行改进，通过把列表分为三部分，
# 10000之内的整数，一共一百万个进行排序，进行100次测试，平均时间3.16866001606
# 对第一个版本进行了一些改动效率提高的不是太明显
# 输入一个列表，输出排序后的列表
def quick_sort(l):
    if len(l) <= 1:
        return l
    mid = l[0]
    left_l = []
    mid_l = []
    right_l = []

    for x in l:
        if x < mid:
            left_l.append(x)
        elif x == mid:
            mid_l.append(x)
        else:
            right_l.append(x)
    left_l = quick_sort(left_l)
    right_l = quick_sort(right_l)


    this_list = left_l + mid_l + right_l
    return this_list

def speed_test():
    l = numpy.random.randint(10000, size=1000000)
    l = list(l)
    start_time = time.time()
    l = quick_sort(l)
    usetime = time.time() - start_time
    return usetime

def avg_test():
    total_time = 0
    times = 10
    for x in range(times):
        print x
        total_time += speed_test()
    return total_time/times



if __name__ == '__main__':
    l = numpy.random.randint(10000, size=1000000)
    l = list(l)
    start_time = time.time()
    l = quick_sort(l)
    usetime = time.time() - start_time
    print usetime
    # print l
    # print avg_test()


    # print l
