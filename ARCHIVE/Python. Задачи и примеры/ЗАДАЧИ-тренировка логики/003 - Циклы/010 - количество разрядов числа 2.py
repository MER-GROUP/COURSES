def Enter():
	try:
		cso=input('Введите целое число : ')
		if 'q'==cso: pass
		else: cso=int(cso)
	except ValueError:
		cso=None
		print('Некоректный ввод')
	finally:
		return cso

'''		
def Razrad(cso):
	cso=abs(cso)
	cnt=0
	if 0==cso:
		cnt=1
		pass
	while 0<cso:
		cnt+=1
		cso//=10
	return cnt
'''

def Razrad(cso):
	cso=abs(cso)
	cnt=len(str(cso))
	return cnt

def Main():
	while True:
		print('Main')
		cso=None
		while cso is None:
			cso=Enter()
		if 'q'==cso: break
		print(f'Разрядов у {cso} = {Razrad(cso)}')
	
Main()