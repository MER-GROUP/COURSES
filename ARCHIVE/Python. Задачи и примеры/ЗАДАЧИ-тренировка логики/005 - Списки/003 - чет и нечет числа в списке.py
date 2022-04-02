from random import randint

def Enter():
	try:
		d = input()
		if 'q' == d:
			pass
		else:
			d = int(d)
			if 0 == d:
				raise IndexError
	except (ValueError, IndexError):
		print('Некоректный ввод')
		d = None
	finally:
		return d
		
def oddEven(nArr):
	even = int()
	odd = int()
	arr = [randint(0, 100) for i in range(nArr)]
	print(arr)
	for i in arr:
		if 0 == i % 2:
			even += 1
		else:
			odd += 1
	print('even =', even)
	print('odd =', odd)

def Main():
	while True:
		print('---Main---')
		nArr = None
		while nArr is None:
			nArr = Enter()
		if 'q' == nArr:
			break
		else:
			oddEven(nArr)
		
Main()