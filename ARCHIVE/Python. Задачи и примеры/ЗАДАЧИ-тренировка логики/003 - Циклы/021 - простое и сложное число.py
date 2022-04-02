def Enter():
	try:
		cso=input('Введи положительное целое число : ')
		if 'q'==cso:pass
		elif '0'==cso[0] and 1<len(cso) or '-'==cso[0] or '+0'==cso[0:2] and 2<len(cso):
			raise ValueError
		else:
			cso=int(cso)
	except ValueError:
		print('Некоректный ввод')
		cso=None
	finally:
		return cso
		
def Chislo(cso):
	if 1==cso or 0==cso:
		print('Число не простое и не составное')
	else:
		from math import sqrt
		stp=int(sqrt(cso))
		i=2
		chk=False
		while i<=stp:
			if 0==cso%i:
				chk=True
				break
			i+=1
		if True==chk:
			print('Число составное')
		else:
			print('Число простое')

def Main():
	while True:
		print('---Main---')
		cso=None
		while cso is None:
			cso=Enter()
		if 'q'==cso:break
		else:Chislo(cso)
Main()