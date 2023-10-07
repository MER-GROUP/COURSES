print('---------------------------')

import numpy as np
# создаем одномерный массив
arr = np.array([1, 2, 3, 4, 5])
# применяем функцию add() к массиву
result = np.add(arr, 2)
print(result)# [3, 4, 5, 6, 7]
# применяем функцию sin() к массиву
result = np.sin(arr)
print(result)# [0.84147098, 0.90929743, 0.14112001, -0.7568025, -0.95892427]
# применяем функцию floor() к массиву
result = np.floor(arr / 2)
print(result)# [0, 1, 1, 2, 2]

print('---------------------------')

import numpy as np
# создаем одномерный массив
arr = np.array([1.23456789, 2.3456789, 3.456789])
# применяем функцию round() с параметром 3 к массиву
result = np.round(arr, 3)
print(result)# [1.235, 2.346, 3.457]

print('---------------------------')

import numpy as np
arr = np.array([1, 2, 3])
result = np.exp(arr)
print(result)# [2.71828183 7.3890561  20.08553692]

print('---------------------------')

import numpy as np
arr = np.array([2.71828183, 7.3890561, 20.08553692])
result = np.log(arr)
print(result)# [1. 2. 3.]

print('---------------------------')

import numpy as np
arr = np.array([4, 9, 16])
result = np.sqrt(arr)
print(result)# [2. 3. 4.]

print('---------------------------')

import numpy as np
arr = np.array([-1, -2, 3])
result = np.abs(arr)
print(result)# [1 2 3]

print('---------------------------')

import numpy as np
arr = np.array([-15, 0, 14])
result = np.sign(arr)
print(result)# [-1  0  1]

print('---------------------------')

import numpy as np
arr = np.array([2, 3, 4])
result = np.power(arr, 3)
print(result)# [ 8 27 64]

print('---------------------------')

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 1, 4])
result = np.maximum(arr1, arr2)
print(result)# [2 2 4]

print('---------------------------')

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 1, 4])
result = np.minimum(arr1, arr2)
print(result)# [1 1 3]

print('---------------------------')

import numpy as np
arr = np.array([1.1, 2.7, 3.4])
result = np.ceil(arr)
print(result)# [2. 3. 4.]

print('---------------------------')

import numpy as np
arr = np.array([1.1, 2.7, 3.4])
result = np.floor(arr)
print(result)# [1. 2. 3.]

print('---------------------------')

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
result = np.clip(arr, 2, 4)
print(result)# [2 2 3 4 4]

print('---------------------------')

import numpy as np
arr = np.array([1, 2, 3])
result = np.expm1(arr)
print(result)# [1.71828183 6.3890561  19.08553692]

print('---------------------------')

import numpy as np
arr = np.array([1, 2, 3])
result = np.log1p(arr)
print(result)# [0.69314718 1.09861229 1.38629436]

print('---------------------------')

import numpy as np
arr = np.array([True, False, True])
result = np.logical_not(arr)
print(result)# [False  True False]

print('---------------------------')

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1.01, 1.99, 3.01])
result = np.isclose(arr1, arr2, rtol=0.01, atol=0.01)
print(result)# [ True  True True]

print('---------------------------')

import numpy as np
arr1 = np.array([10, 20, 30])
arr2 = np.array([15, 25, 35])
result = np.gcd(arr1, arr2)
print(result)# [ 5  5 5]

print('---------------------------')

import numpy as np
arr1 = np.array([10, 20, 30])
arr2 = np.array([15, 25, 35])
result = np.lcm(arr1, arr2)
print(result)# [ 30 100 210]

print('---------------------------')