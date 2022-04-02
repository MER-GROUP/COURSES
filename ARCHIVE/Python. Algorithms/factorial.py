# факториал числа
def factorial(n):
	f = int(1)
	for i in range(1, n + 1):
		f *= i
	return 1 if 0 == n else f
	
print(factorial(5))
print(factorial(0))
print(factorial(1))