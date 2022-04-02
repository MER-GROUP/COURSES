from random import randint
count = int()

def Enter():
	try:
		global count
		d = str()
		if 1 == count:
			d = input('Число строк : ')
		else:
			d = input('Число столбцов : ')
		if 'q' == d:
			pass
		elif '0' == d[0] and 1 < len(d):
			raise ValueError
		elif d[ : 2] in ('-0', '+0') and 2 < len(d):
			raise ValueError
		else:
			d = int(d)
			if 1 == count:
				if 0 == d:
					raise ValueError
	except ValueError:
		if type(str()) == type(d):
			print('Некоректный ввод')
		else:
			print(' 0 строк не может быть')
		d = None
	finally:
		return d
		
def Check(s):
	if 'q' == s:
		return True
		
def ArrInit(row_, col_):
	row = list()
	col = list()
	for i in range(row_):
		for j in range(col_):
			col.append(randint(0, 5))
		row.append(list(col))
		col.clear()
	return row
	
def ArrOut(arr):
	for i in arr:
		for j in i:
			print(f'{j : 3d}', end='')
		print()
		
def ArrRowMax(arr):
	rowSum = int()
	rowSumMax = int()
	it, row = int(), int()
	for i in arr:
		rowSum = sum(i)
		if rowSumMax < rowSum:
			rowSumMax = rowSum
			row = it
		it += 1
	print('row =', row, 'max =', rowSumMax)

def ArrColMax(arr):
	#colSum = int()
	#colSumMax = int()
	#it, col = int(), int()
	colSumArr = [0] * len(arr[0])
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			colSumArr[j] += arr[i][j]
	print('col =', colSumArr.index(max(colSumArr)), 'max =', max(colSumArr))

# 9 и 5 ошибка	
# работоет при квадратной матрице 5 на 5
'''
def ArrColMax_2(arr):
	colSum = int()
	colSumMax = int()
	it = int()
	for i in range(len(arr)):
		colSum = 0
		for j in range(len(arr[i])):
			colSum += arr[j][i]
		if colSumMax < colSum:
			colSumMax = colSum
			it = i
	print('col =', it, 'max =', colSumMax)
'''

# думает как проитерировать j	
def ArrColMax_3(arr):
	colSum = int()
	colSumMax = int()
	it = int()
	for j in range(len(arr[0])):
		colSum = 0
		for i in range(len(arr)):
			colSum += arr[i][j]
		if colSumMax < colSum:
			colSumMax = colSum
			it = j
	print('col =', it, 'max =', colSumMax)

def Main():
	for _  in range(5):
		print('---Main---')
		global count
		count = 1
		row = None
		while row is None:
			row = Enter()
		if Check(row): break
		count += 1
		col = None
		while col is None:
			col = Enter()
		if Check(col): break
		else:
			#print('Do something')
			arr = ArrInit(row, col)
			ArrOut(arr)
			ArrRowMax(arr)
			ArrColMax(arr)
			#ArrColMax_2(arr)
			ArrColMax_3(arr)
		
Main()