class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Aart'

p3 = Person()
p3.name = 'Eart'

p4 = Person()
p4.name = 'lart'

L1 = [p1, p2, p3, p4]
L2 = sorted(L1, lambda p1, p2: cmp(p1.name, p2.name))

print L2[0].name
print L2[1].name
print L2[2].name
print L2[3].name

        