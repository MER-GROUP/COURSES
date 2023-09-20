print('----------')

from itertools import *
for a1, a2, a3 in permutations('0123456789', r = 3):
    if int(a1+a2+a3)*3 == int(a3*3):
        print(a1,a2,a3)

print('----------')

for i in range(1, 10):
    if (3 * i) % 10 == i:
        print(37 * i)

print('----------')

for i in range(100, 1000):
    if i * 3 == int(str(i)[2] * 3):
        print(i, i, i)

print('----------')

class add(int):
    def __call__(self, value):
        return add(self + value)
    
print(add())
print(add(1))
print(add(1)(2))
print(add(1)(2)(3))
print(add(1)(2)(3)(4))
print(add(1)(2)(3)(4)(5))
print('*****')
add_two = add(2)
print(add_two)
print(add_two + 5)
print(add_two(3))
print(add_two(3)(5))
print('*****')
print(add(2) + add(10))
print(add(10) - add(10))
print(add(3) * add(10))
print('*****')
add_two = add(2)
print(add_two + add(1000))
print(add_two + add_two)
print(add_two * 10)
print(add_two // 2)
print(add_two / 2)

print('----------')

arr = [1, 2, 3, 4, 5]
arr_slice = arr[:4]

print(arr)
print(arr_slice)

arr_slice.sort(reverse=True)

print(arr)
print(arr_slice)

print('----------')