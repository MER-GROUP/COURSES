# Создание множества
print('###################')
numbers = {2, 4, 6, 8, 10}
languages = {'Python', 'C#', 'C++', 'Java'}
info = {'Timur', 1992, 61.5}
print(numbers)
print(languages)
print(info)

# Пустое множество
print('###################')
# пустое множество
myset = set()
print(type(myset))
# создается словарь
myset = {}
print(type(myset))

# Вывод множества
print('###################')
numbers = {2, 4, 6, 8, 10}
languages = {'Python', 'C#', 'C++', 'Java'}
mammals = {'cat', 'dog', 'fox', 'elephant'}
print(numbers)
print(languages)
print(mammals)

# Встроенная функция set()
print('###################')
# множество из элементов последовательности
myset1 = set(range(10))
# множество из элементов списка
myset2 = set([1, 2, 3, 4, 5])
# множество из элементов строки
myset3 = set('abcd')
# множество из элементов кортежа
myset4 = set((10, 20, 30, 40))
print(myset1)
print(myset2)
print(myset3)
print(myset4)

# Пустое множество
print('###################')
# пустое множество из пустого списка
emptyset1 = set([])
# пустое множество из пустой строки
emptyset2 = set('')
# пустое множество из пустого кортежа
emptyset3 = set(())
print(emptyset1)
print(emptyset2)
print(emptyset3)

# Дубликаты при создании множеств
print('###################')
myset1 = {2, 2, 4, 6, 6}
myset2 = set([1, 2, 2, 3, 3])
myset3 = set('aaaaabbbbccccddd')
print(myset1)
print(myset2)
print(myset3)

# множество - каждый элемент — строковое значение
print('###################')
myset = set(['aaa', 'bbbb', 'cc'])
print(myset)

# множество - каждый элемент — символьное значение
print('###################')
myset = set('aaa bbbb cc')
print(myset)

# элементы изменяемых типов данных не могут входить в множества
print('###################')
# множество не может содержать список
# myset1 = {1, 2, [5, 6], 7}
# TypeError: unhashable type: 'list'
# множество не может содержать множество
# myset2 = {1, 2, {5, 6}, 7}
# TypeError: unhashable type: 'set'

# элементы не изменяемых типов данных могут входить в множества
print('###################')
# множество может содержать кортеж
myset = {1, 2, (5, 6), 7}
print(myset)