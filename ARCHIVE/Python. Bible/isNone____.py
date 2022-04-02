def Chislo():
	try:
		a=input('введи число : ')
		a=int(a)
	except:
		print('исключение')
	else:
		return a

	
for i in range(5):			
	a=Chislo()
	print(a)
	if a is None:
		print('досрочный выход')
		break