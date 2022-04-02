from random import randint

iCount = int()

def Enter():
	try:
		global iCount
		d = str()
		if 1 == iCount:
			d = input('Введи число строк : ')
		else:
			d = input('Введи число столбцов : ')
		if 'q' == d.lower():
			pass
		elif '0' == d[0] and 1 < len(d):
			raise ValueError
		elif d[ : 2] in ('-0', '+0') and 2 < len(d):
			raise ValueError
		else:
			d = int(d)
			if 1 == iCount:
				if 0 == d:
					raise ValueError
	except ValueError:
		#print(type(d))
		if type(str()) == type(d):
			print('Некоректный ввод')
		else:
			print('Количество строк не может быть нулевым')
		d = None
	finally:
		return d
		
def ArrInit_1(n, m):
	arrN = list()
	arrM = list()
	for i in range(n):
		#arrM = list()
		for j in range(m):
			arrM.append(randint(10, 99))
		arrN.append(list(arrM))
		arrM.clear()
	return arrN
	
def ArrOur_1(arr):
	for i in arr:
		for j in i:
			print(f'{j : 3d}', end=' ')
		print()
		
def ArrOut_2(arr):
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			print(f'{arr[i][j] : 3d}', end=' ')
		print()

def Main():
	while True:
		print('---Main---')
		global iCount
		iCount = 1
		n = None
		while n is None:
			n = Enter()
		if 'q' == n:
			break
		iCount += 1
		m = None
		while m is None:
			m = Enter()
		if 'q' == m:
			break
		print('-------------------------')
		arr = ArrInit_1(n, m)
		ArrOur_1(arr)
		print('xxxxxxxxxxxxxx')
		ArrOut_2(arr)
		
Main()