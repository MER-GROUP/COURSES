print('-------------------------')

import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)
print(type(my_array))
print(my_list)
print(type(my_list))

print('-------------------------')

import numpy as np

zeros_array = np.zeros(5) 
ones_array = np.ones(5)
random_array = np.random.rand(5)
print(zeros_array)
print(ones_array)
print(random_array)

print('-------------------------')

arr = np.empty(10, dtype=int)
print(arr)

print('-------------------------')

arr = np.empty(0)
print(arr)

print('-------------------------')

arr = np.array(list('123456789'), dtype=int)
print(arr)

print('-------------------------')

import numpy as np 
# Создание массива 2x3, заполненного значением 7 
arr = np.full((2,3), 7) 
print(arr) 
# Вывод: 
# [[7 7 7] 
# [7 7 7]] 

print('-------------------------')

arr = np.full(5, 7) 
print(arr) 

print('-------------------------')

import numpy as np
range_array = np.arange(1, 6)
linspace_array = np.linspace(1, 5, 5)
print(range_array)
print(linspace_array)

print('-------------------------')

import numpy as np
range_array = np.arange(1, 6)
linspace_array = np.linspace(2.3, 5.7, 10)
print(range_array)
print(linspace_array)

print('-------------------------')

import numpy as np
range_array = np.arange(1, 6)
linspace_array = np.linspace(2, 5, 3)
print(range_array)
print(linspace_array)

print('-------------------------')

# import numpy as np

# user_input = input("Введите несколько чисел, разделенных пробелом: ")
# user_array = np.array(user_input.split(), dtype=float)
# print(user_array)

print('-------------------------')

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.zeros_like(a)
print(b)  # [0 0 0 0]

print('-------------------------')