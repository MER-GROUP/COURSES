# Перебор кортежей
print('####################')
# Вариант 1. Если нужны индексы элементов
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in range(len(numbers)):
    print(numbers[i])
# Вариант 2. Если индексы не нужны
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for num in numbers:
    print(num)
    
# распаковка кортежа
print('####################')
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
languages = ('Python', 'C++', 'Java')
print(*numbers)
print(*languages, sep='\n')

# Сравнение кортежей
print('####################')
print((1, 8) == (1, 8))
print((1, 8) != (1, 10))
print((1, 9) < (1, 2))
print((2, 5) < (6,))
print(('a', 'bc') > ('a', 'de'))
# TypeError: '<' not supported between instances of 'int' and 'str'
# print((7, 5) < ('java', 'python'))

# Сортировка кортежей
# сортировка функцией sorted
print('####################')
not_sorted_tuple = (34, 1, 8, 67, 5, 9, 0, 23)
print(not_sorted_tuple)
sorted_tuple = tuple(sorted(not_sorted_tuple))
print(sorted_tuple)
# сортировка методом sort
not_sorted_tuple = ('cc', 'aa', 'dd', 'bb')
tmp = list(not_sorted_tuple)
tmp.sort()
sorted_tuple = tuple(tmp)
print(sorted_tuple)

# Преобразование кортежа в список и строку (str(), list(), tuple(), join())
print('####################')
# Преобразование кортежа в список и наоборот
tuple1 = (1, 2, 3, 4, 5)
list1 = list(tuple1)
print(list1)
list1 = [1, 17.8, 'Python']
tuple1 = tuple(list1)
print(tuple1)
# Преобразование кортежа в строку и наоборот
notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
string1 = ''.join(notes)
string2 = '.'.join(notes)
print(string1)
print(string2)
letters = 'abcdefghijkl'
tpl = tuple(letters)
print(tpl)
# TypeError: 'int' object is not iterable
# number = 12345
# tpl = tuple(number)
# print(tpl)