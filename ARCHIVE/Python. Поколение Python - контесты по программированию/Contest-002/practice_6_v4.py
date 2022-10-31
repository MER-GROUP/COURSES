from math import gcd
from functools import reduce
from collections import Counter


line = input()

d = Counter(line)
n = reduce(gcd, d.values())

print(n)