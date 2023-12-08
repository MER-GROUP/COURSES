print('---------------------------')

import numpy as np
# Создание массива
arr = np.array([1, 2, 3, 4, 5])
# Поиск индексов элементов, которые больше 2
indices = np.where(arr > 2)
# Вывод результатов
print(indices) # (array([2, 3, 4], dtype=int64),)

print('---------------------------')

import numpy as np
# Создание массива
arr = np.array([1, 2, 3, 4, 5])
# Замена значений, которые больше 2, на 0
arr[np.where(arr > 2)] = 0
# Вывод результатов
print(arr) # [1 2 0 0 0]

print('---------------------------')

import numpy as np
# Создание массива
arr = np.array([1, 2, 3, 4, 5])
# Поиск индексов элементов, которые больше 2 и меньше 5
indices = np.where((arr > 2) & (arr < 5))
# Вывод результатов
print(indices) # (array([2, 3], dtype=int64),)

print('---------------------------')

import numpy as np
# Создание массива
arr = np.array([1, 2, 3, 4, 5])
# Создание нового массива на основе условия
new_arr = np.where(arr > 2, arr, 0)
# Вывод результатов
print(new_arr) # [0 0 3 4 5]

print('---------------------------')

import numpy as np
# Создание двух массивов
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
# Нахождение индексов элементов, которые больше 2 в обоих массивах
indices = np.where((arr1 > 2) & (arr2 > 2))
# Вывод результатов
print(indices) # (array([2, 3, 4], dtype=int64),)

print('---------------------------')

import numpy as np
# Создание массива с NaN-значениями
arr = np.array([1, np.nan, 3, np.nan, 5])
# Замена NaN-значений на 0
new_arr = np.where(np.isnan(arr), 0, arr)
# Вывод результатов
print(new_arr) # [1. 0. 3. 0. 5.]

print('---------------------------')

import numpy as np
# Создание массива
arr = np.array([1, 2, 3, 4, 5])
# Создание маски для поиска значений
mask = np.array([True, False, True, False, True])
# Нахождение значений по маске
result = np.where(mask, arr, 0)
# Вывод результатов
print(result) # [1 0 3 0 5]

print('---------------------------')

import numpy as np
# Создание массива
arr = np.array([1, 2, 3, 4, 5])
# Создание новых массивов на основе условий
arr1 = np.where(arr > 2, 1, 0) # [0, 0, 1, 1, 1]
arr2 = np.where(arr % 2 == 0, arr, 0) # [0, 2, 0, 4, 0]
# Вывод результатов
print(arr1)
print(arr2)

print('---------------------------')