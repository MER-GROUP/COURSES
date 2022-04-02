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
	'''
	fact=1
	while 0<cso:
		#print('Дописать факториал')
		fact*=cso
		cso-=1
	'''
	if 1==cso:return 1
	else:return cso*Factorial(cso-1)

def Main():
	while True:
		cso=None
		while cso is None:
			cso=Enter()
		if 'q'==cso:break
		else:
			print(Factorial(cso))
		
Main()