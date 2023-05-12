print('------------------')

def speak(text):
    # объявляем вложенную функцию
    def whisper(t):                      
        return t.lower() + '...'
    # вызываем вложенную функцию и возвращаем ее результат
    return whisper(text)                 

print(speak('Hello, World'))   

print('------------------')

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'

    if volume > 0.5:
        return yell
    else:
        return whisper

print('------------------')

whisper = get_speak_func(0.3)     # функция whisper()
yell = get_speak_func(0.7)        # функция yell()

print(whisper('Hello'))           # говорим шепотом
print(yell('Hello'))              # кричим

print('------------------')

def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    
    if volume > 0.5:
        return yell
    else:
        return whisper

yell = get_speak_func('Hello, World', 0.7)

print(yell())

print('------------------')

def closure():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(count)
    return inner

start = closure()
another = closure()             # другое замыкание, со своими локальными значениями

start()                         # выводит 1
start()                         # выводит 2

another()                       # выводит 1

start()                         # выводит 3

print('------------------')

def greeting_creator(greeting_word):
    def greet(name):
        return f'{greeting_word}, {name}'

    return greet

say_hi = greeting_creator('Hi')
say_hello = greeting_creator('Hello')

print(say_hi('Timur'))
print(say_hello('Soslan'))

print('------------------')

def make_adder(n):
    def add(x):
        return x + n
    return add

def multiplier_of(n):
    def mult(x):
        return x * n
    return mult

def make_adder(n):
    return lambda x: x + n

def multiplier_of(n):
    return lambda x: x * n

plus_3 = make_adder(3)
plus_5 = make_adder(5)
multiply_3 = multiplier_of(3)
multiply_5 = multiplier_of(5)

print(plus_3(10), plus_3(100))
print(plus_5(10), plus_5(100))
print(multiply_3(10), multiply_3(100))
print(multiply_5(10), multiply_5(100))

print('------------------')

def line_generator(k, b):
    def func(x):
        return k * x + b
    return func

line_func_1 = line_generator(2, 5)        # получаем функцию y = 2*x + 5
line_func_2 = line_generator(-6, 9)       # получаем функцию y = -6*x + 9

print(line_func_1(10))                    # печатаем значение 2*10 + 5
print(line_func_2(4))                     # печатаем значение -6*4 + 9

print('------------------')

def f(x):
    z = 2
    def g(y):
        # обращение к локальной переменной z и параметрической переменной x
        return z*x + y    
    return g

h = f(5)
print(h(1))

print('------------------')

# def outer_function():
#     num = 5
#     # определяем вложенную функцию
#     def inner_function():      
#         num += 10
#         print(num)
#     # вызываем вложенную функцию
#     inner_function()           
        
# outer_function()

print('------------------')

def outer_function():
    num = 5
    # определяем вложенную функцию
    def inner_function():      
        nonlocal num
        num += 10
        print(num)
    # вызываем вложенную функцию
    inner_function()           
        
outer_function()

print('------------------')

def outer_function(arg):
    num = 5
    name = 'Timur'
    numbers = [1, 2, 3]
    # определяем вложенную функцию
    def inner_function():      
        print(arg)
        print(num)
        print(numbers)
    # возвращаем вложенную функцию
    return inner_function      
        
inner = outer_function('python')

print(type(inner.__closure__))
print(*inner.__closure__)
for v in inner.__closure__:
    print(v)
print('*****')
for var in inner.__closure__:
    print(var.cell_contents)

print('------------------')