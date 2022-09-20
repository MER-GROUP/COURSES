# Функции
print('---------------------------------')
# функция высшего порядка, так как принимает функцию
# Здесь функция high_order_function() принимает другую функцию на входе и возвращает результат её вызова с аргументом, равным 33.
def high_order_function(func):     
    return func(3)
# обычная функция = функция первого порядка
def double(x):                     
    return 2*x
# обычная функция = функция первого порядка
def add_one(x):                    
    return x + 1
# Приведенный ниже код:
print(high_order_function(double))
print(high_order_function(add_one))
print('---------------------------------')
# Например, для преобразования списка чисел в список их квадратов, код может выглядеть так:
def f(x):
    return x**2     # тело функции, которая преобразует аргумент x

old_list = [1, 2, 4, 9, 10, 25]
new_list = []
for item in old_list:
    new_item = f(item)
    new_list.append(new_item)

print(old_list)
print(new_list)
print('---------------------------------')
def map(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)
    return result
'''
Теперь мы можем совершать преобразования, используя функцию высшего порядка map().
'''
# Приведенный ниже код:
def square(x):
    return x**2
def cube(x):
    return x**3
numbers = [1, 2, -3, 4, -5, 6, -9, 0]
# используем в качестве преобразователя - функцию str
strings = map(str, numbers)   
# используем в качестве преобразователя - функцию abs     
abs_numbers = map(abs, numbers)    
# используем в качестве преобразователя - функцию square
squares = map(square, numbers) 
# используем в качестве преобразователя - функцию cube    
cubes = map(cube, numbers)  

print(strings)
print(abs_numbers)
print(squares)
print(cubes)
print('---------------------------------')
# Приведенный ниже код, при условии, что функция map() определена как указано выше:
strings = ['10', '12', '-4', '-9', '0', '1', '23', '100', '99']
# используем списочное выражение для преобразования
numbers1 = [int(c) for c in strings]  
# используем функцию map() для преобразования 
numbers2 = map(int, strings)               

print(numbers1)
print(numbers2)
print('---------------------------------')
numbers = ['-1', '20', '3', '-94', '65', '6', '-970', '8']
new_numbers = map(abs, map(int, numbers))
print(new_numbers)
print('---------------------------------')
# Реализация такой функции может выглядеть так:
def filter(function, items):
    result = []
    for item in items:
        if function(item): 
            # добавляем элемент item если функция function вернула значение True       
            result.append(item)  
    return result

def is_greater10(num):   
    return num > 10

numbers = [12, 2, -30, 48, 51, -60, 19, 10, 13]
#  список large_numbers содержит элементы, большие 10
large_numbers = filter(is_greater10, numbers)   
print(large_numbers)
print('---------------------------------')
# Приведенный ниже код, при условии, что функция filter() определена как указано выше:
def is_odd(num):
    return num % 2
def is_word_long(word):
    return len(word) > 6

numbers = list(range(15))
words = ['В', 'новом', 'списке', 'останутся', 'только', 'длинные', 'слова']

odd_numbers = filter(is_odd, numbers)
large_words = filter(is_word_long, words)

print(odd_numbers)
print(large_words)
print('---------------------------------')
numbers = [1, 2, 3, 4, 5]
total = 0
product = 1

for num in numbers:
    total += num
    product *= num

print(total)
print(product)
print('---------------------------------')
def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc

# Приведенный ниже код, при условии, что функция reduce() определена как указано выше:
def add(x, y):
    return x+y
def mult(x, y):
    return x*y

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers, 0)
product = reduce(mult, numbers, 1)

print(total)
print(product)
print('---------------------------------')
lst = [1, 2, 3, 4, 5]
for i in map(print, lst):
    i
print('---------------------------------')
import functools
print('---------------------------------')