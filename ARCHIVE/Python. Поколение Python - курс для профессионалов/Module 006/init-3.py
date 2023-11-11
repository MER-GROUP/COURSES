print('------------------')

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])

tim = Person('Тимур', 29, 170)

print(tim)
print(tim._fields)
print(Person._fields)

print('------------------')

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])
# распаковка полей старого кортежа
ExtendedPerson = namedtuple('ExtendedPerson', [*Person._fields, 'weight'])  
timur = ExtendedPerson('Тимур', 29, 170, 65)

print(timur)
print(ExtendedPerson._fields)

print('------------------')

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])

timur = Person('Тимур', 29, 170)

for field, value in zip(Person._fields, timur):
    print(field, '->', value)

print('------------------')

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height', 'country'], defaults=['Russia'])

timur = Person('Тимур', 29, 170)

print(timur)
print(timur._field_defaults)
print(Person._field_defaults)

print('------------------')

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height', 'country'])
timur = Person('Тимур', 29, 170, 'Russia')

print(Person._field_defaults)

print('------------------')

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])
timur = Person._make(['Timur', 29, 170])

print(timur)

print('------------------')

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])
timur = Person._make(['Timur', 29, 170])

print(timur._asdict())

print('------------------')

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height', 'country'])

timur1 = Person('Тимур', 29, 170, 'Russia')
timur2 = timur1._replace(age=30, country='Germany')

print(timur1)
print(timur2)

print('------------------')