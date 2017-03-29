def calc_prod(list):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, list, 1)
    return lazy_prod

f = calc_prod([1, 2, 3, 4])
print f()


