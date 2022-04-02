def Enter():
	try:
		cso=input('Введи целое число : ')
		if 'q'==cso:pass
		elif '0'==cso[0] and 1<len(cso):
			raise ValueError
		else: cso=int(cso)
	except ValueError:
		print('Некоректный ввод')
		cso=None
	finally:
		return cso
		
def Nod(a,b):
	try:
		while 0!=a and 0!=b:
			if a>b:
				a%=b
			else:
				b%=a
		rst=a+b
		print('NOD =',rst)
	except ZeroDivisionError:
		print('На ноль делить нельзя !')

def Main():
	while True:
		print('---Main---')
		a=None
		while a is None:
			a=Enter()
		if 'q'==a:break
		b=None
		while b is None:
			b=Enter()
		Nod(a,b)
		
Main()