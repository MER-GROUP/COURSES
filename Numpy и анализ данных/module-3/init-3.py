print('---------------------------')

import numpy as np

arr = np.array([1, 2, 3])
new_arr = np.append(arr, [4, 5, 6])
print(new_arr)

print('---------------------------')

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.delete(arr, [0, 1])
print(new_arr)

print('---------------------------')

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated_arr = np.concatenate((arr1, arr2))
print(concatenated_arr)

print('---------------------------')

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.hstack((a, b))
print(c)

print('---------------------------')

import numpy as np

arr = np.array([1, 2, 3])
repeated_arr = np.repeat(arr, 3)
print(repeated_arr)

print('---------------------------')

import numpy as np

arr = np.array([1, 2, 3])
arr.resize(5)
print(arr)

print('---------------------------')

import numpy as np

arr = np.array([1, 2, 3])
resized_arr = np.resize(arr, (5,))
print(resized_arr)

print('---------------------------')