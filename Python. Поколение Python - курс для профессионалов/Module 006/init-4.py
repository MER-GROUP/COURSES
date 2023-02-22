print('------------------')

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])

timur = Person('Тимур', 29, 170)

print(timur.name)
print(timur.age)
print(timur.height)

print('------------------')

timur = {'name': 'Тимур', 'age': 29, 'height': 170}

print(timur['name'])
print(timur['age'])
print(timur['height'])

print('------------------')

timur = {'name': 'Тимур', 'age': 29, 'height': 170}
# изменяем значение в словаре
timur['age'] = 30      
# выводим измененное значение
print(timur['age'])    

print('------------------')

# from collections import namedtuple

# Person = namedtuple('Person', ['name', 'age', 'height'])

# timur = Person('Тимур', 29, 170)
# timur.age = 30

# print(timur.age)

print('------------------')

from collections import namedtuple
from pympler import asizeof

Person = namedtuple('Person', ['name', 'age', 'height'])

timur = Person('Тимур', 29, 170)
timur_dct = {'name': 'Тимур', 'age': 29, 'height': 170}

print(f'Именованный кортеж: {asizeof.asizeof(timur)} байт')
print(f'Словарь: {asizeof.asizeof(timur_dct)} байт')

import sys

print('-----')
print(f'Именованный кортеж: {sys.getsizeof(timur)} байт')
print(f'Словарь: {sys.getsizeof(timur_dct)} байт')

print('------------------')

from collections import namedtuple
import sys

Person = namedtuple('Person', ['name', 'age', 'height'])

timur = Person('Тимур', 29, 170)
timur_dct = {'name': 'Тимур', 'age': 29, 'height': 170}

print(f'Именованный кортеж: {sys.getsizeof(timur)} байт')
print(f'Словарь: {sys.getsizeof(timur_dct)} байт')

print('------------------')

from collections import namedtuple
from time import perf_counter

def average_time(structure, test_func):
    time_measurements = []
    for _ in range(1_000_000):
        start = perf_counter()
        test_func(structure)
        end = perf_counter()
        time_measurements.append(end - start)
    return sum(time_measurements) / len(time_measurements) * int(10**9)

def time_dict(dictionary):
    'name' in dictionary
    'missing_key' in dictionary
    28 in dictionary.values()
    'missing_value' in dictionary.values()
    dictionary['age']

def time_namedtuple(named_tuple):
    'name' in named_tuple._fields
    'missing_field' in named_tuple._fields
    28 in named_tuple
    'missing_value' in named_tuple
    named_tuple.age

Person = namedtuple('Person', ['name', 'age', 'height'])

timur = Person('Тимур', 29, 170)
timur_dct = {'name': 'Тимур', 'age': 29, 'height': 170}

print(f'Именованный кортеж: {average_time(timur, time_namedtuple)} наносекунд')
print(f'Словарь: {average_time(timur_dct , time_dict)} наносекунд')

print('------------------')