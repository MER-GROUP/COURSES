n = int(input())
'''
a, b, fibo = int(1), int(), int()
for i in range(n):
	if 0 == i:
		print(a, end=' ')
	else:
		fibo = a + b
		print(fibo, end=' ')
		a, b = fibo, a
'''
a, b = 1, 1
for i in range(n):
	print(a, end=' ')
	a, b = b, a + b