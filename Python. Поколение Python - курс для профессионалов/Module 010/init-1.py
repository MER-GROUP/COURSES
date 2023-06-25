print('------------------')

numbers = [1, 2, 3]
name = 'python'

# итерируем по списку, перебирая каждый элемент
for num in numbers:        
    print(num)

# итерируем по строке, перебирая каждый символ
for c in name:             
    print(c)

# неявное итерирование по списку
print(2 in numbers)   
# неявное итерирование по строке     
print('A' in name) 
# неявное итерирование по списку при распаковке        
print(*numbers)            

print('------------------')

numbers = [1, 2, 3]
# создаем итератор на основании списка
iterator = iter(numbers)          
# запрашиваем и печатаем первый элемент итератора
print(next(iterator))   
# запрашиваем и печатаем второй элемент итератора          
print(next(iterator))  
# запрашиваем и печатаем третий элемент итератора           
print(next(iterator))             

print('------------------')

# numbers = [1, 2, 3]
# # создаем итератор на основе списка
# iterator = iter(numbers)          
# # запрашиваем и печатаем первый элемент итератора
# print(next(iterator))     
# # запрашиваем и печатаем второй элемент итератора        
# print(next(iterator))    
# # запрашиваем и печатаем третий элемент итератора         
# print(next(iterator))             
# # возбуждается исключение StopIteration
# print(next(iterator))             

print('------------------')

numbers = [1, 2, 3, 4]            # список
letters = ('a', 'b', 'c')         # кортеж
language = 'python'               # строка

print(numbers[3])                 # обращение по индексу
print(letters[2])                 # обращение по индексу
print(language[5])                # обращение по индексу

print('------------------')

# letters = ('a', 'b', 'c')
# # создаем итератор на основе кортежа
# iterator = iter(letters)           
# # обращение по индексу
# print(iterator[1])                 

print('------------------')

numbers = [1, 2, 3, 4]

for num in numbers:
    print(num)

print('------------------')

numbers = [1, 2, 3, 4]

# создается итератор
iterator = iter(numbers)           

while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break

print('------------------')

# 5 чисел в последовательности
numbers = range(5)             

for num in numbers:
    print(num)

print('------------------')

from sys import getsizeof

# 5 чисел в последовательности
numbers1 = range(5)     
# 100000 чисел в последовательности             
numbers2 = range(100000)     
# 10000000000000 чисел в последовательности        
numbers3 = range(10000000000000)     

print(getsizeof(numbers1))
print(getsizeof(numbers2))
print(getsizeof(numbers3))

print('------------------')

from sys import getsizeof

# 5 чисел в списке
numbers1 = list(range(5)) 
# 100000 чисел в списке                 
numbers2 = list(range(100000))             

print(getsizeof(numbers1))
print(getsizeof(numbers2))

print('------------------')

# from sys import getsizeof

# # 10000000000000 чисел в списке
# numbers3 = list(range(10000000000000))     

# print(getsizeof(numbers3))

print('------------------')

sentence = 'In the face of ambiguity refuse the temptation to guess'

# фильтруем
filter_iterator = filter(lambda word: len(word) > 4, sentence.split()) 
# преобразовываем  
map_iterator = map(lambda word: word.upper(), filter_iterator) 
# нумеруем          
enumerate_iterator = enumerate(map_iterator, 1)                          

# выводим
for index, value in enumerate_iterator:                                  
    print(f'{index}. {value}')

print('------------------')

nums = iter([1, 2, 3, 4])

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums, -1))
print(next(nums, -1))

print('------------------')

# nums = [1, 2, 3, 4]

# print(next(nums))

print('------------------')

nums = [1, 2, 3, 4]
# создаем итератор
nums_iterator = iter(nums)       

print(type(nums))
print(type(nums_iterator))
print(next(nums_iterator))
print(next(nums_iterator))

print('------------------')

# numbers = [1, 2, 3, 4, 5, 6]

# evens = filter(lambda num: num % 2 == 0, numbers)
# print(len(evens))

print('------------------')

# 5 чисел в последовательности
numbers1 = range(5)      
# 100000 чисел в последовательности            
numbers2 = range(100000)   
# 10000000000000 чисел в последовательности          
numbers3 = range(10000000000000)     

print(len(numbers1))
print(len(numbers2))
print(len(numbers3))

print('------------------')

numbers = list(range(1, 10))

iterator1 = iter(numbers)
iterator2 = iter(numbers)
iterator3 = iter(numbers)

print(numbers)

print(next(iterator1))
print(next(iterator1))

print(next(iterator2))

print(next(iterator3))
print(next(iterator3))
print(next(iterator3))
print(next(iterator3))
print(next(iterator3))

print('------------------')