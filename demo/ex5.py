def f1(x):
    return x*2

def new_fn(f):
    def fn(x):
        print 'call' + f.__name__ + '()'
        return f(x)
    return fn

g1 = new_fn(f1)
print g1(5)