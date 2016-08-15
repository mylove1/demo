# coding:utf-8
import time
import numpy

# 自己写的第一个快排，通过把列表分为三部分，
# 10000之内的整数，一共一百万个进行排序，进行100次测试，平均时间3.21119998693
'''
由于第一个想法是分为左右两个部分，而不是后来的三个部分，当时为了照顾小于等于造成的最后分为的小列表
元素大于1，所以就把检查列表元素数目放到了最后，而且有很多的情况检查，后来发现这种分为两个部分的方法
有点牵强就放弃了，但是也没有改动（结尾检查等部分）造成了很多的啰嗦，下个版本把检查放到开头就会很简单了
'''

# 输入一个列表，输出排序后的列表
def quick_sort(l):
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

    if len(left_l) <= 1:
        pass
    else:
        if left_l == l:
            return l
        left_l = quick_sort(left_l)

    if len(mid_l) <= 1:
        pass
    else:
        if mid_l == l:
            return l
        mid_l = quick_sort(mid_l)

    if len(right_l) <= 1:
        pass
    else:
        if right_l == l:
            return l
        right_l = quick_sort(right_l)

    this_list = left_l + mid_l + right_l
    if this_list == l:
        return l
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
    times = 100
    for x in range(times):
        print x
        total_time += speed_test()
    return total_time/times



if __name__ == '__main__':
    print avg_test()


    # print l
