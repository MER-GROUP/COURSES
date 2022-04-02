from random import randint

def Viborka(arr):
	print('Viborka')
	print(arr)
	neg = list()
	pos = list()
	for i in arr:
		if 0 > i:
			neg.append(i)
		elif 0 == i:
			continue
		else:
			pos.append(i)
	print(neg)
	print(pos)

def Main():
	for _ in range(10):
		print('---Main---')
		arr = [randint(-10, 10) for i in range(10)]
		print(arr)
		'''
		neg = list()
		pos = list()
		for i in arr:
			if 0 > i:
				neg.append(i)
			elif 0 == i:
				continue
			else:
				pos.append(i)
		print(neg)
		print(pos)
		'''
		Viborka(arr)
		
Main()