from random import randint

def SetCount(myList, mySet):
	myDigit, myCount = int(), int()
	maxCount = int()
	for i in mySet:
		myCount = myList.count(i)
		if myCount > maxCount:
			maxCount = myCount
			myDigit = i
	print('maxCount =', maxCount)
	print('myDigit =', myDigit)

def Main():
	for _ in range(5):
		print('---Main---') 
		myList = [randint(1,5) for i in range(10)]
		print(myList)		
		mySet = set(myList)
		SetCount(myList, mySet)
		
Main()