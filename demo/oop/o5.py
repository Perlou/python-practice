class Person(object):
    count = 0

    @classmethod
    def cls_len(cls):
        return cls.count

    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

print Person.cls_len()
p1 = Person('Perlou')
print Person.cls_len()
