def Enter():
	try:
		cso=input('Введите целое число : ')
		if 'q'==cso:pass
		else:
			cso=int(cso)
			if 0==cso:raise ValueError
	except ValueError:
		if 0==cso:
			print('Сумма = 0 и Произведение = 0')
		else:
			print('Некоректный ввод')
		cso=None
	finally:
		return cso
		
def Arithmetic(a):
	a=abs(a)
	sm=0
	pr=1
	while 0<a:
		dgt=a%10
		sm+=dgt
		pr*=dgt
		a//=10
	rst=(sm,pr)
	return rst

def Main():
	while True:
		cso=None
		while cso is None:
			cso=Enter()
		if 'q'==cso:break
		else:
			print(Arithmetic(cso))
	
Main()