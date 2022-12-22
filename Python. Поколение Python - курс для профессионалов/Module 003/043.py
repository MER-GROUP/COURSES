'''
Функция get_the_fastest_func()
Реализуйте функцию get_the_fastest_func(), 
которая принимает два аргумента в следующем порядке:

funcs — список произвольных функций
arg — произвольный объект

Функция get_the_fastest_func() должна возвращать функцию из списка funcs, 
которая затратила на вычисление значения при вызове с аргументом arg наименьшее количество времени.

Примечание. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию get_the_fastest_func(), 
но не код, вызывающий ее.
'''
from time import perf_counter, sleep

def get_the_fastest_func(funcs, arg):
    dictonary = dict()
    for func in funcs:
        start = perf_counter()
        func(arg)
        dictonary[func] = dictonary.get(func, 0) + perf_counter() - start
    return min(dictonary, key=dictonary.get)

def get_the_fastest_func_2(funcs):
    dictonary = dict()
    for func in funcs:
        start = perf_counter()
        func()
        dictonary[func] = dictonary.get(func, 0) + perf_counter() - start
    return min(dictonary, key=dictonary.get)

def add1(a):
    sleep(1)
    return a

def add2(a):
    sleep(2)
    return a

# функция из модуля math 
from math import factorial                       

# рекурсивная функция
def factorial_recurrent(n):                  
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)    

# итеративная функция
def factorial_classic(n):                    
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

# # с использованием цикла for и метода append()
# def for_and_append():                            
#     iterations = 10_000_000
#     result = []
#     for i in range(iterations):
#         result.append(i + 1)
#     return result
        
# # с использованием списочного выражения
# def list_comprehension():                        
#     iterations = 10_000_000
#     return [i + 1 for i in range(iterations)]  


# с использованием цикла for и метода append()
def for_and_append(iterable):             
    result = []
    for elem in iterable:
        result.append(elem)
    return result
        
# с использованием списочного выражения
def list_comprehension(iterable):         
    return [elem for elem in iterable]    
    
# с использованием встроенной функции list()
def list_function(iterable):              
    return list(iterable) 

if __name__ == '__main__':
    print(
        get_the_fastest_func([add1, add2], 5),
        get_the_fastest_func([add1, add2], 5)(2),
        sep='\n'
    )
    print(
        get_the_fastest_func([factorial, factorial_recurrent, factorial_classic], 900),
        get_the_fastest_func([factorial, factorial_recurrent, factorial_classic], 900)(900),
        sep='\n'
    )
    # print(
    #     get_the_fastest_func_2([for_and_append, list_comprehension]),
    # )
    print(
        get_the_fastest_func([for_and_append, list_comprehension, list_function], range(100_00)),
    )