def Enter():
	try:
		a=input('Введи N : ')
		if 'q'==a:pass
		else:
			if a in('0','+0','-0'):raise ValueError
			elif '+0'==a[0:2] or '-0'==a[0:2]:
				raise ValueError
			else:a=int(a)
	except ValueError:
		if a in('0','+0','-0') or '+0'==a[0:2] or '-0'==a[0:2]:
			print('Нужно ввести больше 0 !')
		else:
			print('Некоректный ввод')
		a=None
	finally:
		return a
		
def Ryad(n):
	r=1
	while 0<n:
		print(r,end=' ')
		r/=-2
		n-=1
	print()

def Main():
	while True:
		n=None
		while n is None:
			n=Enter()
		if 'q'==n:break
		else:
			print('-----Main-----')
			Ryad(n)
		
Main()