def Enter():
	try:
		cso=input('Введи целое число : ')
		if 'q'==cso:pass
		else:cso=int(cso)
	except ValueError:
		print('Некоректный ввод')
		cso=None
	finally:
		return cso
		
def Factorial(cso):
	fact=1
	while 0<cso:
		#print('Дописать факториал')
		fact*=cso
		cso-=1
	print(f'Factorial = {fact}')

def Main():
	while True:
		cso=None
		while cso is None:
			cso=Enter()
		if 'q'==cso:break
		else:Factorial(cso)
		
Main()