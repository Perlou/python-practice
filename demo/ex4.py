def is_odd(x):
    return x%2 == 1

print filter(is_odd, [1, 3, 6, 7, 8, 9, 12, 13])

def is_not_empty(s):
    return s and len(s.strip()) > 0

print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])


# def 
