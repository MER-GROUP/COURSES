# функция и аргументы
def printab_1(a, b, *args):
	print(a)
	print(b)
	for i in args:
		print(i, end=' ')
	print()
		
def printab_2(a, b, **kwargs):
	print(a)
	print(b)
	for k, v in kwargs.items():
		print(k, v)
		
printab_1(10, 20, 30, 40, 50)
printab_2(1, 2, c=3, d=4, red=5)