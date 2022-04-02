# инициализация списков
print('##########')
numbers = [10, 3]
constants = [3.1415, 2.71828, 1.1415]
countries = ['Russia', 'Armenia', 'Argentina']
flags = [True, False]

print(numbers)
print(constants)
print(countries)
print(flags)

# инициализация списков разными типами
print('##########')
info = ['Timur', 1992, 72.5]

print(info)

# инициализация вложенных списков
print('##########')
my_list = [[0], [1, 2], [3, 4, 5]]

print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(len(my_list))

my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik']]

print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])

# индексация вложенных списков
print('##########')
my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik!']]

# индексирование строки 'Python'
print(my_list[0][2])
# индексирование списка [10, 20, 30]
print(my_list[1][1])
# индексирование списка ['Beegeek', 'Stepik!']
print(my_list[2][-1])
# индексирование строки 'Stepik!'
print(my_list[2][-1][-1])

# # у списка my_list индексы от 0 до 2
# вызовет ошибку:
# IndexError: index out of range
# print(my_list[3])

# функция len()
print('##########')
my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]

print(len(my_list))

# функция len()
total = 0
my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]

for li in my_list:
    total += len(li)

print(total)

# функция max() и min()
print('##########')
list1 = [1, 7, 12, 0, 9, 100] 
list2 = [1, 7, 90] 
list3 = [1, 10]

print(min(list1, list2, list3))
print(max(list1, list2, list3))

# функция max() и min()
print('##########')
list1 = [[1, 7, 12, 0, 9, 100], [1, 7, 90], [1, 10]]
list2 = [['a', 'b'], ['a'], ['d', 'p', 'q']]

print(min(list1))
print(max(list1))
print(min(list2))
print(max(list2))

# my_list = [[1, 7, 12, 0, 9, 100], ['a', 'b']]
# print(min(my_list))
# print(max(my_list))
# приведет к возникновению ошибки:
# TypeError: '<' not supported between instances of 'str' and 'int'