# факториал числа
def factorial(n):
	if 0 == n: return 0
	elif 1 == n: return 1
	return n * factorial(n - 1)
	
print(factorial(5))