print('---------------------------')

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)

print('---------------------------')

import numpy as np
a = np.array([4, 5, 6])
b = np.array([1, 2, 3])
c = a - b
print(c)

print('---------------------------')

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

print('---------------------------')

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a * b
print(c)

print('---------------------------')

import numpy as np
a = np.array([4, 6, 8])
b = np.array([2, 3, 4])
c = a / b
print(c)

print('---------------------------')

import numpy as np
a = np.array([1, 2, 3])
b = a ** 2
print(b)

print('---------------------------')

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.zeros(3)
for i in range(3):
    c[i] = a[i] * b[i] 
print(c)

print('---------------------------')

a = np.array([1, 2, 3]) 
b = np.array([4, 5, 6])
c = a * b 
print(c)

print('---------------------------')

import numpy as np
a = np.array([1, 2, -3])
b = np.array([0, 1, 0])
c = a / b
print(c) # >>> [ inf   2. -inf]

print('---------------------------')

import numpy as np
a = np.array([1e100, 2e100, 3e100])
b = np.array([1e-1000, 1e100, 1e100])
c = a / b
print(c)# >>> [inf  2.  3.]

print('---------------------------')

import numpy as np
a = np.array([np.inf, -np.inf, np.inf])
b = np.array([np.inf, np.inf, -np.inf])
c = a / b
print(c) # >>> [nan nan nan]

print('---------------------------')

import numpy as np
a = np.array([0, 0, 0])
b = np.array([0, 1, 2])
c = a / b
print(c) # >>> [nan  0.  0.]

print('---------------------------')