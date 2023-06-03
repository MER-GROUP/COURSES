print('---------------------------')

# import numpy as np
# arr = np.array([1, 2, 2223], dtype=np.int8)

print('---------------------------')

import numpy as np
arr = np.array([1, 'two', [3, 4], {'five': 5}], dtype=object)
print(arr)

print('---------------------------')

import numpy as np
arr = np.array([1, 2, 3], dtype=np.int32)
print(arr)

print('---------------------------')

import numpy as np
arr = np.array([1, 2.5, '3'], dtype=None)
print(arr)

print('---------------------------')

import numpy as np
# Создаем массив данных с отсутствующими значениями
data = np.array([1.2, 2.5, np.nan, 3.8, np.nan])
# Выполняем операции с использованием NaN
print("Исходные данные: ", data)# Исходные данные:  [1.2 2.5 nan 3.8 nan]
print("Сумма данных: ", np.sum(data))# Сумма данных:  nan
print("Максимальное значение: ", np.max(data))# Максимальное значение:  nan
print("Минимальное значение: ", np.min(data)) # Минимальное значение:  nan

print('---------------------------')

import numpy as np

# Выполняем операцию извлечения квадратного корня из -1
result = np.array([np.sqrt(-1)])

# Результат будет NaN
print(result)

print('---------------------------')

import numpy as np
# Создаем массив данных с NaN значениями
data = np.array([1.2, 2.5, np.nan, 3.8, np.nan])
print(data)
# Создаем маску, исключающую значения NaN
mask = np.isnan(data)
print(mask)
# Применяем маску к массиву данных
filtered_data = data[~mask]
# Выводим отфильтрованные данные
print("Отфильтрованные данные: ", filtered_data) # Отфильтрованные данные:  [1.2 2.5 3.8]

print('---------------------------')

import numpy as np
arr = np.array([1, 2, 3], dtype=np.uint8)
arr[0] = -1
print(arr[0])

print('---------------------------')

import numpy as np
# Создаем массив целых чисел
arr = np.array([1, 2, 3, 4, 5])
# Преобразуем его в массив с плавающей точкой
arr_float = arr.astype(float)
print(arr_float) # out: [1. 2. 3. 4. 5.]

print('---------------------------')

import numpy as np
# Создаем массив с плавающей точкой
arr_float = np.array([1.2, 2.5, 3.7, 4.1, 5.9])
# Преобразуем его в массив целых чисел
arr_int = arr_float.astype(int)
print(arr_int) # [1 2 3 4 5]

print('---------------------------')

import numpy as np
# Создаем массив целых чисел
arr = np.array([1, 2, 3, 4, 5])
# Преобразуем его в массив булевых значений
arr_bool = arr.astype(bool)
print(arr_bool) # [ True True True True True]

print('---------------------------')

# Создаем массив целых чисел
arr_int = np.array([1, 2, 3, 4, 5])
# Преобразуем его в массив строк
arr_str = arr_int.astype(str)
print(arr_str) # ['1' '2' '3' '4' '5']

print('---------------------------')

import numpy as np
# Создаем массив с плавающей точкой
arr_float = np.array([1.2, 2.5, 3.7, 4.1, 5.9])
# Создаем массив целых чисел
arr_int = np.array([0, 1, 2, 3, 4], dtype=int)
# Преобразуем массив с плавающей точкой в массив целых чисел, 
# используя тип данных массива целых чисел
arr_int_from_float = arr_float.astype(arr_int.dtype)
print(arr_int_from_float)

print('---------------------------')