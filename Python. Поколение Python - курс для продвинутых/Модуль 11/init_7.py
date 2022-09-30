# Функции
print('---------------------------------')
# Приведенный ниже код:
#  возвращает True, так как все значения списка равны True
print(all([True, True, True])) 
#  возвращает False, так как не все значения списка равны True    
print(all([True, True, False])) 
print('---------------------------------')
print(all([1, 2, 3]))   
print(all([1, 2, 3, 0, 5]))
print(all([True, 0, 1]))
print(all(('', 'red', 'green')))
print(all({0j, 3+4j}))
print('---------------------------------')
dict1 = {0: 'Zero', 1: 'One', 2: 'Two'}
dict2 = {'Zero': 0, 'One': 1, 'Two': 2}
print(all(dict1))
print(all(dict2))
print('---------------------------------')
print(all([]))          #  передаем пустой список
print(all(()))          #  передаем пустой кортеж
print(all(''))          #  передаем пустую строку
print(all([[], []]))    #  передаем список, содержащий пустые списки
print('---------------------------------')
# Приведенный ниже код:
#  возвращает True, так как есть хотя бы один элемент, равный True
print(any([False, True, False]))  
#  возвращает False, так как нет элементов, равных True     
print(any([False, False, False])) 
print('---------------------------------')
# Приведенный ниже код:
dict1 = {0: 'Zero'}
dict2 = {'Zero': 0, 'One': 1}
print(any(dict1))
print(any(dict2))
print('---------------------------------')
print(any([]))          #  передаем пустой список
print(any(()))          #  передаем пустой кортеж
print(any(''))          #  передаем пустую строку
print(any([[], []]))    #  передаем список, содержащий пустые списки
print('---------------------------------')
# Приведенный ниже код, проверяет, все ли элементы списка numbers больше 10:
numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]
result = all(map(lambda x: True if x > 10 else False, numbers))
if result:
    print('Все числа больше 10')
else:
    print('Хотя бы одно число меньше или равно 10')
print('---------------------------------')
numbers = [17, 91, 78, 55, 231, 45, 5, 89, 99, 11, 19]
result = any(map(lambda x: x % 2 == 0, numbers))
if result:
    print('Хотя бы одно число четное')
else:
    print('Все числа нечетные')
print('---------------------------------')
colors = ['red', 'green', 'blue']
for pair in enumerate(colors):
    print(pair)
print('---------------------------------')
colors = ['red', 'green', 'blue']
for pair in enumerate(colors, 100):
    print(pair)
print('---------------------------------')
colors = ['red', 'green', 'blue']
pairs = enumerate(colors)

print(pairs)
print(list(pairs))
print('---------------------------------')
colors = ['red', 'green', 'blue']
for index, item in enumerate(colors):
    print(index, item)
print('---------------------------------')
colors = ['red', 'green', 'blue']
for i in range(len(colors)):
    print(i, colors[i])
print('---------------------------------')
numbers = [1, 2, 3]
words = ['one', 'two', 'three']
for pair in zip(numbers, words):
    print(pair)
print('---------------------------------')
numbers = [1, 2, 3]
words = ['one', 'two', 'three']
result = zip(numbers, words)

print(result)
print(list(result))
print('---------------------------------')
numbers = [1, 2, 3]
words = ['one', 'two', 'three']
romans = ['I', 'II', 'III']

result = zip(numbers, words, romans)
print(list(result))
print('---------------------------------')
numbers = [1, 2, 3]
result = zip(numbers)
print(list(result))
print('---------------------------------')
numbers = [1, 2, 3, 4]
words = ['one', 'two']
romans = ['I', 'II', 'III']

result = zip(numbers, words, romans)
print(list(result))
print('---------------------------------')
keys = ['name', 'age', 'gender']
values = ['Timur', 28, 'male']

info = dict(zip(keys, values))
print(info)
print('---------------------------------')
name = ['Timur', 'Ruslan', 'Rustam']
age = [28, 21, 19]

for x, y in zip(name, age):
    print(x, y)
print('---------------------------------')
def all(iterable):
    for item in iterable:
       if not item:
           return False
    return True

def any(iterable):
    for item in iterable:
        if item:
            return True
    return False
print('---------------------------------')
list1 = ['a1', 'a2', 'a3']
list2 = ['b1', 'b2', 'b3']

# for index, (item1, item2) in enumerate(zip(list1, list2)):
for index, item in enumerate(zip(list1, list2)):
    print(index, item[0], item[1])
print('---------------------------------')
'''
Сценарий 3. C помощью zip() можно очень просто транспонировать матрицу:
'''
matrix = [[1, 2, 3, 4], 
          [5, 6, 7, 8], 
          [9, 10, 11, 12]]

# new_matrix = list(zip(*matrix))
new_matrix = list(map(list, zip(*matrix)))
print(new_matrix)


[print(*row) for row in new_matrix]
print('---------------------------------')
def zip2(*iterables):
    length = min(map(len, iterables))
    result = []
    for index in range(length):
        new_item = tuple(map(lambda item: item[index], iterables))
        result.append(new_item)
        print(new_item) #
    return result

print(zip2([1,2,3],['a','b']))
print('---------------------------------')
print(tuple(map(lambda item: item[0], ([1, 2, 3], ['a', 'b', 'v']))))
print('---------------------------------')
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(*zip(*[iter(l)]*3))
print(list(zip(*[iter(l)]*3)), sep='\n')
print('---------------------------------')
