def Enter():
	try:
		f=input('Введите ряд Фибоначи : ')
		if 'q'==f:pass
		elif '0' in (f[0]) or f[0:2] in ('-0','+0'):
			raise ValueError
		else:
			f=int(f)
	except ValueError:
		if '0' in (f[0]) or f[0:2] in ('-0','+0'):
			print('Нет 0 в ряде Фибоначи')
			print('Некоректный ввод')
		else:
			print('Некоректный ввод')
		f=None
	finally:
		return f
		
def Fibonachi(f):
	f1=f2=1
	print(f1,f2,end=' ')
	while 2<f:
		#можно без sum
		#f1,f2=f2,f1+f2
		sum=f1+f2
		f1=f2
		f2=sum
		print(f2,end=' ')
		f-=1
	print()

def Main():
	while True:
		f=None
		while f is None:
			f=Enter()
		if 'q'==f:break
		else:Fibonachi(f)

Main()
		