my_set = set()
my_set.add('red')
my_set.add('alert')
print(my_set)

print('------------------')

my_tuple = (1, 2, 3)
print(my_tuple)
print(type(my_tuple))
print(str(my_tuple))
print(type(str(my_tuple)))

print('------------------')

arr = [1, 2, 3, 4, 5]
arr_sub = [2, 3]
print(set(arr_sub).issubset(arr))
arr = ['1', '2', '3', '4', '5']
arr_sub = ['2', '3']
print(set(arr_sub).issubset(arr))
arr = ['1', '2', '3', '4', '5']
arr_sub = ['2', '3', '25']
print(set(arr_sub).issubset(arr))
arr = ['1', '2', '3', '4', '5']
arr_sub = ['2', '45', '3']
print(set(arr_sub).issubset(arr))
arr = ['1', '2', '3', '4', '5']
arr_sub = ['2', '45', '3']
print(set(arr_sub).intersection(arr))
arr = ['454']
arr_sub = ['2', '45', '3']
print(set(arr_sub).intersection(arr))

print('------------------')

word = '12345'
for i in range(len(word)-1, -1, -1):
    print(word[i], end='')
print()

print('------------------')

s = [1, 1, 0, 0, 1]
print(s[ : len(s) - s[::-1].index(1)])

print('------------------')

digits = '0123456789'
name = 'max274'
name = name.rstrip(digits)
print(name)

print('------------------')

my_dict = dict()
my_dict['mp3'] = {'111': 1, '222': 2}
print(my_dict)

print('------------------')

print('####################')
info = {'name': 'Bob', 'age': 25}
# параметр default не задан
name1 = info.setdefault('name')
# параметр default задан
name2 = info.setdefault('name', 'Max')
print(name1)
print(type(name1))
print(name2)
print(type(name2))
print('####################')
info = {'name': 'Bob', 'age': 25}
job = info.setdefault('job', 'Dev')
print(info)
print(type(info))
print(job)
print(type(job))

print('------------------')

print('####################')
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
result = {}
for num in numbers:
    result[num] = result.get(num, 0) + 1
print(result)
result = {}
for num in numbers:
    result[num] = result.setdefault(num, 0) + 1
print(result)