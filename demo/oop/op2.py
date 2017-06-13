class Person(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth

        for k, v in kw.iteritems():
            setattr(self, k, v)

Perlou = Person('Perlou', 'Male', '6666-66-66', job = 'FE', age = 18)

print Perlou
