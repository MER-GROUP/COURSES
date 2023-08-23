print('------------------')

from itertools import groupby

numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]

group_iter = groupby(numbers)

print(type(group_iter))
print(*group_iter, sep='\n')
print(*group_iter, sep='\n')

print('------------------')

from itertools import groupby

numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]

group_iter = groupby(numbers)

for key, values in group_iter:
    # преобразуем итератор в список
    print(f'{key}: {list(values)}')   

print('------------------')

from itertools import groupby

numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]

group_iter = groupby(sorted(numbers))

for key, values in group_iter:
    # преобразуем итератор в список
    print(f'{key}: {list(values)}')    

print('------------------')

numbers = [-81, 2, -6, -3, 9, -17, -8, -6, 7]

print(min(numbers, key=abs))               # минимальный элемент по модулю
print(max(numbers, key=lambda num: num**2))# элемент с максимальным квадратом
print(sorted(numbers, key=abs))            # сортировка элементов по модулю

print('------------------')

from itertools import groupby

numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]

group_iter = groupby(numbers, key=lambda num: num < 10)

for key, values in group_iter:
    print(f'{key}: {list(values)}')

print('------------------')

from itertools import groupby

numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]

key_func = lambda num: num < 10
print(sorted(numbers, key=key_func))

group_iter = groupby(sorted(numbers, key=key_func), key=key_func)

for key, values in group_iter:
    print(f'{key}: {list(values)}')

print('------------------')

from itertools import groupby

data = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'A', 'A', 'B', 'B', 'B']

result = [key for key, group in groupby(data)] 

print(result)

print('------------------')

from itertools import groupby

data = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'A', 'A', 'B', 'B', 'B']

result = [key for key, group in groupby(sorted(data))] 

print(result)

print('------------------')

from itertools import groupby

data = 'aaabcdaabcccdddcccccccbrttbcc'
group_iter = groupby(sorted(data))

max_result = max(group_iter, key=lambda tpl: sum(1 for i in tpl[1]))

print('Символ встречающийся чаще всего в строке:', max_result[0])

print('------------------')

from itertools import groupby

data = 'aaabcdaabcccdddcccccccbrttbcc'
group_iter = groupby(sorted(data))

saved_data = [(key, list(group)) for key, group in group_iter]

# можем уже использовать len()
max_result = max(saved_data, key=lambda tpl: len(tpl[1]))       
min_result = min(saved_data, key=lambda tpl: len(tpl[1]))

print('Символ встречающийся чаще всего в строке:', max_result[0])
print('Символ встречающийся реже всего в строке:', min_result[0])

print('------------------')

from itertools import groupby

numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]

group_iter = groupby(numbers)

group1 = next(group_iter)[1]
group2 = next(group_iter)[1]
group3 = next(group_iter)[1]

print(list(group1))
print(list(group2))
print(list(group3))

print('------------------')

from itertools import groupby

numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]

group_iter = groupby(numbers)

group1 = next(group_iter)
group2 = next(group_iter)
group3 = next(group_iter)

print(list(group1))
print(list(group2))
print(list(group3))

print('------------------')

from itertools import groupby

numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]

group_iter = groupby(numbers)

group1 = next(group_iter)[1]
print(group1)
group2 = next(group_iter)[1]
print(group1)
# group3 = next(group_iter)[1]
# print(group1)

print(list(group1))
# print(list(group2))
# print(list(group3))

print('------------------')

from itertools import groupby

numbers = [1, 1, 1, 7, 7, 7, 7, 15, 7, 7, 7]

group_iter = groupby(numbers)

group1 = next(group_iter)[1]
print(list(group1))

group2 = next(group_iter)[1]
print(list(group2))

group3 = next(group_iter)[1]
print(list(group3))

print('------------------')

data = [1, 9, 5, 3, 4, 10, 2, 6]

print(sorted(data))
print(sorted(set(data)))
print(sorted(iter(data)))

print('------------------')