from math import sqrt

def Hypot(x,y):
	h=sqrt(x**2+y**2)
	return h
	
def Result(h,r):
	if h<=r:
		print('точка в круге')
	else:
		print('точка за пределами')

while True:
	try:
		x=input('x = ')
		if 'q'==x:break
		x=float(x)
		y=float(input('y = '))
		r=float(input('r = '))
	except ValueError:
		print('некоректный ввод')
		continue
	Result(Hypot(x,y),r)