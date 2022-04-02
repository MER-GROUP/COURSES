#числа Фибоначчи
def fibonacci(n):
	if n in (0, 1): return 1
	elif n in (2, 3): return 1
	return fibonacci(n - 1) + fibonacci(n - 2)
	
for i in range(1, 10):
	print(fibonacci(i), end=' ')