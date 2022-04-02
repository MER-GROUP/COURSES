def Enter():
	try:
		cso=input('Введите целое число : ')
		if 'q'==cso:pass
		elif '0'==cso[0] or cso[0:2] in ('-0','+0'):
			raise ValueError
		else: cso=int(cso)
	except ValueError:
		print('Некоректный ввод')
		cso=None
	finally:
		return cso
		
def EvenOdd(sco):
	if 0==sco:
		print('Зеро !')
	else:
		sco=abs(sco)
		even=0
		odd=0
		while 0<sco:
			buf=sco%10
			if 0==buf%2:
				even+=1
			else:
				odd+=1
			sco//=10
		print(f'even = {even}')
		print(f'odd = {odd}')

def Main():
	while True:
		cso=None
		while cso is None:
			cso=Enter()
		if 'q'==cso:break
		else:EvenOdd(cso)
		
Main()