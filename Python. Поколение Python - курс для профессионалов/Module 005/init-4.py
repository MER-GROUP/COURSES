print('------------------')

import sys

nums = [1, 2, 3] 
print(sys.getrefcount(nums))

print('------------------')

import sys

nums = [1, 2, 3]                            # ссылка 1
nums1 = nums                                # ссылка 2
nums2 = nums1                               # ссылка 3
temp = [4, 5, 6, nums, nums1, nums2]        # ссылка 4, 5, 6
print(sys.getrefcount(nums))                # ссылка 7

print('------------------')

nums1 = [1, 2, 3]
nums2 = [4, 5]

nums1.append(nums2)
nums2.append(nums1) 

print(nums1)
print(nums2)

print('------------------')

nums = [1, 2, 3]
nums.append(nums)

print(nums)

print('------------------')

import sys

print(sys.getrefcount(0))     # число 0
print(sys.getrefcount(1))     # число 1
print(sys.getrefcount(''))    # пустая строка
print(sys.getrefcount(()))    # пустой кортеж

print('------------------')

import sys

print(sys.getrefcount([]))       # пустой список
print(sys.getrefcount({}))       # пустой словарь
print(sys.getrefcount(set()))    # пустое множество

print('------------------')

# import objgraph
# objgraph.show_refs([y], filename='sample-graph.png')

print('------------------')

import sys
import datetime
import fractions

print(sys.getrefcount(0))

print('------------------')

import sys

nums1 = [1, 2, 3]
nums2 = [nums1]
print(nums2)
nums3 = nums2 * 10
print(nums3)
print(sys.getrefcount(nums1))

print('------------------')