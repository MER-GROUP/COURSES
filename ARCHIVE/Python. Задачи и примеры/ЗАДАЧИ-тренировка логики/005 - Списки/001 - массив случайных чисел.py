from random import randint

def Main():
	i = int()
	while 10 > i:
		print('---Main---')
		arr = [randint(0, 51) for i in range(10)]
		print(arr)
		i += 1
		
		
Main()