from random import random

def GenArr():
	arr = [int(random() * 100) for _ in range(100)]
	return arr
	
def BinarySearch(find, arr):
	low = 0
	hight = len(arr) - 1
	#mid = len(arr) // 2
	while low <= hight:
		mid = (hight + low) // 2
		if find < arr[mid]:
			hight = mid - 1
			#mid = hight
		elif find > arr[mid]:
			low = mid + 1
			#mid = low
		else:
			print('find :', arr[mid])
			break
	else:
		print('No find')

def Main():
	for _ in range(5):
		print('---Main---')
		arr = GenArr()
		print(arr)
		print('----------')
		arr.sort()
		print(arr)
		find = int(input())
		BinarySearch(find, arr)
		
Main()