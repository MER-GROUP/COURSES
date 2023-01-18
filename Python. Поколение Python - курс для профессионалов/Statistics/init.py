print('---------------------')

import statistics
from fractions import Fraction as F
from decimal import Decimal as D

print(statistics.mean([1, 2, 3, 4, 4]))
print(statistics.mean([-1.0, 2.5, 3.25, 5.75]))
print(statistics.mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)]))
print(statistics.mean([D('0.5'), D('0.75'), D('0.625'), D('0.375')]))

print('---------------------')

import statistics
from fractions import Fraction as F
from decimal import Decimal as D

print(statistics.fmean([1, 2, 3, 4, 4]))
print(statistics.fmean([-1.0, 2.5, 3.25, 5.75]))
print(statistics.fmean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)]))
print(statistics.fmean([D('0.5'), D('0.75'), D('0.625'), D('0.375')]))

print('---------------------')

import statistics
from fractions import Fraction as F
from decimal import Decimal as D

print(statistics.geometric_mean([1, 2, 3, 4, 4]))
print(statistics.geometric_mean([1.0, 2.5, 3.25, 5.75]))
print(statistics.geometric_mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)]))
print(statistics.geometric_mean([D('0.5'), D('0.75'), D('0.625'), D('0.375')]))

print('---------------------')

import statistics
from fractions import Fraction as F
from decimal import Decimal as D

print(statistics.harmonic_mean([1, 2, 3, 4, 4]))
print(statistics.harmonic_mean([1.0, 2.5, 3.25, 5.75]))
print(statistics.harmonic_mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)]))
print(statistics.harmonic_mean([D('0.5'), D('0.75'), D('0.625'), D('0.375')]))

print('---------------------')

import statistics
from fractions import Fraction as F
from decimal import Decimal as D

print(statistics.median([1, 2, 3, 4, 4]))
print(statistics.median([1.0, 2.5, 3.25, 5.75]))
print(statistics.median([F(3, 7), F(1, 21), F(5, 3), F(1, 3)]))
print(statistics.median([D('0.5'), D('0.75'), D('0.625'), D('0.375')]))

print('---------------------')

import statistics
from fractions import Fraction as F
from decimal import Decimal as D

data1 = [1.0, 2.5, 3.25, 5.75]
data2 = [F(3, 7), F(1, 21), F(5, 3), F(1, 3)]

print(statistics.median_low(data1), statistics.median_high(data1))
print(statistics.median_low(data2), statistics.median_high(data2))

print('---------------------')

import statistics

print(statistics.mode([1, 1, 2, 3, 3, 3, 3, 4]))
print(statistics.mode([1, 1, 2, 3, 3, 3, 3, 4, 1, 1, 1]))

print('---------------------')

import statistics

print(statistics.mode(['red', 'blue', 'blue', 'red', 'green', 'red', 'red']))
print(statistics.mode('abcccddeec'))
print(statistics.mode([True, False, True, False, False]))

print('---------------------')

import statistics

print(statistics.multimode('aabbbbccddddeeffffgg'))
print(statistics.multimode(['a', 'cc', 'dd', 'a', 'ee', 'dd', 'ee', 'f', 'a']))
print(statistics.multimode(['a', 'cc', 'dd', 'a', 'ee', 'dd', 'ee', 'f', 'dd', 'a']))
print(statistics.multimode([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))
print(statistics.multimode([]))

print('---------------------')

import statistics

modes = statistics.multimode([5, 5, 2, 2, 5, 4, 3, 1, 1, 1, 2])

print(min(modes))
print(max(modes))

print('---------------------')