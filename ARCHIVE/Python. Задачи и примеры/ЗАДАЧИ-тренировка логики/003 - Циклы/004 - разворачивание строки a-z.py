def Enter():
	try:
		alph=ord(input('Буква : '))
		a=ord('a')
		z=ord('z')
		A=ord('A')
		Z=ord('Z')
		if a<=alph<=z or A<=alph<=Z:pass
		else:raise ValueError
	except ValueError:
		alph=None
		print('Некоректный ввод')
	except UnboundLocalError:
		alph=None
		print('Некоректный ввод')
	except TypeError:
		alph=None
		print('Некоректный ввод')
	finally:
		return alph
		
def Razvorot(alph1,alph2):
		if alph1<alph2:
			print('Разворот равен :')
			while alph1<=alph2:
				if ord('Z')<alph1<ord('a'):
					alph1+=1
					continue
				print(chr(alph1),end='')
				alph1+=1
			print()
		elif alph1>alph2:
			print('Разворот равен :')
			s=''
			while alph1>=alph2:
				if ord('Z')<alph1<ord('a'):
					alph1-=1
					continue
				print(chr(alph1),end='')
				s+=str(chr(alph1))
				alph1-=1
			print('\n'+''.join(reversed(s)))
			print()
			#print('В разработке')
		else:
			print('Разворот равен :')
			print(chr(alph1))
			
def Exit():
		try:
			e=input('q - выход, с - продолжить : ')
			if 'q'==e or 'c'==e:pass
			else:raise ValueError
		except ValueError:
			e=None
			print('Некоректный ввод')
		finally:
			return e
		
		
while True:
	print('Введи 2 буквы : ')
	alph1=None
	while None==alph1:
		alph1=Enter()
	alph2=None
	while None==alph2:
		alph2=Enter()
	#print(f'alph1={alph1} alph2={alph2}')
	Razvorot(alph1,alph2)
	e=None
	while None==e:
		e=Exit()
	if 'q'==e:break
	else:continue