class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if (self.score == s.score):
            return cmp(self.name, s.name)
        return -cmp(self.score, s.score)

L = [
    Student('Perlou1', 99),
    Student('Perlou2', 88),
    Student('Perlou3', 77),
    Student('Aerlou', 99)
]

print sorted(L)
