# coding:utf-8
import numpy
import time

'''
这是看github上一个人的代码，虽然就一行，然而并没有什么卵用
10000之内的整数，一共一百万个进行排序，进行100次测试，平均时间11.3029999733
'''
def qsort(L):
    return (qsort([y for y in L[1:] if y < L[0]]) + L[:1] + qsort([y for y in L[1:] if y >= L[0]])) if len(L) > 1 else L


# 为什么这么慢，把他的代码拆开试试


def qsort1(L):
    global depth
    depth += 1
    if len(L) <= 1:
        return L
    mid = L[0]
    left_list = []
    right_list = []
    for x in L[1:]:
        if x < mid:
            left_list.append(x)
        else:
            right_list.append(x)
    left_list = qsort1(left_list)
    right_list = qsort1(right_list)
    return left_list + [mid] + right_list

# 情况还是那样
# 改为三个部分
def qsort2(L):
    global depth
    depth += 1
    if len(L) <= 1:
        return L
    mid = L[0]
    left_list = []
    right_list = []
    mid_list = []
    for x in L[1:]:
        if x < mid:
            left_list.append(x)
        elif x == mid:
            mid_list.append(x)
        else:
            right_list.append(x)
    left_list = qsort2(left_list)
    right_list = qsort2(right_list)
    return left_list + L[:1] + mid_list + right_list

# 好像是因为>=比较的问题
# >= 之后，深度会增加许多
# 通过对深度的计算，对于1000个100以内的整数，
# >= 时，深度1801左右
# 没有>= 时，深度201





    # return (qsort([y for y in L[1:] if y < L[0]]) + L[:1] + qsort([y for y in L[1:] if y >= L[0]])) if len(L) > 1 else L


if __name__ == '__main__':
    depth = 0
    l = numpy.random.randint(100, size=1000)
    l = list(l)
    start_time = time.time()
    l = qsort2(l)
    usetime = time.time() - start_time
    print usetime
    print depth
