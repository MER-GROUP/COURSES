# Наименьшее общее кратное двух чисел
def nok(a, b):
	i = a if a > b else b
	while True:
		if 0 == i % a and 0 == i % b:
			return i
		i += 1
		
print(nok(14, 6))