print('------------------')

def null_decorator(func):
    return func

print('------------------')

def say():
    print('Привет Мир!')

# декорируем функцию
say = null_decorator(say)      

# вызываем декорированную функцию
say()                          

print('------------------')

# определяем декоратор
def sample_decorator(func):          
    def wrapper():
        print('Начало функции')
        func()
        print('Конец функции')
    return wrapper

def say():
    print('Привет Мир!')

# декорируем функцию
say = sample_decorator(say)          
# вызываем декорированную функцию
say()                                

print('------------------')
# определяем декоратор
def sample_decorator(func):          
    def wrapper():
        print('Начало функции')
        func()
        print('Конец функции')
    return wrapper

def say():
    print('Привет Мир!')
print('------------------')

# до декорирования
print(say)                         
say = sample_decorator(say)
# после декорирования
print(say)                         

print('------------------')

def null_decorator(func):
    return func

def say():
    print('Привет Мир!')

# декорируем функцию
say = null_decorator(say)            

say()

print('------------------')

def null_decorator(func):
    return func

# декорируем функцию
@null_decorator                      
def say():
    print('Привет Мир!')

say()

print('------------------')

# определяем декоратор
def sample_decorator(func):          
    def wrapper():
        print('Начало функции')
        func()
        print('Конец функции')
    return wrapper

def say():
    print('Привет Мир!')

# декорируем функцию
say = sample_decorator(say)          
# вызываем декорированную функцию
say()                                

print('------------------')

# определяем декоратор
def sample_decorator(func):          
    def wrapper():
        print('Начало функции')
        func()
        print('Конец функции')
    return wrapper

# декорируем функцию
@sample_decorator                    
def say():
    print('Привет Мир!')

say()

print('------------------')

def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

print('------------------')

@uppercase_decorator
def greet():
    return 'Hello world!'

print(greet())

print('------------------')

def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def greet():
    return 'Hello world!'

print(greet)
# ручное декорирование
greet = uppercase_decorator(greet)     
print(greet)

print('------------------')

def bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def italic(func):
    def wrapper():
        return '<i>' + func() + '</i>'
    return wrapper
    
@bold
@italic
def greet():
    return 'Hello world!'

print(greet())

print('------------------')

def bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def italic(func):
    def wrapper():
        return '<i>' + func() + '</i>'
    return wrapper
    
def greet():
    return 'Hello world!'

greet = bold(italic(greet))

print(greet())

print('------------------')

def greet(name):
    return f'Hello {name}!'

print(greet('Timur'))

print('------------------')

# @bold
# def greet(name):
#     return f'Hello {name}!'

# print(greet('Timur'))

print('------------------')

def bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    return wrapper

@bold
def greet1(name):
    return f'Hello {name}!'

@bold
def greet2():
    return 'Hello world!'

@bold
def greet3(name, surname):
    return f'Hello {name} {surname}!'

print(greet1('Timur'))
print(greet2())
print(greet3('Timur', 'Guev'))

print('------------------')

def talk(func):
    def wrapper(*args, **kwargs):
        dash = '-' * 15
        print(dash)
        # вызываем декорируемую функцию
        func(*args, **kwargs)           
        print(dash)
    return wrapper

@talk
def greet(name):
    return f'Hello {name}!'

print(greet('Timur'))

print('------------------')

def talk(func):
    def wrapper(*args, **kwargs):
        dash = '-' * 15
        result = func(*args, **kwargs)
        return dash + '\n' + result + '\n' + dash
    return wrapper

@talk
def greet(name):
    return f'Hello {name}!'

print(greet('Timur'))

print('------------------')

def sample_decorator(func):
    print('Начало функции')
    func()
    print('Конец функции')

def say():
    print('Привет Мир!')

say = sample_decorator(say)

say

print('------------------')

def sample_decorator(func):
    print('Начало функции')
    func()
    print('Конец функции')

@sample_decorator
def say():
    print('Привет Мир!')

say

print('------------------')