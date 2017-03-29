def f(j):
    def g():
        return j*j
    return g

def count():
    res = []
    for i in range(1, 4):
        r = f(i)
        res.append(r)
    return res

f1, f2, f3 = count()
print f1(), f2(), f3()

