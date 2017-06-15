#!/usr/bin/env python2
# -*- coding: utf-8 -*-

class Fib(object):
    def __call__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(n)
            a, b = b, a + b
        return L

f = Fib()
print f(20)
