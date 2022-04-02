from random import randint

count = int()

def Enter():
	try:
		d = str()
		if 1 == count:
			d = input('количество строк : ')
		else:
			d = input('количество столбцов : ')
		if 'q' == d: pass
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
			print('0 не может быть строк')
		else:
			print('0 не может быть столбцов')
		d = None
	finally:
		return d
		
def Check(s):
	if 'q' == s: return True
	else: return False
	
def ArrInit(row, col):
	return [ [randint(0, 100) for _ in range(col)] for _ in range(row)]
	
def ArrOut(arr):
	for i in arr:
		for j in i:
			print(f'{j : 4d}', end='')
		print()
		
def SearchInRow(arr, search):
	for i in range(len(arr)):
		if search in arr[i]:
			print(i, end=' ')
	print('... index in row')
	
def SeachInCol(arr, search):
	for j in range(len(arr[0])):
		for i in range(len(arr)):
			if search == arr[i][j]:
				print(j, end=' ')
				break
	print('... index in col')

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
		search = int(input('число для поиска от 0 до 100 : '))
		arr = ArrInit(row, col)
		ArrOut(arr)
		SearchInRow(arr, search)
		SeachInCol(arr, search)
		
Main()