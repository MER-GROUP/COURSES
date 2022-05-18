from math import gcd
from functools import reduce

s = input()
s2 = set(s)
sdict = {}
for i in s2:
    sdict[i] = s.count(i)
lst = list(map(int, sdict.values()))
print(reduce(gcd, lst))