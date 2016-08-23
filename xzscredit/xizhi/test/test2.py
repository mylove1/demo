a = [3]
print a.pop()
try:
    print a.pop()
except IndexError:
    print 'meiyou l '
print a