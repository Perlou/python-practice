class Person(object):
    count = 0
    def __init__(self, name):
        Person.count = Person.count + 1
        self.name = name

p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count

class Person2(object):
    __count = 0
    def __init__(self, name):
        Person2.__count = Person2.__count + 1
        self.name = name
        print Person2.__count

p1 = Person2('Perlou1')
p2 = Person2('Perlou2')

print Person2.__count
