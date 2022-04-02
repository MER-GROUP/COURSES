from random import randint

def Zamena(arr):
	for i in range(len(arr)):
		if 0 < arr[i]:
			arr[i] = 1
		elif 0 > arr[i]:
			arr[i] = -1
	print(arr)

def Main():
	for _ in range(5):
		print('---Main---')
		arr = [randint(-10, 10) for i in range(10)]
		print(arr)
		Zamena(arr)
		
Main()