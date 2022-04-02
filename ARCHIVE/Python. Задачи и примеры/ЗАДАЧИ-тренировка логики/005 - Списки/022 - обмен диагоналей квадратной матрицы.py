from random import randint

def Enter():
	try:
		d = input('введи число : ')
		if 'q' == d: pass
		elif '0' == d[0] and 1 < len(d):
			raise ValueError
		elif d[ : 2] in ('+0', '-0') and 2 < len(d):
			raise ValueError
		else:
			d = int(d)
	except ValueError:
		print('некоректный ввод')
		d = None
	finally:
		return d
		
def ArrInitOut(n):
	arr, row = list(), list()
	for i in range(n):
		for j in range(n):
			row.append(randint(0, 100))
			print(f'{row[j] : 4d}', end='')
		print()
		arr.append(row.copy())
		row.clear()
	return arr

def ArrOut(arr):
	for i in arr:
		for j in i:
			print(f'{j : 4d}', end='')
		print()
		
def RevDiag(arr):
		for i in range(len(arr)):
			arr[i][i], arr[i][len(arr) - 1 - i] = arr[i][len(arr) - 1 - i], arr[i][i]
		
def Main():
	while True:
		print('-----Main()-----')
		d = None
		while d is None:
			d = Enter()
		if 'q' == d: break
		else:
			arr = ArrInitOut(d)
			print('----------')
			RevDiag(arr)
			print('----------')
			ArrOut(arr)
			print('----------')
			arr.clear()
		
Main()