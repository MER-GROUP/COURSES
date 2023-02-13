print('------------------')

data1 = [1, 2, 3]
data2 = data1
data1.append(4)

print(id(data1), data1)
print(id(data2), data2)

print('------------------')

import copy

data1 = [1, 2, 3]
data2 = copy.copy(data1)
data1.append(4)

print(id(data1), data1)
print(id(data2), data2)

print('------------------')

import copy

data1 = [[1, 2, 3], [4, 5, 6]]
data2 = copy.copy(data1)

data1.append([7, 8, 9])

print(id(data1), data1)
print(id(data2), data2)

print('------------------')

import copy

data1 = [[1, 2, 3], [4, 5, 6]]
data2 = copy.copy(data1)

data1[0].append(7)
data2[1].append(8)

print(id(data1), data1)
print(id(data2), data2)

print('------------------')

import copy

data1 = [[1, 2, 3], [4, 5, 6]]
data2 = copy.deepcopy(data1)

data1[0].append(7)
data2[1].append(8)

print(id(data1), data1)
print(id(data2), data2)

print('------------------')

data1 = [1, 2, 3, 4]
data2 = [[1, 2], [3, 4]]

new_data1 = data1.copy()
new_data2 = data2.copy()

print(data1 is new_data1, data1 == new_data1)
print(data2 is new_data2, data2 == new_data2)

new_data1[0] = 100
new_data2[0][0] = 100

print(data1)
print(data2)

print('------------------')

data1 = [1, 2, 3, 4]
data2 = {'a': 1, 'b': 2}
data3 = {1, 2, 3, 4}

new_data1 = list(data1)
new_data2 = dict(data2)
new_data3 = set(data3)

print(data1 is new_data1, data1 == new_data1)
print(data2 is new_data2, data2 == new_data2)
print(data3 is new_data3, data3 == new_data3)

print('------------------')

data = [1, 2, 3, 4]

new_data = data[:]

print(data is new_data, data == new_data)

print('------------------')

data = [[1, 2], [3, 4]]

new_data = data[:]

data[0][0] = 10
new_data[1][1] = 40
 
print(data)
print(new_data)

print('------------------')

import sys

print(sys.getsizeof(10))
print(sys.getsizeof(True))
print(sys.getsizeof(None))
print(sys.getsizeof(''))
print(sys.getsizeof('beegeek'))

print('------------------')