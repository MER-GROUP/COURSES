def Enter():
	try:
		cso=input('Введи целое число : ')
		if 'q'==cso:pass
		elif '0' in(cso[0]) or cso[0:2] in ('-0','+0'):raise ValueError
		else:cso=int(cso)
	except ValueError:
		print('Некоректный ввод')
		cso=None
	finally:
		return cso
		
def Factorial(cso):
	from math import factorial
	return factorial(cso)

def Main():
	while True:
		cso=None
		while cso is None:
			cso=Enter()
		if 'q'==cso:break
		else:
			print(Factorial(cso))
		
Main()