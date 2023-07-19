print('------------------')

def generate_ints(n):
    for num in range(n):
        yield num

print('------------------')

# создаем генератор, порождающий числа 0 1 2 3 4
generator1 = generate_ints(5)           

print(type(generator1))

print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))

# создаем генератор, порождающий числа 0 1 2
generator2 = generate_ints(3)           

for num in generator2:
    print(num)

# создаем генератор, порождающий числа 0 1
num1, num2 = generate_ints(2)           

print(num1, num2)

print('------------------')

class GenerateInts:   
    # конструктор принимает верхнюю границу диапазона                          
    def __init__(self, n):         
        self.n = n
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self): 
        if self.current == self.n:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

print('------------------')

# создаем итератор, содержащий числа 0 1 2 3 4
iterator1 = GenerateInts(5)           

print(type(iterator1))

print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))

# создаем итератор, содержащий числа 0 1 2
iterator2 = GenerateInts(3)           

for num in iterator2:
    print(num)

# создаем итератор, содержащий числа 0 1
num1, num2 = GenerateInts(2)          

print(num1, num2)

print('------------------')

def generate_1234():
    yield 1
    yield 2
    yield 3
    yield 4

# распаковка генератора
print(*generate_1234())         

print('------------------')

def generate_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')

for char in generate_AB():
    print('-->', char)

# gen = generate_AB()
# print(next(gen))
# print('--------')
# print(next(gen))
# print('--------')
# print(next(gen))

print('------------------')

def generate_ints():
    yield 1
    yield 2
    return 3
    yield 4

for num in generate_ints():
    print(num)

print('------------------')

def counter(low, high):
    for num in range(low, high + 1):
        yield num

counter1 = counter(3, 10)

for i in counter1:
    print(i)

counter2 = counter(100, 103)
print(next(counter2))
print(next(counter2))

print('------------------')

def even_numbers(begin):
    begin += begin % 2
    while True:
        yield begin
        begin += 2

print('------------------')

# все четные числа от 10 до бесконечности
evens1 = even_numbers(10)                     

for index, num in enumerate(evens1):
    if index > 5:
        break
    print(num)

# все четные числа от 102 до бесконечности
evens2 = even_numbers(101)                    

print(next(evens2))
print(next(evens2))
print(next(evens2))
print(next(evens2))

print('------------------')

def string_wrapper(text, symbol):
    for char in text:
        yield symbol + char + symbol

string_wrapper1 = string_wrapper('beegeek', '~')

for char in string_wrapper1:
    print(char)
 
string_wrapper2 = string_wrapper('Python', '+')
print(next(string_wrapper2))
print(next(string_wrapper2))
print(next(string_wrapper2))

print(list(string_wrapper('stepik', '-')))

print('------------------')

def factorials():
    value = 1
    index = 1
    while True:
        yield value
        index += 1
        value *= index

infinite_factorials = factorials()

for index, num in enumerate(infinite_factorials, 1):
    if index <= 10:
        print(f'Факториал числа {index} равен {num}')
    else:
        break

print('------------------')

def generate_1():
    yield 1

gen = generate_1()

print(dir(gen))

print('------------------')