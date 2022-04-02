def ArrInit1():
	return [i for i in range(1, 6)]
	
def ArrInit2():
	return [i for i in 'abcde']
	
mydict = dict(zip(ArrInit2(), ArrInit1()))

for k, v in mydict.items():
	print(k, v)