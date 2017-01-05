class Person:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError('Age must be within [18, 99]')

p1 = Person(20)
print(p1.age)
p2 = Person(120)
print(p2.age) # OK
p2.age = 110 # not OK

