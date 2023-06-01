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