print('------------------')

def my_func():
    return 17

input = my_func
num = input()
print(num)
print(input())

print('------------------')

# def nop(*rest, **kwargs):
#     # заглушка, функция ничего не делает
#     pass                               

# print = nop
# print('Привет', 'мир')
# print('Stepik', 'Beegeek', 'Python', sep='*', end='')
# print('Stepik', 'Beegeek', 'Python', delimeter='-', endline='\n')

print('------------------')

def avg(nums):
    return sum(nums)/len(nums)

funcs = [len, sum, min, avg]

primes = [2, 3, 5, 7, 11]

for func in funcs:
    print(func(primes))

print('------------------')

funcs = {'capitalize': str.capitalize, 
         'swapcase': str.swapcase, 
         'title': str.title, 
         'lower': str.lower, 
         'upper': str.upper}

sentence = 'This is the Best course TO study in the world!'

print(funcs['upper'](sentence))
print(funcs['swapcase'](sentence))

print('------------------')

text = 'hello'
numbers = [1, 2, 3]

text_upper = str.upper(text)
list.append(numbers, 4)

print(text_upper)
print(numbers)

print('------------------')

def func(name, language='Python', year=1992):
    pass

# имя функции
print(func.__name__)  
# строка документирования        
print(func.__doc__) 
# кортеж с аргументами по умолчанию          
print(func.__defaults__)      

print('------------------')

print(abs.__doc__)
print(str.lower.__doc__)

print('------------------')

def square(n):
    '''Принимает число и возвращает его квадрат.'''
    return n**2

def average(*args):
    '''Принимает несколько чисел и возвращает их среднее арифметическое значение.'''
    return sum(args)/len(args)

print(square.__doc__)
print(average.__doc__)

print('------------------')

def sum_squares(nums):
    '''Принимает список чисел и возвращает сумму квадратов его элементов.'''
    total = 0
    '''Это уже не относится к строке документации.'''
    for i in nums:
        total += i ** 2
    return total

print(sum_squares.__doc__)

print('------------------')

def multiplier(num1, num2):
    """Перемножает два числа и возвращает их произведение.
    :параметр num1: int, float, первое число в произведении;
    :параметр num2: int, float, второе число в произведении;
    :возвращаемое значение: int, float, произведение двух чисел.
    """
    return num1 * num2

print('------------------')

def append(element, seq=[]):
    seq.append(element)

print(append.__defaults__)
append(10)
print(append.__defaults__)
append(20)
print(append.__defaults__)

print('------------------')

def append(element, seq=None):
    if seq is None:
        seq=[]
    seq.append(element)

print(append.__defaults__)
append(10)
print(append.__defaults__)
append(20)
print(append.__defaults__)

print('------------------')