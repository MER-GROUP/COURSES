# Наименьшее общее кратное двух чисел
def nok(a, b):
	c = a * b
	while 0 != a and 0 != b:
		if a > b: a %= b
		else: b %= a
	return c // (a + b)

print(nok(14, 6))