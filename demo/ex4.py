import math

def is_odd(x):
    return x%2 == 1

print filter(is_odd, [1, 3, 6, 7, 8, 9, 12, 13])

def is_not_empty(s):
    return s and len(s.strip()) > 0

print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])


def is_sqrt(x):
    r = int(math.sqrt(x))
    return r*r == x

print filter(is_sqrt, [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
