from random import randint

count = int()

def Enter():
	try:
		d = str()
		if 1 == count:
			d = input('количество строк : ')
		else:
			d = input('количество столбцов : ')
		if Check(d): pass
		elif '' == d: raise ValueError
		elif '0' == d[0] and 1 < len(d):
			raise ValueError
		elif d[ : 2] in ('-0', '+0') and 2 < len(d):
			raise ValueError
		else:
			d = int(d)
			if 0 == d: raise ValueError
	except ValueError:
		if type(d) == type(str()):
			print('некоректный ввод')
		elif 1 == count:
			print('0 строк не бывает')
		else:
			print('0 столбцов не бывает')
		d = None
	finally:
		return d
		
def Check(s):
	if 'q' == s: return True
	else: return False
	
def ArrInit(row, col):
	return [ [randint(10, 99) for _ in range(col)] for _ in range(row) ]
	
def ArrOut(arr):
	for i in arr:
		print(i)
		
def ArrSortCol(arr):
	col = len(arr[0]) - 1
	while 0 < col:
		max = 0
		for j in range(1, col + 1):
			if arr[0][max] < arr[0][j]:
				max = j
		for i in range(len(arr)):
			arr[i][max], arr[i][col] = arr[i][col], arr[i][max]
		col -= 1

def Main():
	while True:
		print('-----Main()-----')
		global count
		count = 0
		count += 1
		row = None
		while row is None:
			row = Enter()
		if Check(row): break
		count += 1
		col = None
		while col is None:
			col = Enter()
		if Check(col): break
		arr = ArrInit(row, col)
		ArrOut(arr)
		ArrSortCol(arr)
		print('--------------------')
		ArrOut(arr)
		
Main()