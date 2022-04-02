def Global():
	global temp
	temp = int()
	
def Average(arr):
	return sum(arr) / len(arr)
	
def Main():
	for _ in range(5):
		print('-----Main-----')
		print(Average([int(i) for i in input().split()]))
		
Global()
Main()