import time
a = ["http://www/%s/%s" % (x, y) for x in range(1, 4) for y in range(1, 3)]
print a
print time.ctime(time.time())