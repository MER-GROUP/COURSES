from random import randint

def Global():
	global temp
	temp = int
	
def ArrInit(arr, n, min, max):
	#arr = [randint(min, max) for _ in range(n)]
	for i in range(n):
		arr.append(randint(min, max))
	
def Main():
	for _ in range(5):
		print('-----Main()-----')
		arr = list()
		#arr = []
		n, min, max = int(input('n = ')) , int(input('min = ')), int(input('max = '))
		ArrInit(arr, n, min, max)
		print(arr)
Global()
Main()