a = [3]
print a.pop()
try:
    print a.pop()
except IndexError:
    print 'meiyou l '
print a

b = {}
def ttt(m, ind):
    try:
        print m[ind]
    except:
        print ',,,'
ttt(a, 38)


m['3'] = 'sdf'
print m