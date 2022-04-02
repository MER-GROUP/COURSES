def isFloat(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

while True:
	print('Q - выход')
	print('A(x1,y1):')
	x1=input('\t')
	if x1=='q' or x1=='Q':
		break
	y1=input('\t')
	print('B(x2,y2):')
	x2=input('\t')
	y2=input('\t')
	if ((x1.isdigit() and y1.isdigit() and
	     x2.isdigit() and y2.isdigit()) or
	     (isFloat(x1) and isFloat(y1) and
	     isFloat(x2) and isFloat(y2))):
	     	x1=float(x1)
	     	y1=float(y1)
	     	x2=float(x2)
	     	y2=float(y2)
	     	print('Equation :')
	     	k=(y1-y2)/(x1-x2)
	     	b=y2-k*x2
	     	print(f'\ty={k:.2f}*x+{b:.2f}')
	else:
		print('Некоректный ввод')