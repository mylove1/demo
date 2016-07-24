import time


def xx(num):
    if num == 2:
        time.sleep(1)
        print num
    else:
        print num
    return num

if __name__ == '__main__':
    a = [x for x in range(10)]
    b = map(xx,a)
    print b

