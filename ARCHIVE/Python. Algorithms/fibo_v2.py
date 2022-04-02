#числа Фибоначчи
def fibonacci(n):
	f1, f2 = 0, 1
	while 2 < n:
		f2, f1 = f1 + f2, f2
		n -= 1
	return f1 if n in (0, 1) else f2
	
for i in range(1, 10):
	print(fibonacci(i), end=' ')