d = int(input())
fact = int(1)
total = int(0)
for i in range(1, d + 1):
	for j in range(1, i + 1):
		fact *= j
	total += fact
	fact = 1
print(total)

from math import factorial
d = int(input())
total = int()
for i in range(1, d + 1):
	total += factorial(i)
print(total)