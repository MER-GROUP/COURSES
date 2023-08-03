print('---------------------------')

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
mask = np.array([True, False, True, False, False])
filtered_arr = arr[mask]
print(filtered_arr) # [1, 3]

print('---------------------------')

import numpy as np
arr = np.array([-1, 2, -3, 4, -5])
negative_mask = arr < 0
print(negative_mask)
print(arr[arr<0])
negative_values = arr[negative_mask]
print(negative_values) # [-1, -3, -5]

print('---------------------------')

import numpy as np
a = np.array([1, 6, 3, 8, 4, 9])
mask = (a > 3) & (a < 7)
print(a[mask])

print('---------------------------')