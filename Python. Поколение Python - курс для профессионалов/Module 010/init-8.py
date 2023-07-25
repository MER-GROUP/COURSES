print('------------------')

from sys import getsizeof

numbers = [1, 9, 8, 7, 90, -56, -34, 56, 100, 90, 2, 8]

even_numbers = [num for num in numbers if num % 2 == 0]

print(type(even_numbers))
print(even_numbers)
print(getsizeof(even_numbers))

print('------------------')

from sys import getsizeof

numbers = [1, 9, 8, 7, 90, -56, -34, 56, 100, 90, 2, 8]

# используем круглые скобки
even_numbers = (num for num in numbers if num % 2 == 0)         

print(type(even_numbers))
print(even_numbers)
print(getsizeof(even_numbers))

print('------------------')

# создаем генератор с помощью генераторного выражения
squares = (i ** 2 for i in range(1, 7))  
# создаем генератор с помощью генераторного выражения       
capitals = (s.upper() for s in 'abc')   
# создаем генератор с помощью генераторного выражения        
stars = ('*' for i in range(5))                 

for num in squares:
    print(num)

print(next(capitals))

print(*stars, end=' ')

print()
print('------------------')

# squares = i*i for i in range(10)
# print(*squares)

print('------------------')

print(sum(i*i for i in range(10)))          # передача без скобок
print(sum((i*i for i in range(10))))        # передача со скобками

print('------------------')

even_squares = (
                i ** 2
                for i in range(10)
                if i % 2 == 0
               )

even_squares = (i ** 2 for i in range(10) if i % 2 == 0)

print('------------------')

# squares = (i*i for i in range(10))
# print(len(squares))

print('------------------')

squares = (i*i for i in range(10))
print(squares)
print(*squares)

print('------------------')

# squares = (i*i for i in range(10))
# print(squares[7])

print('------------------')

# squares = (i*i for i in range(10))
# print(squares[1:6])

print('------------------')

squares = (i*i for i in range(10))

first, second = next(squares), next(squares)

nums1 = list(squares)
nums2 = list(squares)

print(first)
print(second)
print(nums1)
print(nums2)

print('------------------')

fruits = ['apple', 'apricot', 'avocado', 'pineapple', 'banana', 'bergamot', 'durian', 'grapefruit']

fruits_filter = filter(lambda s: len(s) > 7, fruits)
fruits_map = map(lambda s: s.upper(), fruits)
fruits_filter_map = map(lambda s: s.upper(), filter(lambda s: len(s) > 7, fruits))

print(*fruits_filter)
print(*fruits_map)
print(*fruits_filter_map)

print(type(fruits_filter))
print(type(fruits_map))

print('------------------')

fruits = ['apple', 'apricot', 'avocado', 'pineapple', 'banana', 'bergamot', 'durian', 'grapefruit']

fruits_filter = (s for s in fruits if len(s) > 7)
fruits_map = (s.upper() for s in fruits)
fruits_filter_map = (s.upper() for s in fruits if len(s) > 7)

print(*fruits_filter)
print(*fruits_map)
print(*fruits_filter_map)

print(type(fruits_filter))
print(type(fruits_map))

print('------------------')

from sys import getsizeof

range_object = range(1000000)
list_object = list(range_object)
filter_object = filter(lambda num: True, range_object)
map_object = map(lambda num: num, range_object)
generator_object = (num for num in range_object)

print(getsizeof(range_object))
print(getsizeof(list_object))
print(getsizeof(filter_object))
print(getsizeof(map_object))
print(getsizeof(generator_object))

print('------------------')

squares_tuple = tuple(i*i for i in range(5))
squares_list = list(i*i for i in range(5))
squares_set = set(i*i for i in range(5))

print(squares_tuple, type(squares_tuple))
print(squares_list, type(squares_list))
print(squares_set, type(squares_set))

print('------------------')

numbers = range(10)

# Before
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]

# After
squared_evens = [
    n ** 2
    for n in numbers
    if n % 2 == 0
]

print('------------------')

# my_dict = {n: n**2 if n % 2 == 1 else n: n**4 for n in range(1, 10)} # Syntax Error: invalid syntax

print('------------------')