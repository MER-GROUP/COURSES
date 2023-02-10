print('------------------')

name = 'Timur'
age = 29
is_teacher = True

print(id(name))
print(id(age))
print(id(is_teacher))

print('------------------')

nums1 = [1, 2, 3]
nums2 = [1, 2, 3]

print(nums1 == nums2)
print(id(nums1))
print(id(nums2))

print('------------------')

nums1 = [1, 2, 3]
nums2 = nums1

print(id(nums1))
print(id(nums2))

print('------------------')

nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
nums3 = nums1

print(nums1 is nums2, nums1 == nums2)
print(nums1 is nums3, nums1 == nums3)
print(nums2 is nums3, nums2 == nums3)

print('------------------')

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

print(hex(id(nums1)))
print(hex(id(nums2)))

print('------------------')

x = 1
print(id(x)) # => 1409681916176
y = 1
print(id(y)) # => 1409681916176
print(x is y) # => True

y = pow(10, 30, 10**30-2) # => 1
print(id(y)) # => 1409688059312
print(x, y, x is y) # => 1, 2, False

print('------------------')

a, b, c, = 10, 10, 1
print(id(a), id(b), id(c), sep='\n')

a, b, c, = 1000000000, 1000000000, 1000000000
print(id(a), id(b), id(c), sep='\n')

print('------------------')

x = 1
print(id(x)) # => 1409681916176
y = 1
print(id(y)) # => 1409681916176
print(x is y) # => True

y = pow(10, 30, 10**30-1) # => 1
print(id(y)) # => 1409688059312
print(x, y, x is y) # => 1, 1, False

print('------------------')

nums1 = [1, 2, 3, 4, 5]
print(id(nums1))

nums2 = nums1
print(id(nums2))

nums1 = [1, 2, 3, 4, 5]
print(id(nums1))

print('------------------')

s1 = 'beegeek'

s2 = s1.lower()
s3 = s1.upper()

print(s1)

print('------------------')

num1 = 100
num2 = 100

num3 = 1000
num4 = 1000

print(num1 is num2, num1 == num2)
print(num3 is num4, num3 == num4)

print('------------------')

num1 = 100 
num2 = int(100)
num3 = int('100')
num4 = 1 + 2 + 97

print(id(num1))
print(id(num2))
print(id(num3))
print(id(num4))

print('------------------')

s1 = 'beegeek'
s2 = 'beegeek'
s3 = 'bee' + 'geek'

print(id(s1))
print(id(s2))
print(id(s3))

print('------------------')

s1 = 'beegeek!'
s2 = 'beegeek!'

print(id(s1))
print(id(s2))

print('------------------')

s1 = 'b' * 4096
s2 = 'b' * 4096

s3 = 'b' * 5000
s4 = 'b' * 5000

print(s1 is s2)
print(s3 is s4)

print('------------------')

s1 = 'степик!'
s2 = 'степик!'

print(s1 is s2)

print('------------------')

import sys

s1 = sys.intern('степик!')
s2 = sys.intern('степик!')

print(s1 is s2)

print('------------------')

nums1 = (1, 'a', (3, 4), True, 6.7)
nums2 = (1, 'a', (3, 4), True, 6.7)
print(nums1 is nums2) # True
print(nums1 == nums2) # True
print(id(nums1), id(nums2)) # два одинаковых числа

print('------------------')