def Global():
	global temp
	temp = int()
	
def ArrInput():
	try:
		return [int(input()) for _ in range(2)]
	except ValueError:
		print('некоректный ввод')
	
def Average(arr):
	return sum(arr) / len(arr)
	
def Main():
	for _ in range(5):
		print('-----Main()-----')
		arr = ArrInput()
		print(Average(arr))
		
Global()
Main()