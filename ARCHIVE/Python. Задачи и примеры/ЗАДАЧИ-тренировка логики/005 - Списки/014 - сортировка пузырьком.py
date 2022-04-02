from random import randint

def EnterRand():
	myList = [randint(-10,10) for i in range(10)]
	return myList
	
def SortBuble(arr):
	for i in range(len(arr) - 1):
		for j in range(len(arr) - 1 - i):
			if arr[j] > arr[j + 1]:
				arr[j + 1], arr[j] = arr[j], arr[j + 1]

def Main():
	for _ in range(5):
		print('---Main---')
		myList = EnterRand()
		print(myList)
		SortBuble(myList)
		print(myList)
		
Main()