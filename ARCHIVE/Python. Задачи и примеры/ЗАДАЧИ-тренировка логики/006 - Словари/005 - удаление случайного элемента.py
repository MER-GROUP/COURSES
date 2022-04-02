from random import choice

def Global():
	global temp
	temp = int()
	
def DictInit():
	return {'max' : 35, 'mather' : 59, 'sister' : 39, 'father' : 59, 'ilias' : 14}
	
def Main():
	for _ in range(5):
		print('-----Main-----')
		myDict = DictInit()
		print(myDict)
		arr = list(myDict.keys())
		print(arr)
		#arr2 = list(myDict.values())
		#print(arr2)
		r = choice(arr)
		myDict.pop('max')
		print(myDict)
		del myDict[r]
		print(myDict)
		
Global()
Main()