a = [
{"name": 2,
     "age": 3},

    {"name": 3,
     "age": 4},

    ]
def f():
    for x in a:
        yield x["name"]

for x in f():
    print x