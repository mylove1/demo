class hello():
    def __init__(self):
        self.a = {
            "b": [2, 3, ]
        }

    def hello(self, sd):
        self.a["b"].append(sd)
        print self.a


def hel():
    for x in range(20):
        yield x


def addadd(x):
    x += 1


maping = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
}
column = ['b', 'c', 'a']

dic = {
    'A': '1',
    'B': '2',
    'C': '3',
}

print [dic[maping[x]] for x in column]