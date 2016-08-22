# coding: utf-8
import time



# f = now
# print now.__name__
# print f.__name__

def log(func):
    def wrapper(*args, **kw):
        print"call %s():" % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print time.time()

# 以上三行就相当于以下三行

# def now():
#     print time.time()
# now = log(now)

now()