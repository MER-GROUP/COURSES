from random import randint

def Enter():
	try:
		d = input('введи число : ')
		if 'q' == d: pass
		elif '' == d:
			raise ValueError
		elif '0' == d[0] and 1 < len(d):
			raise ValueError
		elif d[ : 2] in ('-0', '+0') and  2 < len(d):
			raise ValueError
		else:
			d = int(d)
	except ValueError:
		print('некоректный ввод')
		d = None
	finally:
		return d
		
def ArrInit(d):
	arr = [ [randint(0, 100) for _ in range(d)] for _ in range(d)]
	return  arr
	
def ArrOut(arr):
	for i in arr:
		for j in i:
			print(f'{j : 4d}', end='')
		print()
		
def SumDiag(arr):
	d1, d2 = int(), int()
	for i in range(len(arr)):
		d1 += arr[i][i]
		d2 += arr[i][len(arr) - 1 - i]
	print('d1 =', d1, 'd2 =', d2)

def Main():
	while True:
		print('-----Main()-----')
		d = None
		while d is None:
			d = Enter()
		if 'q' == d: break
		else:
			arr = ArrInit(d)
			ArrOut(arr)
			SumDiag(arr)
		
Main()