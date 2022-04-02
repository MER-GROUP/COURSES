from random import randint

def Average(arr):
	total = int()
	average = float()
	for i in arr:
		total += i
	average = total / len(arr)
	return average
	
def Print(arr, averange):
	for i in arr:
		if i > averange:
			print(i, end=' ')
	print()

def Main():
	for i in range(5):
		print('---Main---')
		arr = [randint(0, 9) for i in range(10)]
		print(arr)
		averange = Average(arr)
		print(averange)
		Print(arr, averange)
		
Main()