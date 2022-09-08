# Функции
def my_func(*args):
    print(type(args))
    print(args)

my_func()
my_func(1, 2, 3)
my_func('a', 'b')

print('---------------------------------')
# не является рабочим, так как параметр со звездочкой указан раньше позиционного num.
# def my_func(*args, num):
#     print(args)
#     print(num)
# my_func(17, 'Python', 2, 'C#')
print('---------------------------------')
# Приведенный ниже код:
def my_func(num, *args):
    print(args)
    print(num)
my_func(17, 'Python', 2, 'C#')
print('---------------------------------')
# Приведенный ниже код:
def my_func(num, *args):
    print(args)
    print(num)
my_func(17)
print('---------------------------------')
print(sum((5, 8)))
print('---------------------------------')
# Приведенный ниже код:
# sum1 = sum(1, 2, 3, 4)        
# print(sum1)
print('---------------------------------')
def my_sum(*args):
    # args - это кортеж
    return sum(args) 
# Приведенный ниже код:
print(my_sum())
print(my_sum(1))
print(my_sum(1, 2))
print(my_sum(1, 2, 3))
print(my_sum(1, 2, 3, 4)) 
print('---------------------------------')
# Приведенный ниже код:
def my_sum(*args):
    # args - это кортеж
    return sum(args) 
# распаковка списка
print(my_sum(*[1, 2, 3, 4, 5]))  
# распаковка кортежа 
print(my_sum(*(1, 2, 3))) 
print('---------------------------------')
test = 1, 3, 4, 5, 9 
print(test)
print('---------------------------------')
# Приведенный ниже код:
def my_sum(*args):
    # args - это кортеж
    return sum(args) 
print(my_sum(1, 2, *[3, 4, 5], *(7, 8, 9), 10))
print('---------------------------------')
# Рассмотрим определение функции my_func():
def my_func(**kwargs):
    print(type(kwargs))
    print(kwargs)
# Приведенный ниже код:
my_func()
my_func(a=1, b=2)
my_func(name='Timur', job='Teacher')
print('---------------------------------')
# Рассмотрим определение функции, которая принимает все виды аргументов.
def my_func(a, b, *args, name='Gvido', age=17, **kwargs):
    print(a, b)
    print(args)
    print(name, age)
    print(kwargs)
# Приведенный ниже код:
my_func(1, 2, 3, 4, name='Timur', age=28, job='Teacher', language='Python')
print('---------------------------------')
my_func(1, 2, name='Timur', age=28, job='Teacher', language='Python')
print('---------------------------------')
my_func(1, 2, 3, 4, job='Teacher', language='Python')
print('---------------------------------')
# Рассмотрим определение функции my_func():
def my_func(**kwargs):
    print(type(kwargs))
    print(kwargs)
# Приведенный ниже код:
info = {'name':'Timur', 'age':'28', 'job':'teacher'}
my_func(**info)
print('---------------------------------')
# 
def print_info(name, surname, age, city, *children, **additional_info):
    print('Имя:', name)
    print('Фамилия:', surname)
    print('Возраст:', age)
    print('Город проживания:', city)
    if len(children) > 0:
        print('Дети:', ', '.join(children))
    if len(additional_info) > 0:
        print(additional_info)
# Приведенный ниже код:
children = ['Бодхи Рансом Грин', 'Ноа Шэннон Грин', 'Джорни Ривер Грин']
additional_info = {'height':163, 'job':'actress'}

print_info('Меган', 'Фокс', 34, 'Ок-Ридж', *children, **additional_info)
print('---------------------------------')