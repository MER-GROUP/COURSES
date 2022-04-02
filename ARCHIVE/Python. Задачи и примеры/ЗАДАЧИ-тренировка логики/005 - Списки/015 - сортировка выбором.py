from random import randint

def EnterRand():
	myList = [randint(-10, 10) for _ in range(10)]
	return myList
	
def SortV(arr):
	for i in range(len(arr) - 1, 0, -1):
		index = 0
		for j in range(1, i + 1):
			if arr[index] > arr[j]:
				index, j = j, index
		arr[i], arr[index] = arr[index], arr[i]

def Main():
	for _ in range(5):
		print('---Main---')
		myList = EnterRand()
		print(myList)
		SortV(myList)
		print(myList)
		
Main()