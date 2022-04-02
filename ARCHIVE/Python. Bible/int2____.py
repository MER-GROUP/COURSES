cnt=1

def Chislo():
	try:
		if cnt==1:
			c=input('Введи число : ')
			if 'q'==c:
				#print(c)
				pass
			else:
				c=int(c)
		elif cnt==2:
			c=input('Введите систему счисления (2-9) : ')
			c=int(c)
			if 2<=c<=9:pass
			else:raise ValueError
		else:
			raise ValueError
	except ValueError:
		c=None
		print('Некоректный ввод')
	finally:
		#print(c)
		return c
		
while True:
	a=None
	while None==a:
		a=Chislo()
	if 'q'==a:quit()
	cnt+=1
	b=None
	while None==b:
		b=Chislo()
	cnt=1
	nN=''
	bb=a
	while 0<a:
		nN+=str(a%b)
		a//=b
	nN=''.join(reversed(nN))
	print(nN)
	print(int(nN,b))
	#проверка двоичности
	print(bin(bb))
	print(int(str(bin(bb)),2))