print('------------------')

# data = 'beegeek'
# data[0] = 'B'

# print(data)

print('------------------')

data = ['b', 'e', 'e', 'g', 'e', 'e', 'k']
data[0] = 'B'

print(data)

print('------------------')

nums = [1, 2, 3]

print(nums)
print(id(nums))

nums = [1, 2, 3] + [4]

print(nums)
print(id(nums))

print('------------------')

nums = [1, 2, 3]

print(id(nums))
print(nums)

nums.append(4)

print(id(nums))
print(nums)

print('------------------')

nums1 = [1, 2, 3]
nums2 = nums1

nums1.append(4)

print(nums1)
print(nums2)

print('------------------')

data = (1, 'bee', [1, 2, 3], {'a': 1})

print(data)

data[2][2] = 30
data[3]['b'] = 2

print(data)

print('------------------')

nums1 = [1, 2, 3]
nums2 = nums1

nums1 = nums1 + [4, 5]

print(nums1)
print(nums2)

print('------------------')

nums1 = [1, 2, 3]
nums2 = nums1

nums1 += [4, 5]

print(nums1)
print(nums2)

print('------------------')

def append(element, seq=[]):
    seq.append(element)
    return seq

print(append.__defaults__)
print(append(10))
print(append.__defaults__)
print(append(5))
print(append.__defaults__)
print(append(1))
print(append.__defaults__)
print(append(3))
print(append.__defaults__)

print('------------------')

def append(element, seq=None):
    if seq is None:
        seq = []
    seq.append(element)
    return seq

print(append.__defaults__)
print(append(10))
print(append.__defaults__)
print(append(5))
print(append.__defaults__)
print(append(1))
print(append.__defaults__)

print('------------------')

import sys


numbers = [1, 2, 3, 4]
first_size = sys.getsizeof(numbers)

print(f"numbers =, {numbers}")
print(f"size = {first_size} байт(а)")
print(f"id = {id(numbers)}", end='\n\n')

numbers.extend([5, 6, 7, 8, 9, 10])
second_size = sys.getsizeof(numbers)

print(f"numbers =, {numbers}")
print(f"size = {second_size} байт(а)")
print(f"id = {id(numbers)}")

print('------------------')

def foo(a=[], *, k={}):
    pass

print(foo.__defaults__)
print(foo.__kwdefaults__)

print('------------------')

def append(element, seq=None):
    seq = seq or []
    seq.append(element)
    return seq

print(append(10))
print(append(5))
print(append(1))

print('------------------')

def add_ten(data):
    data.append(10)
    return data

nums = [1, 2, 3]

print(nums, add_ten(nums), nums)

print('------------------')

def add_ten(data):
    data.append(10)
    return data

nums = [1, 2, 3]

print(nums)
print(add_ten(nums))
print(nums)

print('------------------')

def add_ten():
    data=[]
    data.append(10)
    return data

print(add_ten())
print(add_ten())
print(add_ten())

print('------------------')

def add_ten(data=[]):
    data.append(10)
    return data

print(add_ten())
print(add_ten())
print(add_ten())

print('------------------')