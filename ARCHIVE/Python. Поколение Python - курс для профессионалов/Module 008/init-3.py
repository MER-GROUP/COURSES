print('------------------')

def factorial(n):
    if n == 0:
        # базовый случай
        return 1                        
    else:
        # рекурсивный случай
        return n * factorial(n-1)    

print('Факториал числа 4 равен', factorial(4))   

print('------------------')

def sum_to(n):
    if 1 == n:
        return 1
    else:
        return n + sum_to(n-1)

print('Сумма чисел 5 равна', sum_to(5))   

print('------------------')

def sum_to(n):
    def rec(n: int = n):
        if 1 == n:
            return 1
        else:
            return n + sum_to(n-1)
    return rec(n)

print('Сумма чисел 5 равна', sum_to(1))   
print('Сумма чисел 5 равна', sum_to(5))   

print('------------------')

def sum_to(n):
    if n == 0:
        # базовый случай
        return 0                       
    else:
        # рекурсивный случай
        return n + sum_to(n - 1)      

print(sum_to(0))
print(sum_to(5))
print(sum_to(10))
print(sum_to(100)) 

print('------------------')

def recursive_sum(arr):
    i = 0
    def rec(_list=arr, i=i):
        if i == len(_list)-1:
            return _list[i]
        else:
            return _list[i] + rec(_list, i+1)
    return rec()

print(recursive_sum([1, 2, 3, 4, 5]))

print('------------------')

def recursive_sum(nums):    
    if not nums:
        # базовый случай
        return 0      
    # рекурсивный случай                                 
    return nums[0] + recursive_sum(nums[1:])  

numbers = [1, 9, 2, 8, 7, 3]

print(recursive_sum(numbers))         

print('------------------')

def fibo(n):
    if n in (1, 2):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(6))

print('------------------')

def fib(n):
    if n <= 2:
        # базовый случай
        return 1                             
    else:
        # рекурсивный случай
        return fib(n - 1) + fib(n - 2)       
    
print(fib(6))

print('------------------')

# ключ - номер числа, значения - число Фибоначчи 
cache = {1: 1, 2: 1}                

def fib(n):
    result = cache.get(n)
    if result is None:
        result = fib(n - 2) + fib(n - 1)
        cache[n] = result
    return result

print('------------------')

def fib(n):
    cache = {1: 1, 2: 1}
    def fib_rec(n):
        result = cache.get(n)
        if result is None:
            result = fib_rec(n - 2) + fib_rec(n - 1)
            cache[n] = result
        return result
    return fib_rec(n)

print('------------------')

fact = lambda n: 1 if n == 0 else n * fact(n - 1)

print(*map(fact, range(1, 11)))

print('------------------')