def Global():
	global temp
	temp = int()
	
def ArrInit1():
	return [i for i in range(1, 6)]
	
def ArrInit2():
	return [i for i in 'abcde']
	
def DictInit(arr1, arr2):
	res = dict()
	for i in range(len(arr1)):
		res[arr2[i]] = arr1[i]
	return res
	
def Main():
	for _ in range(5):
		print('-----Main-----')
		for k, v in DictInit(ArrInit1(), ArrInit2()).items():
			print(k, v)
	
Global()
Main()