# coding:utf-8
import numpy
import time

def quick_sort(l, start, end):
    mid = l[start]
    i = start
    j = end
    while (i < j):
        while (l[j] > mid and i < j):
            j = j - 1
        l[i] = l[j]

        while (l[i] < mid and i < j):
            i = i + 1

        l[j] = l[i]

    l[i] = mid
    return l



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
# ------------------------
def quicksort(arr, left, right):
    # 只有left < right 排序
    if left < right:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)
    print arr


def partition(arr, left, right):
    """找到基准位置, 并返回"""
    pivot_index = left
    pivot = arr[left]

    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            # 如果此处索引的值小于基准值, 基准值的位置后移一位
            # 并将后移一位的值和这个值交换, 让基准位置及之前的始终小于基准值
            pivot_index += 1
            if pivot_index != i:
                arr[pivot_index], arr[i] = arr[i], arr[pivot_index]

    # 将基准值移动到正确的位置
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]

    return pivot_index

if __name__ == '__main__':
    # l = numpy.random.randint(10000, size=1000000)
    # l = list(l)
    l = [2, 3, 8, 0, 1, 8]
    start_time = time.time()
    l = quick_sort(l, 0, len(l)-1)
    print l
    usetime = time.time() - start_time
    print usetime
    # print l
    # print avg_test()
