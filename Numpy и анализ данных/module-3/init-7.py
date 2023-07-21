print('---------------------------')

import numpy as np
a = np.array([1, 2, 3])
b = np.array([2, 2, 2])
print(np.greater(a, b)) # >>> Output: [False False True]
print(a > b) # >>> Output: [False False True]

print('---------------------------')

import numpy as np
a = np.array([1, 2, 3])
b = np.array([2, 2, 2])
print(np.less(a, b)) # >>> Output: [True False False]
print(a < b) # >>> Output: [True False False]

print('---------------------------')

import numpy as np
a = np.array([1, 2, 3])
b = np.array([2, 2, 2])
print(np.equal(a, b)) # Output: [False True False]
print(a == b) # Output: [False True False]

print('---------------------------')

import numpy as np
a = np.array([1, 2, 3])
b = np.array([2, 2, 2])
print(np.greater_equal(a, b)) # Output: [False True True]
print(a >= b) # Output: [False True True]

print('---------------------------')

import numpy as np
a = np.array([1, 2, 3])
b = np.array([2, 2, 2])
print(np.less_equal(a, b)) # Output: [True True False]
print(a <= b) # Output: [True True False]

print('---------------------------')

import numpy as np
a = np.array([1, 2, 3])
b = np.array([2, 2, 2])
print(np.not_equal(a, b)) # Output: [True False True]
print(a != b) # Output: [True False True]

print('---------------------------')

import numpy as np
a = np.array([False, False, True])
b = np.array([False, False, False])
print(np.any(a)) # Output: True
print(np.any(b)) # Output: False

print('---------------------------')

import numpy as np
a = np.array([True, True, True])
b = np.array([True, False, True])
print(np.all(a)) # Output: True
print(np.all(b)) # Output: False

print('---------------------------')