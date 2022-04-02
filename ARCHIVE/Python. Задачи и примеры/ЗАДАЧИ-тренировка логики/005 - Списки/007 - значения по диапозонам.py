from random import randint

def Output(arr):
	for i in range(1, len(arr) + 1):
		print(f'{arr[i - 1] : 3d}', end=' ')
		if 0 == i % 5:
			print()
	print()
	
def Algo(arr):
	count03, count47, count810 = 0, 0, 0
	for i in arr:
		if 0 <= i <= 3:
			count03 += 1
		elif 4 <= i <= 7:
			count47 += 1
		else:
			count810 += 1
	print('0 - 3 :',count03)
	print('4 - 7 :',count47)
	print('8 - 10 :', count810)

def Main():
	for _ in range(5):
		print('---Main---')
		arr = [randint(0, 10) for i in range(20)]
		Output(arr)
		Algo(arr)
		
Main()