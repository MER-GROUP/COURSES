from math import sqrt

def isFloat(a):
	try:
		float(a)
		return True
	except ValueError:
		return False

while True:
    a=input('Введите число (Q-выход) :')
    if a=='q' or a=='Q':
    	break
    elif a.isdigit():
    	q=sqrt(int(a))
    	print(f'Корень {a} = {q:.2f}')
    elif isFloat(a):
    	q=sqrt(float(a))
    	print(f'Корень {a} = {q:.2f}')
    else:
    	print('Некоректный ввод')