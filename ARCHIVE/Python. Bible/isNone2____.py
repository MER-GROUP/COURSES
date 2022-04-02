a=None

def Chislo():
	try:
		global a
		a=input('введи число : ')
		a=int(a)
	except:
		print('исключение')
	else:
		return a

	
for i in range(5):			
	b=Chislo()
	print(b)
	if b is None:
		print('досрочный выход')
		break