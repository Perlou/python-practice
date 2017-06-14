# class Person(object):
#     __count = 0

#     @classmethod
#     def cls_len(cls):
#         return cls.__count

#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#         Person.__count = Person.__count + 1

# class Teacher(Person):
#     def __init__(self, name, gender, age, title, course):
#         super(Teacher, self).__init__(name, gender, age)
#         self.title = title
#         self.course = course

# t = Teacher('Perlou', 'Male', 18, '教授', 'Eng')

# print t.name

# class Person(object):
#     __count = 0

#     @classmethod
#     def cls_len(cls):
#         return cls.__count

#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

# class Teacher(Person):
#     def __init__(self, name, gender, course):
#         super(Teacher, self).__init__(name, gender)
#         self.course = course

# t = Teacher('Alice', 'Female', 'English')
# print t.name
# print t.course

# print t.cls_len()
