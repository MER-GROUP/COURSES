print('------------------')

from fractions import Fraction

# конструктор за кулисами вызывает магический метод __init__(3, 4)
frac1 = Fraction(3, 4)   
# конструктор за кулисами вызывает магический метод __init__(6, 9)   
frac2 = Fraction(6, 9)      

print('------------------')

class Counter:          
    # конструктор принимает два аргумента low и high (помимо self)                   
    def __init__(self, low, high):         
        self.low = low
        self.high = high
    
    def __iter__(self):
        return self
    
    def __next__(self): 
        if self.low > self.high:
            raise StopIteration
        else:
            self.low += 1
            return self.low - 1

print('------------------')

# создаем итератор Counter, передавая значения low=3, high=10
counter1 = Counter(3, 10)         

# неявно вызываем функцию next()
for i in counter1:                
    print(i)

# создаем итератор Counter, передавая значения low=100, high=103
counter2 = Counter(100, 103)   
# явно вызываем функцию next()   
print(next(counter2))   
# явно вызываем функцию next()          
print(next(counter2))             

print('------------------')

class EvenNumbers:  
    # конструктор принимает один аргумент begin (помимо self)                           
    def __init__(self, begin):                 
        self.begin = begin +  begin % 2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        value  = self.begin
        self.begin += 2
        return value

print('------------------')

# все четные числа от 10 до бесконечности
evens1 = EvenNumbers(10)                     

for index, num in enumerate(evens1):
    if index > 5:
        break
    print(num)

# все четные числа от 102 до бесконечности
evens2 = EvenNumbers(101)                    

print(next(evens2))
print(next(evens2))
print(next(evens2))
print(next(evens2))

print('------------------')

# # все четные числа от 2 до бесконечности
# evens = EvenNumbers(2)                     

# for num in evens:
#     print(num)

print('------------------')

class StringWrapper:                             
    def __init__(self, text, symbol):
        self.text = text
        self.symbol = symbol
        # вспомогательное поле для отслеживания текущего индекса
        self.index = -1                      
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index >= len(self.text):
            raise StopIteration
        return self.symbol + self.text[self.index] + self.symbol

print('------------------')

string_wrapper1 = StringWrapper('beegeek', '~')

for char in string_wrapper1:
    print(char)
 
string_wrapper2 = StringWrapper('Python', '+')

print(next(string_wrapper2))
print(next(string_wrapper2))
print(next(string_wrapper2))

print(list(StringWrapper('stepik', '-')))

print('------------------')

class Factorials:
    def __init__(self):
        self.value = 1
        self.index = 1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.value *= self.index
        self.index += 1
        return self.value

print('------------------')

infinite_factorials = Factorials()

for index, num in enumerate(infinite_factorials, 1):
    if index <= 10:
        print(f'Факториал числа {index} равен {num}')
    else:
        break

print('------------------')

text = 'beegeek'
print(text.upper())

print('------------------')

text = 'beegeek'
print(str.upper(text)) # self = text

print('------------------')

numbers = iter([1, 2, 3, 4, 5])
timur = iter(('Timur', 29, 'Male'))
text = iter('beegeek')
chars = iter({'a', 'b', 'c'})
info = iter({'name': 'Timur', 'age': 29, 'gender': 'Male'})
even_numbers = iter(range(2, 10, 2))

print(type(numbers))
print(type(timur))
print(type(text))
print(type(chars))
print(type(info))
print(type(even_numbers))

print('------------------')

class list_iterator:
    def __init__(self, data): 
        self.data = data
        self.index = -1
        
    def __iter__(self): 
        return self 
        
    def __next__(self):
        self.index += 1
        if self.index == len(self.data):
            raise StopIteration  
        return self.data[self.index]

print('------------------')

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

del numbers[2]

print(next(iterator))

print('------------------')