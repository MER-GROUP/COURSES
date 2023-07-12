print('---------------------------')
import numpy as np

arr = np.arange(10, dtype=int)

arr[2:5] = np.array([10, 11, 12])
print(arr)

print('---------------------------')

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
slice_arr = arr[2:5]
slice_arr[1] = 100
print(arr)

print('---------------------------')

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
copy_arr = np.copy(arr[2:5])
copy_arr[1] = 100
print(arr)

print('---------------------------')