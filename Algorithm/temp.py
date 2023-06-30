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