print('------------------')

# info = {'name': 'Timur', 'age': 29, 'job': 'Teacher'}

# print(info['salary'])

print('------------------')

from collections import defaultdict

# создаем словарь со значением по умолчанию 0
info = defaultdict(int)       

info['name'] = 'Timur'
info['age'] = 29
info['job'] = 'Teacher'

print(info['salary'])
print(info)
print(type(info))

print('------------------')

from collections import defaultdict

info = defaultdict(int, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})

print(info['name'])
print(info['salary'])
print(info)

print('------------------')

from collections import defaultdict

info1 = defaultdict(int, name='Timur', age=29, job='Teacher')
info2 = defaultdict(int, [('name', 'Timur'), ('age', 29), ('job', 'Teacher')])

print(info1)
print(info2)

print('------------------')

from collections import defaultdict

info = defaultdict(name='Timur', age=29, job='Teacher')
print(info)

print('------------------')

# from collections import defaultdict

# info = defaultdict([('name', 'Timur'), ('age', 29), ('job', 'Teacher')])
# print(info)

print('------------------')

numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    value = result.setdefault(num, 0)
    result[num] = value + 1

print('------------------')

numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1

print('------------------')

numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1

print('------------------')

from collections import defaultdict

numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = defaultdict(int)

for num in numbers:
    result[num] += 1

print('------------------')

from collections import defaultdict

my_dict = defaultdict(list)

for i in range(7):
    my_dict[i].append(i)

for key in my_dict:
    print(key, my_dict[key])

print('------------------')

from collections import defaultdict

print(issubclass(defaultdict, dict))

print('------------------')

from collections import defaultdict

info1 = {'name': 'Timur', 'age': 29, 'job': 'Teacher'}
info2 = defaultdict(int, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})

print(info1 == info2)

print('------------------')

from collections import defaultdict

def get_default():
    return 69

info = defaultdict(get_default, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})

print(info['name'])
print(info['salary'])

print('------------------')

from collections import defaultdict

info = defaultdict(lambda: '1000000$', {'name': 'Timur', 'age': 29, 'job': 'Teacher'})

print(info['name'])
print(info['salary'])

print('------------------')

# from collections import defaultdict

# def get_default(x):
#     return 2 * x

# info = defaultdict(get_default, {'name': 'Timur', 'age': 29, 'job': 'Teacher'})

# print(info['name'])
# print(info['salary'])

print('------------------')

# from collections import defaultdict

# info = defaultdict(lambda x: '1000000$', {'name': 'Timur', 'age': 29, 'job': 'Teacher'})

# print(info['name'])
# print(info['salary'])

print('------------------')

# from collections import defaultdict

# data = defaultdict()
# print(data['salary'])

print('------------------')

# from collections import defaultdict

# data = defaultdict(None)
# print(data['salary'])

print('------------------')

from collections import defaultdict

info = defaultdict(name='Timur', age=29, job='Teacher')
print(info)
print(info['name'])
# print(info['red'])

print('------------------')

from collections import defaultdict

data = defaultdict(int)
print(data['salary1'])

data.default_factory = list
print(data['salary2'])

data.default_factory = float
print(data['salary3'])

print(data)

print('------------------')