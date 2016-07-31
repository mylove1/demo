# coding:utf-8
import time

def twoSum(nums, target):
    l = [(target - x) for x in nums]
    ll = set(nums)&set(l)
    print ll
    print nums.index(ll[0])


twoSum([0, 2, 3, 0], 0)
twoSum([3,2,5], 5)
