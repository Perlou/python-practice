import json

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

def who_am_i(x):
    print x.whoAmI()

p = Person('Perlou', 'Male')
s = Student('Perlous', 'Male', 66)

who_am_i(p)
who_am_i(s)

class Students(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'

t = Students()
print json.load(s)

