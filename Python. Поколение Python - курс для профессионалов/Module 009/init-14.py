print('------------------')

def multiply(a, b):
    return a * b

print(multiply(2, 3))

def double(num):
    return multiply(2, num)
 
def triple(num):
    return multiply(3, num)

print('------------------')

from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)
triple = partial(multiply, 3)

print(double(5))        # 2 * 5
print(triple(10))       # 3 * 10

print('------------------')

# print(double(5, 6))

print('------------------')

multiply_two_and_five = partial(multiply, 2, 5)
# вызываем уже без аргументов
print(multiply_two_and_five())  

print('------------------')

print(int('123'))
print(int('123', base=5))
print(int('1001', base=2))
print(int('A12B', base=16))

print('------------------')

from functools import partial

basetwo = partial(int, base=2)

print(basetwo('101'))
print(basetwo('1000'))
print(basetwo('11111'))

print('------------------')

from functools import partial

def pretty_print(text, symbol, count):
    print(symbol * count)
    print(text)
    print(symbol * count)

star_pretty_print = partial(pretty_print, 'Hi!!!', symbol='*')

star_pretty_print(count=7)

print(star_pretty_print.args)
print(star_pretty_print.keywords)

star_pretty_print.func('Исходная функция', symbol='~', count=20)

print('------------------')

from functools import partial

def multiply(a, b):
    '''Функция перемножает два числа и возвращает вычисленное значение.'''
    return a * b

double = partial(multiply, 2)

print(double.func.__name__)
print(double.func.__doc__)

print('------------------')

from functools import partial, update_wrapper

def multiply(a, b):
    '''Функция перемножает два числа и возвращает вычисленное значение.'''
    return a * b

double = partial(multiply, 2)
# копируем информацию из функции multiply в partial объект double
update_wrapper(double, multiply)   

print(double.__name__)
print(double.__doc__)

print('------------------')

from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)

print(type(double))

print('------------------')

from functools import update_wrapper

def my_func():
    """Wrapped function."""
    return 'This original func'

def wrapper_func():
    """Wrapper function."""
    return 'This wrapper func'

print(wrapper_func.__name__) # 'wrapper_func'
print(wrapper_func.__doc__) # 'Wrapper function.'
print(wrapper_func()) # This wrapper func
wrapper_func = update_wrapper(wrapper_func, my_func)
print(wrapper_func.__name__) # 'my_func'
print(wrapper_func.__doc__) # 'Wrapped function.'
print(wrapper_func()) # This wrapper func
print(wrapper_func.__wrapped__()) # This original func

print('------------------')

# from functools import partial

# def add(a, b):
#     '''documentation'''
#     return a + b

# add_one = partial(add, 1)

# print(add_one.__name__)
# print(add_one.__doc__)

print('------------------')