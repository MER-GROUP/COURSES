from random import randint
count = int()

def Enter():
	try:
		global count
		digit = str()
		if 1 == count:
			digit = input('Количество сирок : ')
		else:
			digit = input('Количество сто - в : ')
		if 'q' == digit:
			pass
		elif '0' == digit[0] and 1 < len(digit):
			raise ValueError
		elif digit[ : 2] in ('+0', '-0') and 2 < len(digit):
			raise ValueError
		else:
			digit = int(digit)
			if 1 == count:
				if 0 == digit:
					raise ValueError
	except ValueError:
		if type(str()) == type(digit):
			print('некоректный ввод')
		else:
			print('0 не может быть для строк')
		digit = None
	finally:
		return digit
		
def ArrInit(rows, cols):
	arrRows, arrCols = list(), list()
	for i in range(rows):
		for j in range(cols):
			arrCols.append(randint(0, 3))
		arrRows.append(list(arrCols))
		arrCols.clear()
	return arrRows
	
def ArrOut(arr):
	for i in arr:
		for j in i:
			print(f'{j : 3d}', end=' ')
		print()
		
def ArrOut_2(arr, arrSumR, arrSumC):
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			print(f'{arr[i][j] : 3d}', end='')
		print(f' | {arrSumR[i]}', end='')
		print()
	print('-' * 3 * len(arr[0]) + '-' * 5)
	for i in arrSumC:
		print(f'{i : 3d}', end='')
	print()
	
def ArrOut_3(arr, arrSumR, arrSumC):
	for i in range(len(arr)):
		print(arr[i], end=' | ')
		print(arrSumR[i])
	print('-' * len(arrSumC) * 4)
	print(arrSumC)
		
def ArrSumRows(arr):
	sum = [0] * len(arr)
	#print(sum)
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			sum[i] += arr[i][j]
	return sum
	
def ArrSumCols(arr):
	#print('do something')
	sum = [0] * len(arr[0])
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			sum[j] += arr[i][j]
	return sum

def Main():
	for _ in range(5):
		print('---Main---')
		global count
		rows = None
		cols = None
		count = 1
		while rows is None:
			rows = Enter()
		if 'q' == rows:
			break
		count += 1
		while cols is None:
			cols = Enter()
		if 'q' == cols:
			break
		arr = ArrInit(rows, cols)
		ArrOut(arr)
		print('---------------------------')
		print(ArrSumRows(arr))
		print('---------------------------')
		print(ArrSumCols(arr))
		print('---------------------------')
		ArrOut_2(arr, ArrSumRows(arr), ArrSumCols(arr))
		print('---------------------------')
		ArrOut_3(arr, ArrSumRows(arr), ArrSumCols(arr))
		
Main()